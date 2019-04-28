from rply import LexerGenerator


def get_TPTP_lexer():
    lg = LexerGenerator()

    lg.add('comment', r'%.*')
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

    lg.add('literal', r'~')
    lg.add('operator', r'=')
    # lg.add('', r'')
    lg.add('name', r'\w+')
    lg.add('open_parens', r'\(')
    lg.add('close_parens', r'\)')
    lg.add('coma', r',')
    lg.add('dot', r'\.')
    lg.add('vline', r'\|')

    lg.ignore(r'\s+')

    return lg.build()


if __name__ == '__main__':
    from pprint import pprint

    lexer = get_TPTP_lexer()
    with open('examples/cnf/trivial000-0.p', 'r') as source:
        tokens = lexer.lex(source.read())

        pprint(list(tokens))
