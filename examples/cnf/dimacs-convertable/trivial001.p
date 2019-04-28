% handling multiple formulas
cnf(facts1, axiom,
    ( p0
    | p0(a)
    | p0(b)
    )).

cnf(facts2, axiom,
    ( p0
    | ~p0(X)
    )).

