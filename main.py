import argparse
from pprint import pprint

from src.parser import get_TPTP_parser
from src.tptp_lexer import get_TPTP_lexer

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TPTP to dimacs converter')
    parser.add_argument('TPTP_files',
                        nargs='+',
                        help='TPTP file to convet')
    parser.add_argument('-o', '--output-dir', default='dimacs',
                        help='where to save dimacs file')

    args = parser.parse_args()

    pprint(args)

    lexer = get_TPTP_lexer()
    parser = get_TPTP_parser()

    for TPTP_file in args.TPTP_files:
        with open(TPTP_file, 'r') as source:
            tokens = lexer.lex(source.read())
            pprint(list(tokens))

            parser.parse(tokens)

