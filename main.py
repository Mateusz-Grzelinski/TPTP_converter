import argparse
import sys

from src.antlr_generated.tptpLexer import tptpLexer
from src.antlr_generated.tptpParser import tptpParser, ParseTreeWalker, FileStream, CommonTokenStream
from src.dimacs_converter import DimacsConverter


def parse_args():
    parser = argparse.ArgumentParser(description='TPTP to dimacs converter')
    parser.add_argument('-f', '--file',
                        help='TPTP file to convet',
                        required=True)
    parser.add_argument('-o', '--output',
                        help='where to save dimacs file')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    if args.output is not None:
        sys.stdout = open(args.output, 'w')

    input_stream = FileStream(args.file)
    lexer = tptpLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = tptpParser(stream)
    tree = parser.tptp_file()

    printer = DimacsConverter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
