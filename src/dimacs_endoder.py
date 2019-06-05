from dataclasses import dataclass

from src.ast import TPTPFile


@dataclass
class DIMACSEncoder:
    """
    Example dimacs file:
    c comment starts with c
    c problem starts with 'p cnf nvar nclauses', where:
    c nvar is total number of variables
    c nclauses is total number os clauses
    c clause ends with 0
    c variable is represented by number, minus means variable is negated
    c (x v ~x) ^ (y) would be:
    p cnf 3 2
    1 -1 0
    2 0
    """
    output_path: str = './out.dimacs'

    def encode(self, tptp: TPTPFile):
        pass
