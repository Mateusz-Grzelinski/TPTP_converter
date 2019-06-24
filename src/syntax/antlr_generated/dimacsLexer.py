# Generated from dimacs.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("\60\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\7\4\32\n\4")
        buf.write("\f\4\16\4\35\13\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\7\b*\n\b\f\b\16\b-\13\b\3\b\3\b\2\2\t\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\3\2\7\3\2\63;\3\2\62;\5\2\13\f")
        buf.write("\17\17\"\"\4\2\13\13\"\"\4\2\f\f\17\17\2\61\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\3\21\3\2\2\2\5\23\3\2\2\2\7\27")
        buf.write("\3\2\2\2\t\36\3\2\2\2\13 \3\2\2\2\r\"\3\2\2\2\17&\3\2")
        buf.write("\2\2\21\22\7r\2\2\22\4\3\2\2\2\23\24\7e\2\2\24\25\7p\2")
        buf.write("\2\25\26\7h\2\2\26\6\3\2\2\2\27\33\t\2\2\2\30\32\t\3\2")
        buf.write("\2\31\30\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2")
        buf.write("\2\2\34\b\3\2\2\2\35\33\3\2\2\2\36\37\7/\2\2\37\n\3\2")
        buf.write("\2\2 !\7\62\2\2!\f\3\2\2\2\"#\t\4\2\2#$\3\2\2\2$%\b\7")
        buf.write("\2\2%\16\3\2\2\2&\'\7e\2\2\'+\t\5\2\2(*\n\6\2\2)(\3\2")
        buf.write("\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,.\3\2\2\2-+\3\2\2\2")
        buf.write("./\b\b\2\2/\20\3\2\2\2\5\2\33+\3\b\2\2")
        return buf.getvalue()


class dimacsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    Non_zero_integer = 3
    Not = 4
    Delimiter = 5
    WS = 6
    Line_comment = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'p'", "'cnf'", "'-'", "'0'" ]

    symbolicNames = [ "<INVALID>",
            "Non_zero_integer", "Not", "Delimiter", "WS", "Line_comment" ]

    ruleNames = [ "T__0", "T__1", "Non_zero_integer", "Not", "Delimiter",
                  "WS", "Line_comment" ]

    grammarFileName = "dimacs.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
