# Generated from /home/mat/studia-repos/kompilatory/TPTP_converter/src/syntax/dimacs.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("#\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\6\4\25\n\4\r\4\16\4\26\3\5\5\5\32")
        buf.write("\n\5\3\5\6\5\35\n\5\r\5\16\5\36\3\5\3\5\3\5\2\2\6\2\4")
        buf.write("\6\b\2\2\2!\2\n\3\2\2\2\4\r\3\2\2\2\6\24\3\2\2\2\b\34")
        buf.write("\3\2\2\2\n\13\5\4\3\2\13\f\7\2\2\3\f\3\3\2\2\2\r\16\7")
        buf.write("\3\2\2\16\17\7\4\2\2\17\20\7\5\2\2\20\21\7\5\2\2\21\22")
        buf.write("\5\6\4\2\22\5\3\2\2\2\23\25\5\b\5\2\24\23\3\2\2\2\25\26")
        buf.write("\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27\7\3\2\2\2\30\32")
        buf.write("\7\6\2\2\31\30\3\2\2\2\31\32\3\2\2\2\32\33\3\2\2\2\33")
        buf.write("\35\7\5\2\2\34\31\3\2\2\2\35\36\3\2\2\2\36\34\3\2\2\2")
        buf.write("\36\37\3\2\2\2\37 \3\2\2\2 !\7\7\2\2!\t\3\2\2\2\5\26\31")
        buf.write("\36")
        return buf.getvalue()


class dimacsParser ( Parser ):

    grammarFileName = "dimacs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'p'", "'cnf'", "<INVALID>", "'-'", "'0'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Non_zero_integer", 
                      "Not", "Delimiter", "WS", "Line_comment" ]

    RULE_dimacs_file = 0
    RULE_problem = 1
    RULE_clauses = 2
    RULE_disjunction = 3

    ruleNames =  [ "dimacs_file", "problem", "clauses", "disjunction" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Non_zero_integer=3
    Not=4
    Delimiter=5
    WS=6
    Line_comment=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Dimacs_fileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def problem(self):
            return self.getTypedRuleContext(dimacsParser.ProblemContext,0)


        def EOF(self):
            return self.getToken(dimacsParser.EOF, 0)

        def getRuleIndex(self):
            return dimacsParser.RULE_dimacs_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimacs_file" ):
                listener.enterDimacs_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimacs_file" ):
                listener.exitDimacs_file(self)




    def dimacs_file(self):

        localctx = dimacsParser.Dimacs_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_dimacs_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.problem()
            self.state = 9
            self.match(dimacsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProblemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Non_zero_integer(self, i:int=None):
            if i is None:
                return self.getTokens(dimacsParser.Non_zero_integer)
            else:
                return self.getToken(dimacsParser.Non_zero_integer, i)

        def clauses(self):
            return self.getTypedRuleContext(dimacsParser.ClausesContext,0)


        def getRuleIndex(self):
            return dimacsParser.RULE_problem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProblem" ):
                listener.enterProblem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProblem" ):
                listener.exitProblem(self)




    def problem(self):

        localctx = dimacsParser.ProblemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_problem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(dimacsParser.T__0)
            self.state = 12
            self.match(dimacsParser.T__1)
            self.state = 13
            self.match(dimacsParser.Non_zero_integer)
            self.state = 14
            self.match(dimacsParser.Non_zero_integer)
            self.state = 15
            self.clauses()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClausesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def disjunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dimacsParser.DisjunctionContext)
            else:
                return self.getTypedRuleContext(dimacsParser.DisjunctionContext,i)


        def getRuleIndex(self):
            return dimacsParser.RULE_clauses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClauses" ):
                listener.enterClauses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClauses" ):
                listener.exitClauses(self)




    def clauses(self):

        localctx = dimacsParser.ClausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_clauses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 17
                self.disjunction()
                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==dimacsParser.Non_zero_integer or _la==dimacsParser.Not):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisjunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Delimiter(self):
            return self.getToken(dimacsParser.Delimiter, 0)

        def Non_zero_integer(self, i:int=None):
            if i is None:
                return self.getTokens(dimacsParser.Non_zero_integer)
            else:
                return self.getToken(dimacsParser.Non_zero_integer, i)

        def Not(self, i:int=None):
            if i is None:
                return self.getTokens(dimacsParser.Not)
            else:
                return self.getToken(dimacsParser.Not, i)

        def getRuleIndex(self):
            return dimacsParser.RULE_disjunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisjunction" ):
                listener.enterDisjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisjunction" ):
                listener.exitDisjunction(self)




    def disjunction(self):

        localctx = dimacsParser.DisjunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_disjunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==dimacsParser.Not:
                    self.state = 22
                    self.match(dimacsParser.Not)


                self.state = 25
                self.match(dimacsParser.Non_zero_integer)
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==dimacsParser.Non_zero_integer or _la==dimacsParser.Not):
                    break

            self.state = 30
            self.match(dimacsParser.Delimiter)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





