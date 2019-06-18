grammar dimacs;

Non_zero_integer : [123456789] [0123456789]*;

Not : '-';
Delimiter : '0';

WS : [ \t\r\n] -> skip;
Line_comment : 'c' [ \t] ~[\r\n]* -> skip;

dimacs_file : problem  EOF;
problem : 'p'  'cnf'  Non_zero_integer Non_zero_integer clauses;
clauses : disjunction+;
disjunction : (Not? Non_zero_integer)+ Delimiter ;
