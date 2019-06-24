grammar tptp;

fragment Do_char : [\u0020-\u0021\u0023-\u005B\u005D-\u007E] | '\\'["\\];
fragment Sq_char : [\u0020-\u0026\u0028-\u005B\u005D-\u007E] | '\\'['\\];
fragment Sign : [+-];
fragment Exponent : [Ee];
fragment Non_zero_numeric : [1-9];
fragment Numeric : [0-9];
fragment Lower_alpha : [a-z];
fragment Upper_alpha : [A-Z];
fragment Alpha_numeric : Lower_alpha | Upper_alpha | Numeric | '_';

Or: '|';
And: '&';
Iff : '<=>';
Impl : '=>';
If: '<=';
Niff: '<~>';
Nor: '~|';
Nand: '~&';
Not: '~';
ForallComb: '!!';
TyForall: '!>';
Infix_inequality : '!=';
Infix_equality : '=';
Forall: '!';
ExistsComb: '??';
TyExists: '?*';
Exists: '?';
Lambda: '^';
ChoiceComb: '@@+';
Choice: '@+';
DescriptionComb: '@@-';
Description: '@-';
EqComb: '@=';
App: '@';
Assignment: ':=';
Arrow: '>';
Star: '*';
Plus: '+';
Subtype_sign: '<<';
Gentzen_arrow            : '-->';

Real : Signed_real | Unsigned_real;
Signed_real : Sign Unsigned_real;
Unsigned_real : Decimal_fraction|Decimal_exponent;
Rational: Signed_rational | Unsigned_rational;
Signed_rational: Sign Unsigned_rational;
Unsigned_rational: Decimal '/' Positive_decimal;
Integer : Signed_integer | Unsigned_integer;
Signed_integer: Sign Unsigned_integer;
Unsigned_integer: Decimal;
Decimal : '0' | Positive_decimal;
Positive_decimal : Non_zero_numeric Numeric*;
Decimal_exponent : (Decimal|Decimal_fraction) Exponent Exp_integer;
Decimal_fraction : Decimal Dot_decimal;
Dot_decimal : '.' Numeric Numeric*;
Exp_integer : Signed_exp_integer|Unsigned_exp_integer;
Signed_exp_integer : Sign Unsigned_exp_integer;
Unsigned_exp_integer : Numeric Numeric*;

Dollar_word : '$' Lower_word;
Dollar_dollar_word : '$$' Lower_word;
Upper_word : Upper_alpha Alpha_numeric*;
Lower_word : Lower_alpha Alpha_numeric*;

Single_quoted : '\'' Sq_char+ '\'';
Distinct_object : '"' Do_char+ '"';

WS : [ \r\t\n]+ -> skip ;
Line_comment : '%' ~[\r\n]* -> skip;
Block_comment : '/*' .*? '*/' -> skip;


//%----Files. Empty file is OK.
tptp_file               : tptp_input* EOF;
tptp_input              : annotated_formula | include;

//%----Formula records
annotated_formula       : thf_annotated | tfx_annotated | tff_annotated
                        | tcf_annotated | fof_annotated | cnf_annotated
                        | tpi_annotated;
tpi_annotated           : 'tpi(' name ',' formula_role ',' tpi_formula annotations? ').';
tpi_formula             : fof_formula;
thf_annotated           : 'thf(' name ',' formula_role ',' thf_formula annotations? ').';
tfx_annotated           : 'tfx(' name ',' formula_role ',' tfx_formula annotations? ').';
tff_annotated           : 'tff(' name ',' formula_role ',' tff_formula annotations? ').';
tcf_annotated           : 'tcf(' name ',' formula_role ',' tcf_formula annotations? ').';
fof_annotated           : 'fof(' name ',' formula_role ',' fof_formula annotations? ').';
cnf_annotated           : 'cnf(' name ',' formula_role ',' cnf_formula annotations? ').';
annotations             : ',' source optional_info?;

formula_role            : Lower_word; // #RES no restrictions

//%----THF formulae.
thf_formula : thf_logic_formula | thf_sequent;
thf_logic_formula       : thf_binary_formula | thf_unitary_formula
                        | thf_type_formula | thf_subtype;
thf_binary_formula      : thf_binary_pair | thf_binary_tuple
                        | thf_binary_type;

thf_binary_pair         : thf_unitary_formula thf_pair_connective thf_unitary_formula;
thf_binary_tuple        : thf_or_formula | thf_and_formula
                        | thf_apply_formula;
thf_or_formula          : thf_unitary_formula Or thf_unitary_formula
                        | thf_or_formula Or thf_unitary_formula;
thf_and_formula         : thf_unitary_formula And thf_unitary_formula
                        | thf_and_formula And thf_unitary_formula;
thf_apply_formula       : thf_unitary_formula App thf_unitary_formula
                        | thf_apply_formula App thf_unitary_formula;

thf_unitary_formula     : thf_quantified_formula | thf_unary_formula
                        | thf_atom | thf_conditional | thf_let
                        | thf_tuple | '(' thf_logic_formula ')';

thf_quantified_formula  : thf_quantification thf_unitary_formula;
thf_quantification      : thf_quantifier '[' thf_variable_list ']' ':';
thf_variable_list       : thf_variable (',' thf_variable)*;
thf_variable            : thf_typed_variable | variable;
thf_typed_variable      : variable ':' thf_top_level_type;
thf_unary_formula       : thf_unary_connective '(' thf_logic_formula ')';
thf_atom                : thf_function | variable | defined_term
                        | thf_conn_term;
thf_function            : atom | functor '(' thf_arguments ')'
                        | defined_functor '(' thf_arguments ')'
                        | system_functor '(' thf_arguments ')';
thf_conn_term           : thf_pair_connective | assoc_connective
                        | thf_unary_connective;
thf_conditional         : '$ite(' thf_logic_formula ',' thf_logic_formula ',' thf_logic_formula ')';
thf_let                 : '$let(' thf_unitary_formula ',' thf_formula ')';
thf_arguments           : thf_formula_list;
thf_type_formula        : thf_typeable_formula ':' thf_top_level_type;
thf_typeable_formula    : thf_atom | '(' thf_logic_formula ')';
thf_subtype             : thf_atom Subtype_sign thf_atom;
thf_top_level_type      : thf_unitary_type | thf_mapping_type | thf_apply_type;
thf_unitary_type        : thf_unitary_formula;
thf_apply_type          : thf_apply_formula;
thf_binary_type         : thf_mapping_type | thf_xprod_type
                        | thf_union_type;
thf_mapping_type        : thf_unitary_type Arrow thf_unitary_type
                        | thf_unitary_type Arrow thf_mapping_type;
thf_xprod_type          : thf_unitary_type Star thf_unitary_type
                        | thf_xprod_type Star thf_unitary_type;
thf_union_type          : thf_unitary_type Plus thf_unitary_type
                        | thf_union_type Plus thf_unitary_type;
thf_sequent             : thf_tuple Gentzen_arrow thf_tuple
                        | '(' thf_sequent ')';
thf_tuple               : '[]' | '[' thf_formula_list ']'
                        | '{}' | '{' thf_formula_list '}';
thf_formula_list        : thf_logic_formula (',' thf_logic_formula)*;
tfx_formula              : tfx_logic_formula | thf_sequent;
tfx_logic_formula        : thf_logic_formula;
tff_formula             : tff_logic_formula | tff_typed_atom
                        | tff_sequent;
tff_logic_formula       : tff_binary_formula | tff_unitary_formula
                        | tff_subtype;
tff_binary_formula      : tff_binary_nonassoc | tff_binary_assoc;
tff_binary_nonassoc     : tff_unitary_formula binary_connective tff_unitary_formula;
tff_binary_assoc        : tff_or_formula | tff_and_formula;
tff_or_formula          : tff_unitary_formula Or tff_unitary_formula
                        | tff_or_formula Or tff_unitary_formula;
tff_and_formula         : tff_unitary_formula And tff_unitary_formula
                        | tff_and_formula And tff_unitary_formula;
tff_unitary_formula     : tff_quantified_formula | tff_unary_formula
                        | tff_atomic_formula | tff_conditional
                        | tff_let | '(' tff_logic_formula ')';
tff_quantified_formula  : fof_quantifier '[' tff_variable_list ']' ':' tff_unitary_formula;
tff_variable_list       : tff_variable (',' tff_variable)*;
tff_variable            : tff_typed_variable | variable;
tff_typed_variable      : variable ':' tff_atomic_type;
tff_unary_formula       : unary_connective tff_unitary_formula
                        | fof_infix_unary;
tff_atomic_formula      : fof_atomic_formula;

tff_conditional         : '$ite_f(' tff_logic_formula ',' tff_logic_formula ',' tff_logic_formula ')';
tff_let                 : '$let_tf(' tff_let_term_defns ',' tff_formula ')'
                        | '$let_ff(' tff_let_formula_defns ',' tff_formula ')';
tff_let_term_defns      : tff_let_term_defn | '[' tff_let_term_list ']';
tff_let_term_list       : tff_let_term_defn (',' tff_let_term_defn)*;
tff_let_term_defn       : Forall '[' tff_variable_list ']' ':' tff_let_term_defn
                        | tff_let_term_binding;
tff_let_term_binding    : fof_plain_term Infix_equality fof_term
                        | '(' tff_let_term_binding ')';
tff_let_formula_defns   : tff_let_formula_defn | '[' tff_let_formula_list ']';
tff_let_formula_list    : tff_let_formula_defn (',' tff_let_formula_defn)*;
tff_let_formula_defn    : Forall '[' tff_variable_list ']' ':' tff_let_formula_defn
                        | tff_let_formula_binding;
tff_let_formula_binding : fof_plain_atomic_formula Iff tff_unitary_formula
                        | '(' tff_let_formula_binding ')';

tff_sequent             : tff_formula_tuple Gentzen_arrow tff_formula_tuple
                        | '(' tff_sequent ')';
tff_formula_tuple       : '[]' | '[' tff_formula_tuple_list ']';
tff_formula_tuple_list  : tff_logic_formula (',' tff_logic_formula)*;
tff_typed_atom          : untyped_atom ':' tff_top_level_type
                        | '(' tff_typed_atom ')';
tff_subtype             : untyped_atom Subtype_sign atom;

tff_top_level_type      : tff_atomic_type | tff_mapping_type
                        | tf1_quantified_type | '(' tff_top_level_type ')';
tf1_quantified_type     : '!>' '[' tff_variable_list ']' ':' tff_monotype;
tff_monotype            : tff_atomic_type | '(' tff_mapping_type ')';
tff_unitary_type        : tff_atomic_type | '(' tff_xprod_type ')';
tff_atomic_type         : type_constant | defined_type
                        | type_functor '(' tff_type_arguments ')' | variable;
tff_type_arguments      : tff_atomic_type (',' tff_atomic_type)*;
tff_mapping_type        : tff_unitary_type Arrow tff_atomic_type;
tff_xprod_type          : tff_unitary_type Star tff_atomic_type
                        | tff_xprod_type Star tff_atomic_type;
tcf_formula             : tcf_logic_formula | tff_typed_atom;
tcf_logic_formula       : tcf_quantified_formula | cnf_formula;
tcf_quantified_formula  : Forall '[' tff_variable_list ']' ':' cnf_formula;

fof_formula             : fof_logic_formula | fof_sequent;
fof_logic_formula       : fof_binary_formula | fof_unitary_formula;
fof_binary_formula      : fof_binary_nonassoc | fof_binary_assoc;
fof_binary_nonassoc     : fof_unitary_formula binary_connective fof_unitary_formula;
fof_binary_assoc        : fof_or_formula | fof_and_formula;
fof_or_formula          : fof_unitary_formula Or fof_unitary_formula
                        | fof_or_formula Or fof_unitary_formula;
fof_and_formula         : fof_unitary_formula And fof_unitary_formula
                        | fof_and_formula And fof_unitary_formula;
fof_unitary_formula     : fof_quantified_formula | fof_unary_formula
                        | fof_atomic_formula | '(' fof_logic_formula ')';
fof_quantified_formula  : fof_quantifier '[' fof_variable_list ']' ':' fof_unitary_formula;
fof_variable_list       : variable (',' variable)*;
fof_unary_formula       : unary_connective fof_unitary_formula | fof_infix_unary;

fof_infix_unary             : fof_term Infix_inequality fof_term;
fof_atomic_formula          : fof_plain_atomic_formula
                            | fof_defined_atomic_formula
                            | fof_system_atomic_formula;
fof_plain_atomic_formula    : fof_plain_term;
fof_defined_atomic_formula  : fof_defined_plain_formula | fof_defined_infix_formula;
fof_defined_plain_formula   : fof_defined_term;
fof_defined_infix_formula   : fof_term defined_infix_pred fof_term;
fof_system_atomic_formula   : fof_system_term;

fof_plain_term           : constant
                        | functor '(' fof_arguments ')';
fof_defined_term        : defined_term | fof_defined_atomic_term;
fof_defined_atomic_term : fof_defined_plain_term;
fof_defined_plain_term  : defined_constant
                        | defined_functor '(' fof_arguments ')';
fof_system_term         : system_constant
                        | system_functor '(' fof_arguments ')';

fof_arguments           : fof_term (',' fof_term)*;
fof_term                : fof_function_term | variable
                        | tff_conditional_term | tff_let_term
                        | tff_tuple_term;
fof_function_term       : fof_plain_term | fof_defined_term
                        | fof_system_term;

tff_conditional_term    : '$ite_t(' tff_logic_formula ',' fof_term ',' fof_term ')';
tff_let_term            : '$let_ft(' tff_let_formula_defns ',' fof_term ')'
                        | '$let_tt(' tff_let_term_defns ',' fof_term ')';
tff_tuple_term          : '{}' | '{' fof_arguments '}';

fof_sequent             : fof_formula_tuple Gentzen_arrow fof_formula_tuple
                        | '(' fof_sequent ')';
fof_formula_tuple       : '[]' | '[' fof_formula_tuple_list ']';
fof_formula_tuple_list  : fof_logic_formula (',' fof_logic_formula)*;

cnf_formula             : cnf_disjunction | '(' cnf_disjunction ')';
cnf_disjunction         : cnf_literal | cnf_disjunction Or cnf_literal;
cnf_literal             : fof_atomic_formula | Not fof_atomic_formula
                        | fof_infix_unary;

thf_quantifier          : fof_quantifier | th0_quantifier
                        | th1_quantifier;
th0_quantifier          : Lambda | Choice | Description;
th1_quantifier          : TyForall | TyExists;
thf_pair_connective     : Infix_equality | Infix_inequality
                        | binary_connective | Assignment ;
thf_unary_connective    : unary_connective | th1_unary_connective;
th1_unary_connective    : ForallComb | ExistsComb | ChoiceComb | DescriptionComb | EqComb;

tff_pair_connective     : binary_connective | Assignment;

fof_quantifier: Forall | Exists;
binary_connective: Iff | Impl | If | Niff | Nor | Nand;
assoc_connective : Or | And;
unary_connective : Not;

type_constant           : type_functor;
type_functor            : atomic_word;
defined_type            : Dollar_word;
system_type             : atomic_system_word;

atom                    : untyped_atom | defined_constant;
untyped_atom            : constant | system_constant;

defined_proposition     : Dollar_word;
defined_predicate       : Dollar_word;

defined_infix_pred      : Infix_equality | Assignment;

constant                : functor;
functor                 : atomic_word;

system_constant         : system_functor;
system_functor          : atomic_system_word;

defined_constant        : defined_functor;
defined_functor         : atomic_defined_word;

defined_term            : number | Distinct_object;
variable                : Upper_word;

source                  : dag_source | internal_source
                        | external_source
                        | Lower_word
                        | '[' sources ']';
sources                 : source ( ',' source )*;
dag_source              : name | inference_record;

inference_record        : 'inference(' inference_rule ',' useful_info ',' inference_parents ')';
inference_rule          : atomic_word;

inference_parents       : '[]' | '[' parent_list ']';
parent_list             : parent_info ( ',' parent_info )*;
parent_info             : source parent_details?;
parent_details          : ':' general_list;
internal_source         : 'introduced(' intro_type optional_info? ')';
intro_type              : Lower_word;
external_source          : file_source | theory | creator_source;
file_source             : 'file(' file_name file_info? ')';
file_info               : ',' name;
theory                  : 'theory(' theory_name optional_info? ')';
theory_name             : Lower_word;
creator_source          : 'creator(' creator_name optional_info? ')';
creator_name            : atomic_word;

optional_info           : ',' useful_info;
useful_info             : '[]' | '[' info_items ']' | general_list;
info_items              : info_item ( ',' info_item )*;
info_item               : formula_item | inference_item
                        | general_function;
formula_item            : description_item | iquote_item;
description_item        : 'description(' atomic_word ')';
iquote_item             : 'iquote(' atomic_word ')';

inference_item          : inference_status | assumptions_record
                        | new_symbol_record | refutation;
inference_status        : 'status(' status_value ')' | inference_info;
status_value            : Lower_word;
inference_info          : inference_rule '(' atomic_word ',' general_list ')';
assumptions_record      : 'assumptions(' '[' name_list ']' ')';
refutation              : 'refutation(' file_source ')';
new_symbol_record       : 'new_symbols(' atomic_word ',' '[' new_symbol_list ']' ')';
new_symbol_list         : principal_symbol ( ',' principal_symbol )*;
principal_symbol        : functor | variable;

include                 : 'include(' file_name formula_selection? ').';
formula_selection       : ',' '[' name_list ']';
name_list               : name (',' name)*;

general_term            : general_data | general_data ':' general_term
                        | general_list;
general_data            : atomic_word | general_function
                        | variable | number | Distinct_object
                        | formula_data;
general_function        : atomic_word '(' general_terms ')';
formula_data            : '$thf(' thf_formula ')' | '$tff(' tff_formula ')'
                        | '$fof(' fof_formula ')' | '$cnf(' cnf_formula ')'
                        | '$fot(' fof_term ')';
general_list            : '[]' | '[' general_terms ']';
general_terms           : general_term (',' general_term)*;

name : atomic_word | Integer;
atomic_word : Lower_word | Single_quoted;
atomic_defined_word : Dollar_word;
atomic_system_word : Dollar_dollar_word;
number : Integer | Rational | Real;
file_name : Single_quoted;

