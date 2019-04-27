# ast - abstract syntax tree
from typing import List
from rply.token import BaseBox


class CNFAnnotated(BaseBox):
    def __init__(self, name, formula_role, cnf_formula, annotations=None):
        self.name = name
        self.formula_role = formula_role
        self.cnf_formula = cnf_formula
        self.annotations = annotations


class Include(BaseBox):
    def __init__(self, file_name, formula_selection: List = None):
        self.file_name = file_name
        self.formula_selection = formula_selection  # don't know what it does


class FormulaRole(BaseBox):
    pass


class CNFFormula(BaseBox):
    pass


if __name__ == '__main__':
    print('axiom')
