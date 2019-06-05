from src.syntax.DimacsConverterVisitor import DimacsConverterListener
from antlr4 import FileStream, CommonTokenStream

from src.syntax.antlr_generated.dimacsLexer import dimacsLexer
from src.syntax.antlr_generated.dimacsParser import dimacsParser
from src.syntax.antlr_generated.tptpParser import tptpParser, ParseTreeWalker, ParseTreeVisitor, ParseTreeListener
from src.syntax.antlr_generated.tptpLexer import tptpLexer


def tptp():
    input_stream = FileStream('../../examples/cnf/TPTP-library/PUZ031-1.p')
    lexer = tptpLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = tptpParser(stream)
    tree = parser.tptp_file()
    print(tree)

    # converter = DimacsConverter()
    # result = converter.visit(tree)
    # print(result)
    print('listener ')
    printer = DimacsConverterListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


def dimacs():
    input_stream = FileStream(
        '../../examples/cnf/dimacs-convertable/roles000.dimacs'
    )
    lexer = dimacsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = dimacsParser(stream)
    tree = parser.dimacs_file()
    print(tree.getText())


if __name__ == '__main__':
    dimacs()
