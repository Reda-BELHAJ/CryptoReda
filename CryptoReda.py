import argparse
import pprint
import sys
from typing import Optional, Sequence
from Utilities import encryption, decryption

def write_if_possible(args):
    try:
        with args.output as file:
            pprint.pprint(args['output'])
    except:
        pass

def read_if_possible(args):
    try:
        with args.file as file:
            result = file.read().replace('\n', '')
    except:
        result = ""
    
    return result

def get_input(parser, vars: dict, args):
    if vars['input'] is not None and vars['key'] is None:
        parser.error("argument -i/--input requires argument --key.")

    if vars['input'] is not None and vars['file'] is not None:
        parser.error("argument -i/--input can't be with argument --file Choose one input argument.")

    if vars['file'] is not None and vars['key'] is None:
        parser.error("argument -f/--file requires argument --key.")

    if vars['input'] is not None:
        input = vars['input']

    if vars['file'] is not None:
        input = read_if_possible(args)
    
    return input


def read(parser, vars: dict, args):
    input = get_input(parser, vars, args)

    if vars['decrypt'] and (vars['key'] is None or input == ""):
        parser.error("argument -d/--decrypt requires argument --key and argument --input or --file.")

    elif vars['decrypt'] and (vars['key'] is not None and input != ""):
        pprint.pprint("Decryption")
        pprint.pprint(decryption.decrypt(input, vars['key']))

    if vars['encrypt'] and (vars['key'] is None or input == "" ):
        parser.error("argument -e/--encrypt requires argument --key and argument --input or --file.")

    elif vars['encrypt'] and (vars['key'] is not None and input != ""):
        pprint.pprint("Encryption")
        pprint.pprint(encryption.encrypt(input, vars['key']))
    

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input',help="Specify the Input String.")
    parser.add_argument('-f', '--file',help="Specify the Input File String.", type=argparse.FileType('r'))
    parser.add_argument('-e', '--encrypt',help="Encrypt the input using the CryptoReda Algorithm.", action="store_true")
    parser.add_argument('-d', '--decrypt',help="Decrypt the input using the CryptoReda Algorithm.", action="store_true")
    parser.add_argument('-k', '--key',help="Specify the key String.")
    parser.add_argument('-o', '--output',help="Specify the output file.", type=argparse.FileType('w'))

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        return -1
    else:
        args   = parser.parse_args(argv)

        read(parser, vars(args), args)

        # pprint.pprint(vars(args))

        return 0

if __name__ == '__main__':
    exit(main())