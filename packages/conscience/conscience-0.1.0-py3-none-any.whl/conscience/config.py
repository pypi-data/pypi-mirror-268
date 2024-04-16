import traceback
from io import BytesIO
from pathlib import Path
from types import ModuleType
from typing import NoReturn, Optional, TypedDict, override

import importlib.util
from behave.__main__ import Configuration
from behave.formatter.base import Formatter, StreamOpener
from loguru import logger

from conscience.formatters import GradescopeFormatter
from conscience.score import (
    EMPTY_SCORE,
    GradescopeResults,
    error_results,
    read_results_from_stream,
)
from conscience.suite import ConscienceSuite


class GradeScopeMetadata(TypedDict):
    student_categories: str
    student_metadata: str


def load_under_test(path: Path):
    """Loads the supplied path as the `Software Under Test`, as behave.py requires the
    libary to be loaded already.
    Parameters:
        path: The path to the file to load.
    """
    spec = importlib.util.spec_from_file_location("under_test", path)
    if spec is None:
        raise ModuleNotFoundError(f"Could not find spec at {path}")

    module = importlib.util.module_from_spec(spec)
    # Adding these checks to shutup type errors
    if spec.loader is None:
        raise Exception("Could not find loader on spec:", spec)

    spec.loader.exec_module(module)
    return module


class ConscienceConfiguration(Configuration):
    def __init__(self, command_args=None, load_config=True, verbose=None, **kwargs):
        super().__init__(command_args, load_config, verbose, **kwargs)
        self.suite: Optional[ConscienceSuite] = None
        self.paths: list[str] = []
        self.under_test: Optional[ModuleType] = None
        self.more_formatters: Optional[dict[str, type[Formatter]]] = None
        self.working_directory: Optional[Path] = None

    def load_target(self, target: Path):
        self.under_test = load_under_test(target)

    def load_metadata(self, metadata: GradeScopeMetadata):
        pass

    def handle_load_failure(self, e: Exception) -> GradescopeResults | NoReturn:
        raise e

    def reset_outputs(self):
        pass

    def read_results(self) -> GradescopeResults:
        return {"tests": [EMPTY_SCORE]}


class GradescopeConfiguration(ConscienceConfiguration):
    def __init__(self, command_args=None, load_config=True, verbose=None, **kwargs):
        super().__init__(command_args, load_config, verbose, **kwargs)
        self.student_categories: Optional[str] = None
        self.student_metadata: Optional[str] = None
        self.default_format = "gradescope"
        self.more_formatters = {"gradescope": GradescopeFormatter}

    @override
    def reset_outputs(self):
        logger.debug("Setting up output stream")
        self.output_stream = BytesIO()
        self.outputs = [StreamOpener(stream=self.output_stream)]

    def handle_load_failure(self, e: Exception):
        return error_results(traceback.format_exc())

    @override
    def load_metadata(self, metadata: GradeScopeMetadata):
        self.student_categories = metadata["student_categories"]
        self.student_metadata = metadata["student_metadata"]

    @override
    def read_results(self) -> GradescopeResults:
        return read_results_from_stream(self.output_stream)


def build_config(
    is_gradescope: bool = False,
) -> ConscienceConfiguration:
    """Factory to build a config with the appropriate arguments for its type."""
    extra_args = [] if not is_gradescope else ["--no-summary"]
    command_args = ["--no-source", "--no-timings"] + extra_args
    clz = GradescopeConfiguration if is_gradescope else ConscienceConfiguration
    return clz(command_args=command_args)


def setup_config(
    config: ConscienceConfiguration,
    suite: ConscienceSuite,
    tests: list[Path],
    steps_dir: Path = Path("steps"),
    environment_file: Path = Path("../environment.py"),
    working_directory: Path = Path("."),
    metadata: Optional[GradeScopeMetadata] = None,
):
    """Sets up a ConscienceConfiguration with the supplied parameters.

    Parameters:
        config: The config to modify
        suite: The ConscienceSuite with features enabled to inject into the config.
        tests: A list of paths to the folders that behave will look in to find features.
            For some god awful reason, the environment_file and steps_dir arguments are relative
            to the paths listed here, and I'm unsure of what happens when we give multiple paths.
        steps_dir: The folder in which behave will look for the feature steps. This is relative to
            the tests path.
        environment_file: A file which specifies hooks to be run between steps or features etc.
            Once again, this is relative to the tests directory.
        working_directory: During testing, we will chdir into this directory before we look at
            paths.
        metadata: Some gradescope metadata to inject into the config if it's a gradescope config.
    """

    config.steps_dir = steps_dir.as_posix()
    config.paths = [path.as_posix() for path in tests]
    config.environment_file = environment_file.as_posix()
    config.suite = suite
    config.working_directory = working_directory
    config.log_capture = False

    if metadata:
        config.load_metadata(metadata)
