from rply import LexerGenerator
import regexes


def get_TPTP_lexer():
    lg = LexerGenerator()

    lg.add('comment', regexes.comment)
    lg.add('TPTP_include', r'include')

    lg.add('tpi_annotated', r'tpi')
    lg.add('thf_annotated', r'thf')
    lg.add('tff_annotated', r'tff')
    lg.add('tcf_annotated', r'tcf')
    lg.add('fof_annotated', r'fof')
    lg.add('cnf_annotated', r'cnf')

    lg.add('formula_role', r'axiom|hypothesis|definition|assumption|lemma|theorem|'
                           r'corollary|conjecture|negated_conjecture|plain|type|'
                           r'fi_domain|fi_functors|fi_predicates|unknown')

    lg.add('atomic_word',r'\'([\40-\46\50-\133\135-\176]|[\\][\'\\])([\40-\46\50-\133\135-\176]|[\\][\'\\])*\'|(\b[a-z]\w*\b)')
    lg.add('unsigned_intiger',r'[^+-]\d+')

    lg.add('variable', r'\b[A-Z]\w*\b')
    lg.add('functor', r'(\b[a-z]\w*\b)|(\'\b\w+\b\')')

    lg.add('defined_proposition',r'\$true|\$false')
    lg.add('unary_connective', r'~')
    lg.add('operator', r'=')
    lg.add('assigment',r':=')
    lg.add('gentzen_arrow',r'-->')

    # lg.add('', r'')
    lg.add('name', r'\w+')
    lg.add('open_parens', r'\(')
    lg.add('close_parens', r'\)')
    lg.add('coma', r',')
    lg.add('vline', r'\|')
    #---------------------------------------
    lg.add('vline', r'[|]')
    lg.add('star', r'[*]')
    lg.add('plus', r'[+]')
    lg.add('arrow', r'[>]')
    lg.add('less_sign',r'[<]')
    #---------------------------------------------------
    #lg.add('real', r'([+-]|)')#(<signed_real>|<unsigned_real>)
    #lg.add('signed_real', r'[+-]')#<sign><unsigned_real>
    #lg.add('unsigned_real', r'((([0]|([1-9][0-9]*))[.][0-9][0-9]*)|())')#(<decimal_fraction>|<decimal_exponent>)
    #lg.add('rational', r'(([+-](([0]|([1-9][0-9]*))[/]([1-9][0-9]*)))|(([0]|([1-9][0-9]*))[/]([1-9][0-9]*)))')#(<signed_rational>|<unsigned_rational>)
    #lg.add('signed_rational',r'[+-](([0]|([1-9][0-9]*))[/]([1-9][0-9]*))')#<sign><unsigned_rational>
    #lg.add('unsigned_rational', r'([0]|([1-9][0-9]*))[/]([1-9][0-9]*)')#<decimal><slash><positive_decimal>
    #lg.add('integer', r'([+-]([0]|([1-9][0-9]*)))|([0]|([1-9][0-9]*))')#(<signed_integer>|<unsigned_integer>)
    #lg.add('signed_integer', r'[+-]([0]|([1-9][0-9]*))')#<sign><unsigned_integer>
    #lg.add('unsigned_integer', r'[0]|([1-9][0-9]*)')#<decimal>
    #lg.add('decimal',r'[0]|([1-9][0-9]*)')#(<zero_numeric>|<positive_decimal>)
    #lg.add('positive_decimal', r'[1-9][0-9]*')#<non_zero_numeric><numeric>*
    #lg.add('decimal_exponent', r'(([0]|([1-9][0-9]*))|(([0]|([1-9][0-9]*))[.][0-9][0-9]*))[Ee]([0-9][0-9]*|[+-][0-9][0-9]*)')#(<decimal>|<decimal_fraction>)<exponent><exp_integer>
    #lg.add('decimal_fraction', r'([0]|([1-9][0-9]*))[.][0-9][0-9]*')#<decimal><dot_decimal>
    #lg.add('dot_decimal', r'[.][0-9][0-9]*')#<dot><numeric><numeric>*
    #lg.add('exp_integer',r'[0-9][0-9]*|[+-][0-9][0-9]*')#(<signed_exp_integer>|<unsigned_exp_integer>)
    #lg.add('signed_exp_integer', r'[+-][0-9][0-9]*')#<sign><unsigned_exp_integer>
    #lg.add('unsigned_exp_integer', r'[0-9][0-9]*')#<numeric><numeric>*

    #------------------------------------------------------------------


    lg.add('percentage_sign',r'[%]')
    lg.add('double_quote',r'["]')
    lg.add('do_char',r'([\40-\41\43-\133\135-\176]|[\\]["\\])')
    lg.add('single_quote',r'[\']')
    lg.add('sign',r'[+-]')
    lg.add('dot', r'[.]')
    lg.add('exponent',r'[Ee]')
    lg.add('slash',r'[/]')
    lg.add('zero_numeric',r'[0]')
    lg.add('non_zero_numeric',r'[1-9]')
    lg.add('numeric',r'[0-9]')
    lg.add('lower_alpha',r'[a-z]')
    lg.add('upper_alpha',r'[A-Z]')
    lg.add('alpha_numeric',r'([a-z]|[A-Z]|[0-9]|[_])')
    lg.add('dollar',r'[$]')
    lg.add('printable_char',r'.')
    lg.add('viewable_char',r'[.\n]')

    #lg.add('th1_quantifier')

    lg.ignore(r'\s+')

    return lg.build()


if __name__ == '__main__':
    from pprint import pprint

    lexer = get_TPTP_lexer()

    with open('examples/cnf/TPTP-library/SYN000-1.p', 'r') as source:
        tokens = lexer.lex(source.read())
        pprint(list(tokens))
