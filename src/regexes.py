import re

#comment_line = r'%.*'
#comment_block = r'[\/][*]([^*]*[*][*]*[^\/*])*[^*]*[*][*]*[\/]'
#comment = re.compile('('+comment_line+'|'+comment_block+')')

#
# #%----Character classes
# percentage_sign = r'[%]'
# double_quote = r'["]'
# do_char = r'([\40-\41\43-\133\135-\176]|[\\]["\\])'
# single_quote = r'[\']'
# # %---Space and visible characters upto ~, except ' and \
# sq_char = r'([\40-\46\50-\133\135-\176]|[\\][\'\\])'
# sign = r'[+-]'
# dot = r'[.]'
# exponent = r'[Ee]'
# slash = r'[/]'
# zero_numeric = r'[0]'
# non_zero_numeric = r'[1-9]'
# numeric = r'[0-9]'
# lower_alpha = r'[a-z]'
# upper_alpha = r'[A-Z]'
# alpha_numeric = re.compile('('+lower_alpha+'|'+upper_alpha+'|'+numeric+'|[_])')
# dollar = r'[$]'
# printable_char = r'.'
# #%----<printable_char> is any printable ASCII character, codes 32 (space) to 126
# #%----(tilde). <printable_char> does not include tabs, newlines, bells, etc. The
# #%----use of . does not not exclude tab, so this is a bit loose.
# viewable_char = r'[.\n]'
#
# #%----Numbers. Signs are made part of the same token here.
# unsigned_exp_integer = re.compile(numeric+numeric+'*')
# signed_exp_integer = re.compile(sign+unsigned_exp_integer)
# exp_integer = re.compile('('+signed_exp_integer+'|'+unsigned_exp_integer+')')
# dot_decimal = re.compile(dot+numeric+numeric+'*')
# decimal_fraction = re.compile(decimal+dot_decimal)
# decimal_exponent = re.compile('('+decimal+'|'+decimal_fraction+')'+exponent+exp_integer)
# positive_decimal = re.compile(non_zero_numeric+numeric+'*')
# decimal = re.compile('('+zero_numeric+'|'+positive_decimal+')')
# unsigned_integer = re.compile(decimal)
# signed_integer = re.compile(sign+unsigned_integer)
# integer = re.compile('('+signed_integer+'|'+unsigned_integer+')')
# unsigned_rational = re.compile(decimal+slash+positive_decimal)
# signed_rational = re.compile(sign+unsigned_rational)
# rational = re.compile('('+signed_rational+'|'+unsigned_rational+')')
# unsigned_real = re.compile('('+decimal_fraction+'|'+decimal_exponent+')')
# signed_real = re.compile(sign+unsigned_real)
# real = re.compile('('+signed_real+'|'+unsigned_real+')')
#
#
# #%----Tokens used in syntax, and cannot be character classes
# vline                = r'[|]'
# star                 = r'[*]'
# plus                 = r'[+]'
# arrow                = r'[>]'
# less_sign            = r'[<]'
#
#
#
# lower_word            = re.compile(lower_alpha+alpha_numeric+'*')
# upper_word            = re.compile(upper_alpha+alpha_numeric+'*')
# dollar_dollar_word    = re.compile(dollar+dollar+lower_word)
# dollar_word           = re.compile(dollar+lower_word)
#
#
# distinct_object       = re.compile(double_quote+do_char+'*'+double_quote)
#
# single_quoted         = re.compile(single_quote+sq_char+sq_char+'*'+single_quote)
#
#
#
# not_star_slash       = r'([^*]*[*][*]*[^/*])*[^*]*'
# comment_block        = re.compile('[/][*]'+not_star_slash+'[*][*]*[/]')
# comment_line         = re.compile('[%]'+printable_char+'*')
# comment              = re.compile(comment_line+'|'+comment_block)
#
#
# null                 = r'[]'
# file_name            = re.compile(single_quoted)
#
#
# number               = re.compile(integer+'|'+rational+'|'+real)
# atomic_system_word   = re.compile(dollar_dollar_word)
# atomic_defined_word  = re.compile(dollar_word)
# atomic_word          = re.compile(lower_word+'|'+single_quoted)
# name                 = re.compile(atomic_word+'|'+integer)
#
# #%----Non-logical data
#
# general_terms        = re.compile(general_term+'|'+general_term+','+general_terms)
# general_list         = re.compile('[]|['+general_terms+']')
# formula_data         = re.compile( '$thf('+thf_formula+') | $tff('+tff_formula+') |'+
#                            '$fof('+fof_formula+') | $cnf('+cnf_formula+') |'+
#                            '$fot('+fof_term+')')
# general_data         = re.compile( 'bind('+variable+','+formula_data+')')
# general_function     = re.compile(atomic_word+'('+general_terms+')')
# general_data         = re.compile(atomic_word+'|'+general_function+'|'+
#                            variable+'|'+number+'|'+distinct_object++'|'+
#                            formula_data)
# general_term         = re.compile( general_data+'|'+general_data+':'+general_term+'|'+
#                            general_list)
#
# #%----Include directives
#
# name_list            = re.compile(name+'|'+name+','+name_list)
# formula_selection    = re.compile(',['+name_list+'] | '+null)
# include              = re.compile('include('+file_name+formula_selection+').')
#
# #%----Principal symbols are predicates, functions, variables
# principal_symbol   = re.compile(functor+'|'+variable)
#
#
# new_symbol_list      = re.compile(principal_symbol+'|'+
#                            principal_symbol+','+new_symbol_list)
# new_symbol_record    = re.compile('new_symbols('+atomic_word+',['+new_symbol_list+'])')
#
#
# refutation           = re.compile('refutation('+file_source+')')
#
#
# assumptions_record   = re.compile( 'assumptions(['+name_list+'])')
# inference_info       = re.compile( inference_rule+'('+atomic_word+','+general_list+')')
#
# status_value         = r' suc | unp | sap | esa | sat | fsa | thm | eqv | tac |wec | eth | tau | wtc | wth | cax | sca | tca | wca |cup | csp | ecs | csa | cth | ceq | unc | wcc | ect |fun | uns | wuc | wct | scc | uca | noc '
#
#
# inference_status     = re.compile( 'status('+status_value+') | '+inference_info)
# inference_item       = re.compile(inference_status+'|'+assumptions_record+'|'+
#                            new_symbol_record+'|'+refutation)
#
#
# iquote_item          = re.compile( 'iquote('+atomic_word+')')
# description_item     = re.compile( 'description('+atomic_word+')')
# formula_item         = re.compile( description_item+'|'+iquote_item)
#
#
# info_item            = re.compile( formula_item+'|'+inference_item+'|'+
#                            general_function)
# info_items           = re.compile( info_item+'|'+info_item+','+info_items)
# useful_info          = re.compile( '[] | ['+info_items+']')
# useful_info          = re.compile( general_list)
# optional_info        = re.compile( ','+useful_info+'|'+null)
#
#
# creator_name         = re.compile( atomic_word)
# creator_source       = re.compile( 'creator('+creator_name+optional_info+')')
# theory_name          = r' equality | ac'
# theory               = re.compile( 'theory('+theory_name+optional_info+')')
# file_info            = re.compile( ','+name+'|'+null)
# file_source          = re.compile( 'file('+file_name+file_info+')')
# external_source      = re.compile( file_source+'|'+theory+'|'+creator_source)
#
#
# internal_source      = re.compile( 'introduced('+intro_type+optional_info+')')
# parent_details       = re.compile( ':'+general_list+'|'+null)
# parent_info          = re.compile( source+parent_details+')')
# parent_list          = re.compile( parent_info+'|'+parent_info+','+parent_list)
# inference_parents    = re.compile( '[] | ['+parent_list+']')
# inference_rule       = re.compile( atomic_word)
# inference_record     = re.compile( 'inference('+inference_rule+','+useful_info+','+
#                            inference_parents+')')
# dag_source           = re.compile( name+'|'+inference_record)
# sources              = re.compile( source+'|'+source+','+sources)
# source               = re.compile( dag_source+'|'+internal_source+'|'+
#                            external_source+' | unknown | ['+sources+']')
# source               = re.compile( general_term)
#
#
#
# variable             = re.compile(upper_word)
# defined_term         = re.compile(number+'|'+distinct_object)
# defined_functor      = r' $uminus | $sum | $difference | $product |$quotient | $quotient_e | $quotient_t | $quotient_f |$remainder_e | $remainder_t | $remainder_f |$floor | $ceiling | $truncate | $round |$to_int | $to_rat | $to_real'
# defined_functor      = re.compile(atomic_defined_word)
# defined_constant     = re.compile(defined_functor)
# system_functor       = re.compile(atomic_system_word)
# system_constant      = re.compile(system_functor)
# functor              = re.compile(atomic_word)
# constant             = re.compile(functor)
# infix_inequality     = r'!='
# infix_equality       = r'='
# system_predicate     = re.compile( atomic_system_word)
# system_proposition   = re.compile( system_predicate)
# defined_infix_pred   = re.compile(infix_equality)
#
#
# defined_predicate    = r' $distinct |$less | $lesseq | $greater | $greatereq |$is_int | $is_rat |$box_P | $box_i | $box_int | $box |$dia_P | $dia_i | $dia_int | $dia'
# defined_predicate    = re.compile( atomic_defined_word)
# defined_proposition   = r' $true | $false'
# defined_proposition  = re.compile( defined_predicate)
# predicate            = re.compile( atomic_word)
# proposition          = re.compile( predicate)
# untyped_atom         = re.compile(constant+'|'+system_constant)
# atom                 = re.compile(untyped_atom+'|'+defined_constant)
#
#
# system_type          = re.compile( atomic_system_word)
# defined_type         = r' $oType | $o | $iType | $i | $tType |$real | $rat | $int'
# defined_type         = re.compile(atomic_defined_word)
# type_functor         = re.compile(atomic_word)
# type_constant        = re.compile(type_functor)
#
# assignment           = r':='
# gentzen_arrow        = r'-->'
# unary_connective     = r'~'
# assoc_connective     = re.compile(vline+' | &')
# nonassoc_connective  = r'<=> | => | <= | <~> | ~<vline> | ~&'
# fof_quantifier       = r' ! | ?'
# subtype_sign         = r'<<'
# th1_unary_connective = r' !! | ?? | @@+ | @@- | @='
# thf_unary_connective = re.compile( unary_connective+'|'+th1_unary_connective)
# th0_quantifier       = r' ^ | @+ | @-'
# th1_quantifier       = r' !> | ?*'
# thf_quantifier       = re.compile(fof_quantifier+'|'+th0_quantifier+'|'+
#                            th1_quantifier)
#
#
# literal              = re.compile(fof_atomic_formula+' | ~'+fof_atomic_formula+'|'+
#                            fof_infix_unary)
# disjunction          = re.compile( literal+'|'+disjunction + vline + literal)
# cnf_formula          = re.compile( disjunction + '| ('+disjunction+')')
#
# fof_formula_tuple_list = re.compile( fof_logic_formula+'|'+
#                            fof_logic_formula+','+fof_formula_tuple_list)
# fof_formula_tuple    = re.compile(' {} | {'+fof_formula_tuple_list+'}')
# fof_sequent          = re.compile(fof_formula_tuple + gentzen_arrow+
#                            fof_formula_tuple+'|('+fof_sequent+')')
#
#
# fof_function_term    = re.compile(fof_plain_term+'|'+fof_defined_term+'|'+
#                            fof_system_term)
# fof_term             = re.compile(fof_function_term+'|'+variable)
# fof_arguments        = re.compile(fof_term+'|'+fof_term+','+fof_arguments)
# fof_system_term      = re.compile(system_constant+'|'+system_functor+'('+fof_arguments+')')
# fof_defined_plain_term   = re.compile(defined_constant+'|'+
#                            defined_functor+'('+fof_arguments+')')
# fof_defined_atomic_term  = re.compile(fof_defined_plain_term)
# fof_defined_term     = re.compile(defined_term+'|'+fof_defined_atomic_term)
# fof_plain_term       = re.compile(constant+'|'+functor+'('+fof_arguments+')')
#
#
# fof_system_atomic_formula = re.compile(fof_system_term)
# fof_defined_infix_formula = re.compile(fof_term + defined_infix_pred + fof_term)
# fof_defined_plain_formula = re.compile( defined_proposition+'|'+
#                            defined_predicate+'('+fof_arguments+')')
# fof_defined_plain_formula = re.compile(fof_defined_plain_term)
# fof_defined_atomic_formula = re.compile(fof_defined_plain_formula+'|'+
#                            fof_defined_infix_formula)
# fof_plain_atomic_formula = re.compile( proposition+'|'+predicate+'('+fof_arguments+')')
# fof_plain_atomic_formula = re.compile(fof_plain_term)
# fof_atomic_formula   = re.compile(fof_plain_atomic_formula+'|'+
#                            fof_defined_atomic_formula+'|'+
#                            fof_system_atomic_formula)
# fof_variable_list    = re.compile(variable+'|'+variable+','+fof_variable_list)
# fof_quantified_formula = re.compile(fof_quantifier+ '['+fof_variable_list+'] :'+
#                            fof_unit_formula)
# fof_unitary_formula  = re.compile(fof_quantified_formula+'|'+fof_atomic_formula+'|'+
#                            '('+fof_logic_formula+')')
# fof_unit_formula     = re.compile( fof_unitary_formula+'|'+fof_unary_formula)
# fof_infix_unary      = re.compile( fof_term + infix_inequality + fof_term)
# fof_unary_formula    = re.compile( unary_connective + fof_unit_formula+'|'+
#                            fof_infix_unary)
# fof_and_formula      = re.compile( fof_unit_formula+'&'+fof_unit_formula+'|'+
#                            fof_and_formula+'&'+fof_unit_formula)
# fof_or_formula       = re.compile( fof_unit_formula + vline + fof_unit_formula+'|'+
#                            fof_or_formula + vline + fof_unit_formula)
# fof_binary_assoc     = re.compile( fof_or_formula+'|'+fof_and_formula)
# fof_binary_nonassoc  = re.compile( fof_unit_formula + nonassoc_connective +
#                            fof_unit_formula)
# fof_binary_formula   = re.compile( fof_binary_nonassoc+'|'+fof_binary_assoc)
# fof_logic_formula    = re.compile( fof_binary_formula+'|'+fof_unary_formula+'|'+
#                            fof_unitary_formula)
# fof_formula          = re.compile( fof_logic_formula+'|'+fof_sequent)
# tcf_quantified_formula = re.compile( '! ['+tff_variable_list+'] :'+cnf_formula)
# tcf_logic_formula    = re.compile( tcf_quantified_formula+'|'+cnf_formula)
# tcf_formula          = re.compile( tcf_logic_formula+'|'+tff_atom_typing)
#
#
# tfx_sequent          = re.compile( tfx_tuple + gentzen_arrow + tfx_tuple+'|'+
#                            '('+tfx_sequent+')')
# tff_subtype          = re.compile( untyped_atom + subtype_sign + atom)
# tff_type_list        = re.compile( tff_top_level_type+'|'+
#                            tff_top_level_type+','+tff_type_list)
# tfx_tuple_type       = re.compile( '['+tff_type_list+']')
# tff_xprod_type       = re.compile( tff_unitary_type + star + tff_atomic_type+'|'+
#                            tff_xprod_type + star + tff_atomic_type)
# tff_mapping_type     = re.compile( tff_unitary_type + arrow + tff_atomic_type)
# tff_type_arguments   = re.compile( tff_atomic_type+'|'+
#                            tff_atomic_type+','+tff_type_arguments)
# tff_atomic_type      = re.compile( type_constant+'|'+defined_type+'|'+
#                            type_functor+'('+tff_type_arguments+') |'+variable+'|'+
#                            tfx_tuple_type)
# tff_unitary_type     = re.compile( tff_atomic_type+' | ('+tff_xprod_type+')')
# tff_monotype         = re.compile( tff_atomic_type+' | ('+tff_mapping_type+')')
# tf1_quantified_type  = re.compile( '!> ['+tff_variable_list+'] :'+tff_monotype)
# tff_top_level_type   = re.compile( tff_atomic_type+'|'+tff_mapping_type+'|'+
#                            tf1_quantified_type+' | ('+tff_top_level_type+')')
# tff_atom_typing      = re.compile( untyped_atom+':'+tff_top_level_type+'|'+
#                            '('+tff_atom_typing+')')
#
#
# tff_arguments        = re.compile( tff_term+'|'+tff_term+','+tff_arguments)
# tfx_tuple            = re.compile(' [] | ['+tff_arguments+']')
# tff_unitary_term     = re.compile( tff_atomic_formula+'|'+defined_term+'|'+
#                            tfx_tuple+'|'+variable+' | ('+tff_logic_formula+')')
# tff_term             = re.compile( tff_logic_formula+'|'+defined_term+'|'+tfx_tuple)
# tfx_let_defn_list    = re.compile( tfx_let_defn+'|'+tfx_let_defn+','+tfx_let_defn_list)
# tfx_let_LHS          = re.compile( tff_plain_atomic+'|'+tfx_tuple)
# tfx_let_defn         = re.compile( tfx_let_LHS + assignment + tff_term)
# tfx_let_defns        = re.compile( tfx_let_defn+' | ['+tfx_let_defn_list+']')
# tff_atom_typing_list = re.compile( tff_atom_typing+'|'+
#                            tff_atom_typing+','+tff_atom_typing_list)
# tfx_let_types        = re.compile( tff_atom_typing+' | ['+tff_atom_typing_list+']')
# tfx_let              = re.compile( '$let('+tfx_let_types+','+tfx_let_defns+','+tff_term+')')
# tfx_conditional      = re.compile( '$ite('+tff_logic_formula+','+tff_term+','+tff_term+')')
# tff_system_atomic    = re.compile( system_proposition+'|'+
#                            system_predicate+'('+tff_arguments+')')
# tff_system_atomic    = re.compile( system_constant+'|'+
#                            system_functor+'('+tff_arguments+')')
# tff_defined_infix    = re.compile( tff_unitary_term + defined_infix_pred+
#                            tff_unitary_term)
#
#
# tff_defined_plain    = re.compile( defined_proposition+'|'+
#                            defined_predicate+'('+tff_arguments+') |'+
#                            tfx_conditional+'|'+tfx_let)
# tff_defined_plain    = re.compile( defined_constant+'|'+
#                            defined_functor+'('+tff_arguments+') |'+
#                            tfx_conditional+'|'+tfx_let)
# tff_defined_atomic   = re.compile( tff_defined_plain)
# tff_plain_atomic     = re.compile( proposition+'|'+predicate+'('+tff_arguments+')')
# tff_plain_atomic     = re.compile( constant+'|'+functor+'('+tff_arguments+')')
# tff_atomic_formula   = re.compile( tff_plain_atomic+'|'+tff_defined_atomic+'|'+
#                            tff_system_atomic)
# tff_infix_unary      = re.compile( tff_unitary_term + infix_inequality+
#                            tff_unitary_term)
# tff_prefix_unary     = re.compile( unary_connective + tff_preunit_formula)
# tff_unary_formula    = re.compile( tff_prefix_unary+'|'+tff_infix_unary)
# tff_typed_variable   = re.compile( variable+':'+tff_atomic_type)
# tff_variable         = re.compile( tff_typed_variable+'|'+variable)
# tff_variable_list    = re.compile( tff_variable+'|'+tff_variable+','+tff_variable_list)
# tff_quantified_formula = re.compile( fof_quantifier+'['+tff_variable_list+'] :'+
#                            tff_unit_formula)
# tfx_unitary_formula  = re.compile( variable)
# tff_unitary_formula  = re.compile( tff_quantified_formula+'|'+tff_atomic_formula+'|'+
#                            tfx_unitary_formula+' | ('+tff_logic_formula+')')
# tff_preunit_formula  = re.compile( tff_unitary_formula+'|'+tff_prefix_unary)
# tff_unit_formula     = re.compile( tff_unitary_formula+'|'+tff_unary_formula+'|'+
#                            tff_defined_infix)
# tff_and_formula      = re.compile( tff_unit_formula+'&'+tff_unit_formula+'|'+
#                            tff_and_formula+'&'+tff_unit_formula)
# tff_or_formula       = re.compile( tff_unit_formula + vline + tff_unit_formula+'|'+
#                            tff_or_formula + vline + tff_unit_formula)
# tff_binary_assoc     = re.compile( tff_or_formula+'|'+tff_and_formula)
# tff_binary_nonassoc  = re.compile( tff_unit_formula + nonassoc_connective+
#                            tff_unit_formula)
# tff_binary_formula   = re.compile( tff_binary_nonassoc+'|'+tff_binary_assoc)
# tff_logic_formula    = re.compile( tff_unitary_formula+'|'+tff_unary_formula+'|'+
#                            tff_binary_formula+'|'+tff_defined_infix)
# tff_formula          = re.compile( tff_logic_formula+'|'+tff_atom_typing+'|'+
#                            tff_subtype+'|'+tfx_sequent)
#
#
# logic_defn_value     = r' $rigid | $flexible |$constant | $varying | $cumulative | $decreasing |$local | $global |$modal_system_K | $modal_system_T | $modal_system_D |$modal_system_S4 | $modal_system_S5 |$modal_axiom_K | $modal_axiom_T | $modal_axiom_B |$modal_axiom_D | $modal_axiom_4 | $modal_axiom_5'
# logic_defn_value     = re.compile( defined_constant)
# logic_defn_RHS       = re.compile( logic_defn_value+'|'+thf_unitary_formula)
# logic_defn_LHS       = r' $constants | $quantification | $consequence |$modalities'
# logic_defn_LHS       = re.compile( logic_defn_value+'|'+thf_top_level_type+'|'+name)
# logic_defn_rule      = re.compile( logic_defn_LHS + assignment + logic_defn_RHS)
# thf_sequent          = re.compile( thf_tuple + gentzen_arrow + thf_tuple+'|'+
#                            '('+thf_sequent+')')
# thf_subtype          = re.compile( untyped_atom + subtype_sign + atom)
# thf_union_type       = re.compile( thf_unitary_type + plus + thf_unitary_type+'|'+
#                            thf_union_type + plus + thf_unitary_type)
# thf_xprod_type       = re.compile( thf_unitary_type + star + thf_unitary_type+'|'+
#                            thf_xprod_type + star + thf_unitary_type)
# thf_mapping_type     = re.compile( thf_unitary_type + arrow + thf_unitary_type+'|'+
#                            thf_unitary_type + arrow + thf_mapping_type)
# thf_binary_type      = re.compile( thf_mapping_type+'|'+thf_xprod_type+'|'+
#                            thf_union_type)
# thf_apply_type       = re.compile( thf_apply_formula)
# th1_quantified_type  = re.compile( '!> ['+thf_variable_list+'] : '+thf_unitary_type)
# thf_atomic_type      = re.compile( type_constant+'|'+defined_type+'|'+variable+'|'+
#                            thf_mapping_type+' | ('+thf_atomic_type+')' )
# thf_unitary_type     = re.compile( thf_atomic_type+'|'+th1_quantified_type)
# thf_unitary_type     = re.compile( thf_unitary_formula)
# thf_top_level_type   = re.compile( thf_unitary_type+'|'+thf_mapping_type+'|'+
#                            thf_apply_type)
# thf_atom_typing      = re.compile( untyped_atom+':'+thf_top_level_type+'|'+
#                            '('+thf_atom_typing+')')
# thf_arguments        = re.compile( thf_formula_list)
# thf_conn_term        = re.compile( nonassoc_connective+'|'+assoc_connective+'|'+
#                            infix_equality+'|'+thf_unary_connective)
# thf_formula_list     = re.compile( thf_logic_formula+'|'+
#                            thf_logic_formula+','+thf_formula_list)
# thf_tuple            = re.compile(' [] | ['+thf_formula_list+']')
# thf_unitary_term     = re.compile( thf_atomic_formula+'|'+variable+'|'+
#                            '('+thf_logic_formula+')')
# thf_let_defn_list    = re.compile( thf_let_defn+'|'+thf_let_defn+','+thf_let_defn_list)
# thf_let_defn         = re.compile( thf_logic_formula + assignment + thf_logic_formula)
# thf_let_defns        = re.compile( thf_let_defn+' | ['+thf_let_defn_list+']')
# thf_atom_typing_list = re.compile( thf_atom_typing+'|'+
#                            thf_atom_typing+','+thf_atom_typing_list)
# thf_let_types        = re.compile( thf_atom_typing+' | ['+thf_atom_typing_list+']')
# thf_let              = re.compile( '$let('+thf_let_types+','+thf_let_defns+','+thf_formula+')')
# thf_conditional      = re.compile( '$ite('+thf_logic_formula+','+thf_logic_formula+','+
#                            thf_logic_formula+')')
# thf_fof_function     = re.compile( functor+'('+thf_arguments+') |'+
#                            defined_functor+'('+thf_arguments+') |'+
#                            system_functor+'('+thf_arguments+')')
# thf_system_atomic    = re.compile( system_constant)
# thf_defined_infix    = re.compile( thf_unitary_term + defined_infix_pred+
#                            thf_unitary_term)
# thf_defined_atomic   = re.compile( defined_constant+'|'+thf_conditional+'|'+thf_let+'|'+
#                            '('+thf_conn_term+') |' +defined_term)
# thf_plain_atomic     = re.compile( constant+'|'+thf_tuple)
# thf_atomic_formula   = re.compile( thf_plain_atomic+'|'+thf_defined_atomic+'|'+
#                            thf_system_atomic+'|'+thf_fof_function)
# thf_infix_unary      = re.compile( thf_unitary_term + infix_inequality+
#                            thf_unitary_term)
# thf_prefix_unary     = re.compile( thf_unary_connective + thf_preunit_formula)
# thf_unary_formula    = re.compile( thf_prefix_unary+'|'+thf_infix_unary)
# thf_typed_variable   = re.compile( variable+':'+thf_top_level_type)
# thf_variable_list    = re.compile( thf_typed_variable+'|'+
#                            thf_typed_variable+','+thf_variable_list)
# thf_quantification   = re.compile( thf_quantifier+' ['+thf_variable_list+'] :')
# thf_quantified_formula = re.compile( thf_quantification + thf_unit_formula)
# thf_unitary_formula  = re.compile( thf_quantified_formula+'|'+thf_atomic_formula+'|'+
#                            variable+' | ('+thf_logic_formula+')')
# thf_preunit_formula  = re.compile( thf_unitary_formula+'|'+thf_prefix_unary)
# thf_unit_formula     = re.compile( thf_unitary_formula+'|'+thf_unary_formula+'|'+
#                            thf_defined_infix)
# thf_apply_formula    = re.compile( thf_unit_formula+'@'+thf_unit_formula+'|'+
#                            thf_apply_formula+'@'+thf_unit_formula)
# thf_and_formula      = re.compile( thf_unit_formula+'&'+thf_unit_formula+'|'+
#                            thf_and_formula+'&'+thf_unit_formula)
# thf_or_formula       = re.compile( thf_unit_formula + vline + thf_unit_formula+'|'+
#                            thf_or_formula + vline + thf_unit_formula)
# thf_binary_assoc     = re.compile( thf_or_formula+'|'+thf_and_formula+'|'+
#                            thf_apply_formula)
# thf_binary_nonassoc  = re.compile( thf_unit_formula + nonassoc_connective+
#                            thf_unit_formula)
# thf_binary_formula   = re.compile( thf_binary_nonassoc+'|'+thf_binary_assoc+'|'+
#                            thf_binary_type)
# thf_logic_formula    = re.compile( thf_unitary_formula+'|'+thf_unary_formula+'|'+
#                            thf_binary_formula+'|'+thf_defined_infix)
# thf_formula          = re.compile( thf_logic_formula+'|'+thf_atom_typing+'|'+
#                            thf_subtype+'|'+thf_sequent)
# formula_role         = r'axiom | hypothesis | definition | assumption |lemma | theorem | corollary | conjecture |negated_conjecture | plain | type |fi_domain | fi_functors | fi_predicates | unknown'
# formula_role         = re.compile( lower_word)
#
#
# annotations          = re.compile( ','+source+optional_info+'|'+null)
# cnf_annotated        = re.compile( 'cnf('+name+','+formula_role+','+cnf_formula+
#                            annotations+').')
# fof_annotated        = re.compile( 'fof('+name+','+formula_role+','+fof_formula+
#                            annotations+').')
# tcf_annotated        = re.compile( 'tcf('+name+','+formula_role+','+tcf_formula+
#                            annotations+').')
# tff_annotated        = re.compile( 'tff('+name+','+formula_role+','+tff_formula+
#                            annotations+').')
# thf_annotated        = re.compile( 'thf('+name+','+formula_role+','+thf_formula+
#                            annotations+').')
# tpi_formula          = re.compile( fof_formula)
# tpi_annotated        = re.compile( 'tpi('+name+','+formula_role+','+tpi_formula+annotations+').')
# annotated_formula    = re.compile(thf_annotated+'|'+tff_annotated+'|'+tcf_annotated+'|'+
#                            fof_annotated+'|'+cnf_annotated+'|'+tpi_annotated)
# TPTP_input           = re.compile(annotated_formula+'|'+include)
# TPTP_file            = re.compile(TPTP_input+'*')
