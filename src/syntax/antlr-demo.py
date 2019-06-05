from src.syntax.DimacsConverterVisitor import DimacsConverterVisitor, DimacsConverterListener
from antlr4 import FileStream, CommonTokenStream
from src.syntax.antlr_generated.tptpParser import tptpParser, ParseTreeWalker, ParseTreeVisitor, ParseTreeListener
from src.syntax.antlr_generated.tptpLexer import tptpLexer

if __name__ == '__main__':
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
