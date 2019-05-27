from typing import List, Union

from rply import ParserGenerator, Token
from src import ast
import logging

from src.logger import get_logger

logger = get_logger(__name__)
logger.setLevel(logging.DEBUG)


pg = ParserGenerator(
    # import all valid tokens
    [
        'TPTP_include',
        'cnf_annotated',

        'formula_role',

        'atomic_word',

        'unary_connective',

        'open_parens',
        'close_parens',
        'coma',
        'vline',

        'dot'
    ]
)


@pg.error
def error_handler(token: Token):
    raise ValueError(f'Ran into a {token.gettokentype()} at position {token.getsourcepos()} expected')


@pg.production('FILE : FORMULA FILE')
@pg.production('FILE : FORMULA')
@pg.production('FILE : INCLUDE FILE')
@pg.production('FILE : INCLUDE')
def ending(p):
    return p


# do not support tpi, thf, tff, tcf - show error message
# fof support is optional
# todo problem: atomic_word should be name, but the token is atomic_word, as this is more precise match in regex
@pg.production(
    'FORMULA : cnf_annotated open_parens atomic_word coma formula_role coma CNF_FORMULA ANNOTATIONS close_parens dot')
@pg.production('FORMULA : cnf_annotated open_parens atomic_word coma formula_role coma CNF_FORMULA close_parens dot')
def formula(p: List[Union[Token, ast.Literal]]):
    logger.debug(f'formula {p}')
    return ast.CNFFormula(name=p[2].getstr(),  # string
                          formula_role=p[4].getstr(),  # string
                          variables=p[6]  # ast.Literal
                          )


@pg.production('CNF_FORMULA : DISJUNCTION')
@pg.production('CNF_FORMULA : open_parens DISJUNCTION close_parens')
def cnf_formula(p: List[Union[Token, List[ast.Literal]]]) -> List[ast.Literal]:
    logger.debug(f'cnf form: {p}')
    if len(p) == 1:
        return p[0]
    else:
        return p[1]


@pg.production('DISJUNCTION : LITERAL')
@pg.production('DISJUNCTION : DISJUNCTION vline LITERAL')
def disjuction(p: List[Union[Token, ast.Literal, List[ast.Literal]]]) -> List[ast.Literal]:
    logger.debug(f'disjunction: {p}')
    if len(p) == 1:
        return [p.pop()]
    else:
        # DISJUNCTION on right side of production is accumulating all literals as list
        p[0].append(p.pop())
        return p[0]


# todo this shoud be <fof_atomic_formula> | ~ <fof_atomic_formula> | <fof_infix_unary>
# defined_proposition, defined_functor, defined_predicate is also literal. Should we treat ios specially in model?
@pg.production('LITERAL : atomic_word')
@pg.production('LITERAL : unary_connective atomic_word')
def literal(p: List[Token]) -> ast.Literal:
    logger.debug(f'litral: {p}')
    return ast.Literal(name=p.pop().getstr(), negated=bool(len(p) == 2))


# todo implement
@pg.production('ANNOTATIONS : coma ')
def annotations(p: List[Token]):
    pass


# todo implement. This probably requires adding new parser state.
@pg.production('INCLUDE : TPTP_include')
def include(p: List[Token]):
    logger.debug(f'include: {p}')
    return p


def get_TPTP_parser():
    return pg.build()


if __name__ == '__main__':
    from src.tptp_lexer import get_TPTP_lexer
    from pprint import pprint

    lexer = get_TPTP_lexer()
    parser = get_TPTP_parser()
    tokens = lexer.lex(
        '''
% this is comment
cnf(predicates, axiom,
    ( p0
    | ~ q0
    )).
        ''')
    r = parser.parse(tokens)
    # pprint(list(tokens))
    # pprint('result:', r)
    pprint(r)
