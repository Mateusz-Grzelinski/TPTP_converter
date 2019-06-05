# ast - abstract syntax tree
from dataclasses import dataclass, field
from typing import List


@dataclass
class Literal:
    """atomic word or functor
    literals with dolar are defined literals
    """
    name: str
    negated: bool

    # todo handle variables (starts with uppercase) and predicates (ex. tata(Tomek))
    def is_variable(self):
        return self.name[0].isupper()

    # todo: is it needed?
    def is_predefined(self):
        return self.name in {'$less', '$lesseq', '...'}


@dataclass
class Formula:
    name: str
    formula_role: str
    annotations: List[str] = field(default_factory=list)


@dataclass
class CNFFormula(Formula):
    """Represents single row in cnf formula.
    variables are connected with 'or' statement
    """
    variables: List[Literal] = field(default_factory=list)


@dataclass
class Include:
    file_name: str
    formula_selection: List[str] = field(default_factory=list)


@dataclass
class TPTPFile:
    """Empty file is valid TPTP file"""
    formula: List[Formula] = field(default_factory=list)
    includes: List[Include] = field(default_factory=list)
