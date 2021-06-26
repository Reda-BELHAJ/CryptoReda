import argparse
import pprint
from typing import Optional, Sequence
from Utilities import *

def read(args: dict):
    if args['input'] is not None:
        pprint.pprint(args['input'])
    if args['output'] is not None:
        pprint.pprint(args['output'])
    if args['decrypt']:
        pprint.pprint(args['decrypt'])
    if args['encrypt']:
        pprint.pprint(args['encrypt'])
    if args['file'] is not None:
        pprint.pprint(args['file'])

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input',help="Specify the Input String.")
    parser.add_argument('-f', '--file',help="Specify the Input File String.")
    parser.add_argument('-e', '--encrypt',help="Encrypt the input using the CryptoReda Algorithm.", action="store_true")
    parser.add_argument('-d', '--decrypt',help="Decrypt the input using the CryptoReda Algorithm.", action="store_true")
    parser.add_argument('-o', '--output',help="Specify the output file.")

    args   = parser.parse_args(argv)

    read(vars(args))

    # pprint.pprint(vars(args))

    return 0

if __name__ == '__main__':
    exit(main())