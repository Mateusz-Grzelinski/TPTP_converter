# Generated from dimacs.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .dimacsParser import dimacsParser
else:
    from dimacsParser import dimacsParser

# This class defines a complete listener for a parse tree produced by dimacsParser.
class dimacsListener(ParseTreeListener):

    # Enter a parse tree produced by dimacsParser#dimacs_file.
    def enterDimacs_file(self, ctx:dimacsParser.Dimacs_fileContext):
        pass

    # Exit a parse tree produced by dimacsParser#dimacs_file.
    def exitDimacs_file(self, ctx:dimacsParser.Dimacs_fileContext):
        pass


    # Enter a parse tree produced by dimacsParser#problem.
    def enterProblem(self, ctx:dimacsParser.ProblemContext):
        pass

    # Exit a parse tree produced by dimacsParser#problem.
    def exitProblem(self, ctx:dimacsParser.ProblemContext):
        pass


    # Enter a parse tree produced by dimacsParser#clauses.
    def enterClauses(self, ctx:dimacsParser.ClausesContext):
        pass

    # Exit a parse tree produced by dimacsParser#clauses.
    def exitClauses(self, ctx:dimacsParser.ClausesContext):
        pass


    # Enter a parse tree produced by dimacsParser#disjunction.
    def enterDisjunction(self, ctx:dimacsParser.DisjunctionContext):
        pass

    # Exit a parse tree produced by dimacsParser#disjunction.
    def exitDisjunction(self, ctx:dimacsParser.DisjunctionContext):
        pass
