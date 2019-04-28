% cnf with operators (note X=0)
cnf(data_set, axiom,
    ( X = 0
    | Y = 2
    )).

cnf(pseudo_divide, axiom,
    ( X != 0
    | divide(Y, X)
    )).

