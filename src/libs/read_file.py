"""
A YAML file reader and validator
"""

from typing import List, Tuple, Any
import yamale
from libs.log import Log

class DataReader:
    """
    A utility class for importing data from operators.

    Imports a YAML file, then validates it against schema using yamale
    """
    def __init__(self, schema_file: str):
        self._logger = Log(class_name="DataReader")
        self._schema = self._setup_schema(schema_file=schema_file)

    def read(self, source_file: str) -> List[Tuple[Any, Any | None]]:
        """
        Read data from the source file
        """
        try:
            self._logger.debug(f"Attempting to read from {source_file}")

            data: List[Tuple[Any, Any | None]] = yamale.make_data(path=source_file)

            self._logger.debug("Data successfully read")

            return self._evaluate(parsed_data=data)
        except FileNotFoundError as exc:
            raise ValueError(f"Data file {source_file} could not be found.") from exc
        except Exception as exc:
            raise exc

    def _evaluate(self, parsed_data: List[Tuple[Any, Any | None]]) -> List[Tuple[Any, Any | None]]:
        """
        Take parsed data (in YAML) and return the data if data is correct
        """
        try:
            yamale.validate(schema=self._schema, data=parsed_data)
            return parsed_data
        except Exception as exc:
            raise exc

    def _setup_schema(self, schema_file: str):
        """
        Parse the schema and return it as a Python object
        """
        try:
            return yamale.make_schema(path=schema_file)
        except FileNotFoundError as exc:
            raise ValueError(f"Schema file {schema_file} could not be found.") from exc
        except Exception as exc:
            raise exc
