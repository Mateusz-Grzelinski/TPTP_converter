percentage_sign = r'[%]'
double_quote = r'["]'
do_char = r'([\40-\41\43-\133\135-\176]|[\\]["\\])'
single_quote = r'[\']'
# %---Space and visible characters upto ~, except ' and \
sq_char = r'([\40-\46\50-\133\135-\176]|[\\][\'\\])'
sign = r'[+-]'
dot = r'[.]'
coma = r','
exponent = r'[Ee]'
slash = r'[/]'
zero_numeric = r'[0]'
non_zero_numeric = r'[1-9]'
numeric = r'[0-9]'
lower_alpha = r'[a-z]'
upper_alpha = r'[A-Z]'
alpha_numeric = '(' + lower_alpha + '|' + upper_alpha + '|' + numeric + '|[_])'
dollar = r'[$]'
vline = r'[|]'
star = r'[*]'
plus = r'[+]'
arrow = r'[>]'
less_sign = r'[<]'
open_parens = r'\('
close_parens = r'\)'
printable_char = r'.'

not_star_slash = r'([^*]*[*][*]*[^/*])*[^*]*'
comment_block = '[/][*]' + not_star_slash + '[*][*]*[/]'
comment_line = '[%]' + printable_char + '*'
comment = comment_line + '|' + comment_block

TPTP_include = r'include'

tpi_annotated = r'tpi'
thf_annotated = r'thf'
tff_annotated = r'tff'
tcf_annotated = r'tcf'
fof_annotated = r'fof'
cnf_annotated = r'cnf'

defined_type = r'$oType|$o|$iType|$i|$tType|$real|$rat|$int'
assignment = r':='
gentzen_arrow = r'-->'
unary_connective = r'~'
assoc_connective = vline + '|&'
nonassoc_connective = r'<=>|=>|<=|<~>|~' + vline + '|~&'
fof_quantifier = r'[!?]'
subtype_sign = r'<<'
th1_unary_connective = r'!!|??|@@+|@@-|@='
thf_unary_connective = unary_connective + '|' + th1_unary_connective
th0_quantifier = r'^|@+|@-'
th1_quantifier = r'!>|?*'
infix_inequality = r'!='
infix_equality = r'='
defined_proposition = r'\$true|\$false'

formula_role = r'axiom|hypothesis|definition|assumption|lemma|theorem|corollary|conjecture|negated_conjecture|plain|type|fi_domain|fi_functors|fi_predicates|unknown'

unsigned_exp_integer = numeric + numeric + '*'
signed_exp_integer = sign + unsigned_exp_integer
exp_integer = '(' + signed_exp_integer + '|' + unsigned_exp_integer + ')'
dot_decimal = dot + numeric + numeric + '*'
positive_decimal = non_zero_numeric + numeric + '*'
decimal = '(' + zero_numeric + '|' + positive_decimal + ')'
decimal_fraction = decimal + dot_decimal
decimal_exponent = '(' + decimal + '|' + decimal_fraction + ')' + exponent + exp_integer
unsigned_integer = decimal
signed_integer = sign + unsigned_integer
integer = '(' + signed_integer + '|' + unsigned_integer + ')'
unsigned_rational = decimal + slash + positive_decimal
signed_rational = sign + unsigned_rational
rational = '(' + signed_rational + '|' + unsigned_rational + ')'
unsigned_real = '(' + decimal_fraction + '|' + decimal_exponent + ')'
signed_real = sign + unsigned_real
real = '(' + signed_real + '|' + unsigned_real + ')'

lower_word = lower_alpha + alpha_numeric + '*'
upper_word = upper_alpha + alpha_numeric + '*'
dollar_dollar_word = dollar + dollar + lower_word
dollar_word = dollar + lower_word

single_quoted = single_quote + sq_char + sq_char + '*' + single_quote

number = integer + '|' + rational + '|' + real
atomic_word = lower_word + '|' + single_quoted
name = atomic_word + '|' + integer

atomic_word = lower_word + '|' + single_quoted

variable = upper_word
