import argparse
import pprint
from typing import Optional, Sequence
from Utilities import encryption, decryption

def read(parser, args: dict):
    if args['input'] is not None and args['key'] is None:
        parser.error("argument -i/--input requires argument --key.")

    if args['decrypt'] and (args['key'] is None or args['input'] is None):
        parser.error("argument -d/--decrypt requires argument --key and argument --input.")
    elif args['decrypt'] and (args['key'] is not None and args['input'] is not None):
        pprint.pprint("Decryption")
        pprint.pprint(decryption.decrypt(args['input'], args['key']))

    if args['encrypt'] and (args['key'] is None or args['input'] is None):
        parser.error("argument -e/--encrypt requires argument --key and argument --input.")
    elif args['encrypt'] and (args['key'] is not None and args['input'] is not None):
        pprint.pprint("Encryption")
        pprint.pprint(encryption.encrypt(args['input'], args['key']))
    
    try:
        with args.file as file:
            pprint.pprint(args['file'])
    except:
        pass
        

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input',help="Specify the Input String.")
    parser.add_argument('-f', '--file',help="Specify the Input File String.", type=argparse.FileType('r'))
    parser.add_argument('-e', '--encrypt',help="Encrypt the input using the CryptoReda Algorithm.", action="store_true")
    parser.add_argument('-d', '--decrypt',help="Decrypt the input using the CryptoReda Algorithm.", action="store_true")
    parser.add_argument('-k', '--key',help="Specify the key String.")
    parser.add_argument('-o', '--output',help="Specify the output file.")

    args   = parser.parse_args(argv)

    read(parser ,vars(args))

    # pprint.pprint(vars(args))

    return 0

if __name__ == '__main__':
    exit(main())