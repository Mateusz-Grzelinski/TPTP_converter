from typing import List

from rply import ParserGenerator, Token
from src import ast

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


@pg.production(f'FILE : FORMULA FILE')
@pg.production(f'FILE : FORMULA')
@pg.production(f'FILE : INCLUDE FILE')
@pg.production(f'FILE : INCLUDE')
def ending(p):
    return p


# todo problem: atomic_word should be name, but the token is atomic_word, as this is more precise match in regex
@pg.production('FORMULA : cnf_annotated open_parens atomic_word coma formula_role coma CNF_FORMULA ANNOTATIONS close_parens dot')
@pg.production('FORMULA : cnf_annotated open_parens atomic_word coma formula_role coma CNF_FORMULA close_parens dot')
def formula(p: List[Token]):
    print('formula', p)
    return ast.CNFFormula(name=p[2].getstr(),
                          formula_role=p[4].getstr(),
                          variables=p[6],
                          )


@pg.production('CNF_FORMULA : DISJUNCTION')
@pg.production('CNF_FORMULA : open_parens DISJUNCTION close_parens')
def cnf_formula(p):
    print('cnf form: ', p)
    if len(p) == 1:
        return p[0]
    else:
        return p[1]


@pg.production('DISJUNCTION : LITERAL')
@pg.production('DISJUNCTION : DISJUNCTION vline LITERAL')
def disjuction(p):
    print('disjunction: ', p)
    if len(p) == 1:
        return [p.pop()]
    else:
        p[0].append(p.pop())
        return p[0]


# todo this shoud be <fof_atomic_formula>
@pg.production('LITERAL : atomic_word')
@pg.production('LITERAL : unary_connective atomic_word')
def literal(p):
    print('litral: ', p)
    return ast.Literal(name=p.pop().getstr(), negated=bool(len(p) == 2))


# todo
@pg.production('ANNOTATIONS : coma ')
def annotations(p):
    pass


@pg.production('INCLUDE : TPTP_include')
def include(p):
    print('include: ', p)
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
