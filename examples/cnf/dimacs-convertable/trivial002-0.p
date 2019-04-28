% cnf with operators (note X=1)
cnf(data_set, axiom,
    ( X = 1
    | Y = 2
    )).

cnf(pseudo_divide, axiom,
    ( X != 0
    | divide(Y, X)
    )).

