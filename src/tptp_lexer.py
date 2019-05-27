from rply import LexerGenerator
from src import regexes


def get_TPTP_lexer():
    lg = LexerGenerator()

    lg.add('comment', regexes.comment)
    lg.add('TPTP_include', regexes.TPTP_include)

    lg.add('tpi_annotated', regexes.tpi_annotated)
    lg.add('thf_annotated', regexes.thf_annotated)
    lg.add('tff_annotated', regexes.tff_annotated)
    lg.add('tcf_annotated', regexes.tcf_annotated)
    lg.add('cnf_annotated', regexes.cnf_annotated)
    lg.add('fof_annotated', regexes.fof_annotated)

    lg.add('formula_role', regexes.formula_role)
    lg.add('definied_type', regexes.defined_type)

    lg.add('atomic_word',regexes.atomic_word)
    lg.add('number',regexes.number)
    # lg.add('integer',regexes.integer)
    # lg.add('rational',regexes.rational)
    # lg.add('real',regexes.real)

    lg.add('variable', regexes.variable)


    lg.add('defined_proposition',regexes.defined_proposition)
    lg.add('unary_connective', regexes.unary_connective)
    lg.add('infix_equality', regexes.infix_equality)
    lg.add('assigment',regexes.assignment)
    lg.add('gentzen_arrow',regexes.gentzen_arrow)
    lg.add('infix_inequality',regexes.infix_inequality)
    lg.add('nonassoc_connective',regexes.nonassoc_connective)
    lg.add('subtype_sign',regexes.subtype_sign)
    lg.add('fof_quantifier',regexes.fof_quantifier)

    lg.add('name', regexes.name)
    lg.add('open_parens', regexes.open_parens)
    lg.add('close_parens', regexes.close_parens)
    lg.add('coma', regexes.coma)
    lg.add('vline', regexes.vline)
    lg.add('star', regexes.star)
    lg.add('plus', regexes.plus)
    lg.add('arrow', regexes.arrow)
    lg.add('less_sign',regexes.less_sign)

    lg.add('percentage_sign',regexes.percentage_sign)
    lg.add('double_quote',regexes.double_quote)
    lg.add('single_quote',regexes.single_quote)
    lg.add('sign',regexes.sign)
    lg.add('dot', regexes.dot)
    lg.add('exponent',regexes.exponent)
    lg.add('slash',regexes.slash)

    lg.add('dollar',regexes.dollar)

    lg.add('do_char',regexes.do_char)

    lg.ignore(r'\s+')

    return lg.build()


if __name__ == '__main__':
    from pprint import pprint

    lexer = get_TPTP_lexer()

    with open('examples/cnf/TPTP-library/SYN000-1.p', 'r') as source:
        tokens = lexer.lex(source.read())
        pprint(list(tokens))
