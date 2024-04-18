import sys
sys.path.append('./src')

from . import __version__

from dotenv import load_dotenv

import json
import argparse
import tempfile
from datetime import datetime

from lignator.commands import (
    process,
    headers
)

from lignator import DataTable
from lignator import logger


"""
Archivo normal o STDIN como input

"""
def file_or_stdin(path):
    if path:
        logger.info(f"for file {path}")

        file = open(path, 'rb')
    else:
        logger.info(f"for file stdin")

        temp = tempfile.TemporaryFile("w+b")
        data = sys.stdin.buffer.read()
        temp.write(data)
        temp.seek(0)
        file = temp

    return file


def main():
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="acción a ejecutar")
    parser.add_argument("--file", help="archivo a procesar")
    parser.add_argument('--start-time', type=datetime.fromisoformat, help="Tiempo de inicio")
    parser.add_argument('--end-time', type=datetime.fromisoformat, help="Tiempo de término")
    args = parser.parse_args()

    logger.info(f"command {args.command}")

    result = {}

    match args.command:
        case 'headers':
            file = file_or_stdin(args.file)
            dt = DataTable(file)

            response = headers(dt)
            result['headers'] = response

            print(json.dumps(result, default=str))
            return 0

        case 'process':
            file = file_or_stdin(args.file)
            dt = DataTable(file)

            result['headers']   = headers(dt)
            result['processed'] = process(dt, start_time=args.start_time, end_time=args.end_time)

            print(json.dumps(result, default=str))
            return 0

        case 'version':
            print(__version__)
            return 0

        case _:
            message = f"{args.command} command not supported"
            logger.error(message)
            print(message, file=sys.stderr)
            return 1


if __name__ == "__main__":
    main()
