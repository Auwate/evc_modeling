"""
An argument parser class
"""

import argparse
from argparse import ArgumentParser, Namespace
from libs.singleton import Singleton
from libs.log import Log

class CLIOptions(metaclass=Singleton):
    """
    A command-line arguments reader class.

    It uses argparse to streamline argument parsing and validation.
    """
    def __init__(
            self,
            parser: ArgumentParser = None,
            args: Namespace = None):
        self._logger = Log("CLIOptions")

        self._data_file = None
        self._schema_file = None
        self._log_level = None
        self.evaluate_args(parser, args)

    def evaluate_args(
            self,
            parser: ArgumentParser,
            args: Namespace) -> None:
        """
        Evaluate the given args and assign variables. If args and parsers is not given,
        read every from scratch
        """
        if not parser:
            self._logger.debug("Arguments were not given.")
            parser = self._create_parser()
            args = parser.parse_args()

        self._assign_values(args)

    def _assign_values(self, args: Namespace) -> None:
        """
        Assign each value from args.
        """
        self.data_file = args.data_file
        self.schema_file = args.schema_file
        self.log_level = args.log_level

    def _create_parser(self) -> ArgumentParser:
        """
        Create a default parser with all the desired CLI args
        """
        parser = argparse.ArgumentParser()

        parser.add_argument(
            "--data-file",
            help="The location of the data file. Default is 'data.yml' in the current directory.",
            default="data.yml",
            dest='data_file'
        )

        parser.add_argument(
            "--schema-file",
            help="The location of the schema file. Default is 'schema.yml' in the current "\
            "directory.",
            default="./schema/schema.yml",
            dest='schema_file'
        )

        parser.add_argument(
            "--log-level",
            help="The desired logging level. Available levels include INFO, DEBUG, WARN, "\
                "ERROR, and CRITICAL.",
            default="INFO",
            dest='log_level'
        )

        return parser

    # Getters/Setters

    @property
    def data_file(self) -> str:
        """ Getter """
        return self._data_file

    @data_file.setter
    def data_file(self, data_file: str) -> None:
        """ Setter """
        if not isinstance(data_file, str):
            raise ValueError("Data file must be a String.")
        self._data_file = data_file

    @property
    def schema_file(self) -> str:
        """ Getter """
        return self._schema_file

    @schema_file.setter
    def schema_file(self, schema_file: str) -> None:
        """ Setter """
        if not isinstance(schema_file, str):
            raise ValueError("Schema file must be a String.")
        self._schema_file = schema_file

    @property
    def log_level(self) -> str:
        """ Getter """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level: str) -> None:
        """ Setter """
        if not isinstance(log_level, str):
            raise ValueError("Log level must be a valid level.")
        self._log_level = log_level
