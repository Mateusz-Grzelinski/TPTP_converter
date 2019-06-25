from antlr4 import FileStream

from src.antlr_generated.tptpParser import tptpParser
from src.antlr_generated.tptpListener import tptpListener
from src.antlr_generated.tptpLexer import tptpLexer
from src.antlr_generated.tptpParser import tptpParser, ParseTreeWalker, FileStream, CommonTokenStream


class DimacsConverter(tptpListener):
    def __init__(self, file_name):
        self.variables = {}
        self.number_of_variables = 0
        self.number_of_clauses = 0
        self.delimiter = 0
        self.file_name = file_name
        with open(self.file_name, "w+") as f:
            f.write('p\n')

    def exitTptp_file(self, ctx: tptpParser.Tptp_fileContext):
        print(f'converted file saved to {self.file_name}')

    @property
    def new_variable(self):
        self.number_of_variables += 1
        return self.number_of_variables

    def exitCnf_annotated(self, ctx: tptpParser.Cnf_annotatedContext):
        self.number_of_clauses += 1
        # print('0')
        with open(self.file_name, 'a') as f:
            f.write('0\n')
        with open(self.file_name, 'r+') as m:
            s = m.readlines()
        s[0] = "p cnf " + str(self.number_of_variables) + " " + str(self.number_of_clauses) + "\n"
        with open(self.file_name, 'w') as out_file:
            out_file.writelines(s)

    def enterCnf_literal(self, ctx: tptpParser.Cnf_literalContext):
        if ctx.getToken(tptpParser.Not, 0):
            # print('-', end='')
            with open(self.file_name, 'a') as f:
                f.write('-')

    def enterFof_atomic_formula(self, ctx: tptpParser.Fof_atomic_formulaContext):
        atomic_formula = ctx.getText()
        variable_name = self.variables.get(atomic_formula)
        if variable_name is None:
            variable_name = self.new_variable
            self.variables[atomic_formula] = variable_name
        # print(variable_name, end=' ')
        with open(self.file_name, 'a') as f:
            f.write(str(variable_name) + ' ')



