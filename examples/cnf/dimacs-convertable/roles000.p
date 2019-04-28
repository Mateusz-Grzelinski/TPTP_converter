% axiom like roles are treated the same is cnf

cnf(facts1, axiom, ( p0 )).
cnf(facts2, hypothesis, ( p1 )).
cnf(facts3, definition, ( p2 )).
cnf(facts4, assumption, ( p3 )).
cnf(facts5, lemma, ( p4 )).
cnf(facts6, theorem, ( p5 )).
cnf(facts6, corollary, ( p6 )).

% other acceptable roles
cnf(facts6, plain, ( p7 )).

% TODO: check this roles:
cnf(facts6, type, ( p8 )).
cnf(facts6, unknown, ( p9 )).


% negated_conjectures shold occur only once, but more is acceptable (?)
cnf(prove, negated_conjectures, ( prove0 )).
% should conjectures be present in cnf?
cnf(prove, conjectures, ( prove1 )).
