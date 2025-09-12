"""
Main method
"""

from libs.log import Log
from libs.read_file import DataReader
from libs.cli import CLIOptions

def main() -> int:
    """
    Main
    """
    args = CLIOptions()
    logger = Log(args.log_level)
    data = DataReader(args.schema_file)

    parsed = data.read(args.data_file)
    print(parsed)

if __name__ == "__main__":
    main()