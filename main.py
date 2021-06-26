import argparse
import pprint
from typing import Optional, Sequence

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument('-i')

    args   = parser.parse_args(argv)

    pprint.pprint(vars(args))

    return 0

if __name__ == '__main__':
    exit(main())