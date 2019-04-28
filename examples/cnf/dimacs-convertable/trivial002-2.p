% cnf with operators (in one clousure)
cnf(pseudo_divide, axiom,
    ( X = 1
    | Y = 2
    | X != 0
    | divide(Y, X)
    )).

