import os
import shutil

from Shared.certoraUtils import run_compiler_cmd, VYPER, CompilerVersion, version_triplet_regex
from pathlib import Path
from functools import lru_cache
from typing import Dict, Set, Callable
import re
import logging
from EVMVerifier.Compiler.CompilerCollector import CompilerLang, CompilerCollector
from EVMVerifier.Compiler.CompilerCollectorSol import CompilerCollectorSol, CompilerLangSol
from EVMVerifier.Compiler.CompilerCollectorYul import CompilerLangYul, CompilerCollectorYul
from EVMVerifier.Compiler.CompilerCollectorVy import CompilerCollectorVy, CompilerLangVy
from Shared.certoraUtils import is_windows, match_path_to_mapping_key, remove_file, get_certora_config_dir
from EVMVerifier.certoraContextClass import CertoraContext

# logger for running the Solidity compiler and reporting any errors it emits
compiler_logger = logging.getLogger("compiler")


def get_relevant_compiler(contract_file_path: Path, default_compiler: str, compiler_mappings: Dict[str, str]) -> str:
    """
    @param contract_file_path: the contract that we are working on
    @param compiler_mappings: input arg mapping contract to compiler
    @param default_compiler: compiler we want to run in case the specified file_name is not in compiler_mappings
    @return: the name of the compiler executable we want to run on this contract (as a string, could be a path
             or a resolvable executable name)
    """
    match = None
    if compiler_mappings:
        match = match_path_to_mapping_key(contract_file_path, compiler_mappings)
    if match is not None:
        base = match
    else:
        base = default_compiler
    if is_windows() and not base.endswith(".exe"):
        base = base + ".exe"
    compiler_logger.debug(f"relevant compiler is {base}")
    return base


class CompilerCollectorFactory:
    """
    Returns [CompilerCollector] instance, based on type of the file [file_name] and the file path
    compiler_args: input args optimize and optimize_runs
    optimize_map: input arg mapping contract to optimized number of runs
    compiler_mappings: input arg mapping contract to the compiler executable (solc/vyper)
    default_compiler: compiler exec we want to run in case the specified file_name is not in compiler_mappings

    We added context as first step of making it the only parameters (the other params already appear in Context)
    """

    def __init__(self, context: CertoraContext, default_compiler: str,
                 compiler_mappings: Dict[str, str]):
        self.context = context
        self._default_compiler = default_compiler
        self._compiler_mappings = compiler_mappings

        self._stdout_paths_to_clean: Set[Path] = set()
        self._stderr_paths_to_clean: Set[Path] = set()

    @lru_cache(maxsize=32)
    def get_compiler_collector(self, path: Path) -> CompilerCollector:
        """
        1. Same file path will get the same compiler collector
        2. autoFinder_X file will get the compiler collector of X file
        @returns [CompilerCollector] instance, based on type of the file [file_name] and the file path
        @param path: path of the file to create [CompilerCollector] for
        """
        if str(path).endswith(".vy"):
            version = self.__get_vyper_version(path)
            return CompilerCollectorVy(version)
        elif str(path).endswith(".sol"):
            version = self.__get_solc_version(path)

            return CompilerCollectorSol(version, CompilerLangSol(), not self.context.do_not_use_memory_safe_autofinders)
        elif str(path).endswith(".yul"):
            version = self.__get_solc_version(path)
            return CompilerCollectorYul(version, CompilerLangYul())
        else:
            raise RuntimeError(f'expected {path} to represent a Solidity, Yul, or Vyper file')

    @staticmethod
    def get_vyper_compiler(contract_file_path: Path, default_compiler: str, compiler_mappings: Dict[str, str]) -> str:
        """
        @param contract_file_path: the contract that we wish to compile
        @param default_compiler: the default compiler for the contract
        @param compiler_mappings: mappings from context mapping files to the relevant compiler executable
        @return: the name of the compiler executable to run
        """
        vyper_location = shutil.which(VYPER, os.F_OK)
        if vyper_location is not None:
            # has vyper. use it
            compiler = VYPER
        else:
            compiler = default_compiler

        vyper_exec = get_relevant_compiler(contract_file_path, compiler, compiler_mappings)
        return vyper_exec

    def __get_vyper_version(self, contract_file_path: Path) -> CompilerVersion:
        """
        @param contract_file_path: the contract that we are working on
        @return: the running Vyper version
        """
        vyper_exec_to_run = self.get_vyper_compiler(contract_file_path, self._default_compiler, self._compiler_mappings)
        version = self.__get_compiler_exe_version(vyper_exec_to_run, self.__version_string_handler_vyper)
        return version

    def __get_solc_version(self, contract_file_path: Path) -> CompilerVersion:
        """
        @param contract_file_path: the contract that we are working on
        @return: the running solc version
        """
        compiler_logger.debug(f"visiting contract file {contract_file_path}")
        solc_path = get_relevant_compiler(contract_file_path, self._default_compiler, self._compiler_mappings)
        version = self.__get_compiler_exe_version(solc_path, self.__version_string_handler_solc)
        return version

    @lru_cache(maxsize=32)
    def __get_compiler_exe_version(self, compiler_name: str,
                                   version_string_handler: Callable[[str], CompilerVersion]) -> CompilerVersion:
        """
        @param compiler_name: name of the solc we want to run on this contract
        @return: the running compiler version
        """
        out_name = f"version_check_{Path(compiler_name).name}"
        stdout_path = get_certora_config_dir() / f'{out_name}.stdout'
        stderr_path = get_certora_config_dir() / f'{out_name}.stderr'
        self._stdout_paths_to_clean.add(stdout_path)
        self._stderr_paths_to_clean.add(stderr_path)

        run_compiler_cmd(
            f"{compiler_name} --version",
            wd=Path(os.getcwd()),
            output_file_name=out_name)

        with stdout_path.open() as r:
            version_string = r.read(-1)
        return version_string_handler(version_string)

    @staticmethod
    def __version_string_handler_vyper(version_string: str) -> CompilerVersion:
        version_matches = re.findall(version_triplet_regex(), version_string, re.MULTILINE)
        if len(version_matches) != 1:
            msg = f"Couldn't extract Vyper version from output {version_string}, giving up"
            compiler_logger.debug(msg)
            raise RuntimeError(msg)
        match = version_matches[0]
        return int(match[0]), int(match[1]), int(match[2])

    @staticmethod
    def __version_string_handler_solc(version_string: str) -> CompilerVersion:
        version_matches = re.findall(version_triplet_regex(prefix="Version: "), version_string, re.MULTILINE)
        if len(version_matches) != 1:
            msg = f"Couldn't extract Solidity version from output {version_string}, giving up"
            compiler_logger.debug(msg)
            raise RuntimeError(msg)
        match = version_matches[0]
        return int(match[0]), int(match[1]), int(match[2])

    def __del__(self) -> None:
        for path in self._stdout_paths_to_clean:
            remove_file(path)
        for path in self._stderr_paths_to_clean:
            remove_file(path)


def get_compiler_lang(file_name: str) -> CompilerLang:
    """
    Returns [CompilerLang] instance, based on type of the file [file_name]
    :param file_name: name of the file to create [CompilerLang] from
    """
    if file_name.endswith(".vy"):
        return CompilerLangVy()
    elif file_name.endswith(".sol"):
        return CompilerLangSol()
    elif file_name.endswith(".yul"):
        return CompilerLangYul()
    else:
        raise RuntimeError(f'expected {file_name} to represent a Solidity or Vyper file')
