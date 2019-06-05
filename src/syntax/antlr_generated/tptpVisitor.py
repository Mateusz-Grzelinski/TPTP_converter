# Generated from tptp.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tptpParser import tptpParser
else:
    from src.syntax import tptpParser

# This class defines a complete generic visitor for a parse tree produced by tptpParser.

class tptpVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by tptpParser#tptp_file.
    def visitTptp_file(self, ctx:tptpParser.Tptp_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tptp_input.
    def visitTptp_input(self, ctx:tptpParser.Tptp_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#annotated_formula.
    def visitAnnotated_formula(self, ctx:tptpParser.Annotated_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tpi_annotated.
    def visitTpi_annotated(self, ctx:tptpParser.Tpi_annotatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tpi_formula.
    def visitTpi_formula(self, ctx:tptpParser.Tpi_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_annotated.
    def visitThf_annotated(self, ctx:tptpParser.Thf_annotatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tfx_annotated.
    def visitTfx_annotated(self, ctx:tptpParser.Tfx_annotatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_annotated.
    def visitTff_annotated(self, ctx:tptpParser.Tff_annotatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tcf_annotated.
    def visitTcf_annotated(self, ctx:tptpParser.Tcf_annotatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_annotated.
    def visitFof_annotated(self, ctx:tptpParser.Fof_annotatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#cnf_annotated.
    def visitCnf_annotated(self, ctx:tptpParser.Cnf_annotatedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#annotations.
    def visitAnnotations(self, ctx:tptpParser.AnnotationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#formula_role.
    def visitFormula_role(self, ctx:tptpParser.Formula_roleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_formula.
    def visitThf_formula(self, ctx:tptpParser.Thf_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_logic_formula.
    def visitThf_logic_formula(self, ctx:tptpParser.Thf_logic_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_binary_formula.
    def visitThf_binary_formula(self, ctx:tptpParser.Thf_binary_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_binary_pair.
    def visitThf_binary_pair(self, ctx:tptpParser.Thf_binary_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_binary_tuple.
    def visitThf_binary_tuple(self, ctx:tptpParser.Thf_binary_tupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_or_formula.
    def visitThf_or_formula(self, ctx:tptpParser.Thf_or_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_and_formula.
    def visitThf_and_formula(self, ctx:tptpParser.Thf_and_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_apply_formula.
    def visitThf_apply_formula(self, ctx:tptpParser.Thf_apply_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_unitary_formula.
    def visitThf_unitary_formula(self, ctx:tptpParser.Thf_unitary_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_quantified_formula.
    def visitThf_quantified_formula(self, ctx:tptpParser.Thf_quantified_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_quantification.
    def visitThf_quantification(self, ctx:tptpParser.Thf_quantificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_variable_list.
    def visitThf_variable_list(self, ctx:tptpParser.Thf_variable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_variable.
    def visitThf_variable(self, ctx:tptpParser.Thf_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_typed_variable.
    def visitThf_typed_variable(self, ctx:tptpParser.Thf_typed_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_unary_formula.
    def visitThf_unary_formula(self, ctx:tptpParser.Thf_unary_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_atom.
    def visitThf_atom(self, ctx:tptpParser.Thf_atomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_function.
    def visitThf_function(self, ctx:tptpParser.Thf_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_conn_term.
    def visitThf_conn_term(self, ctx:tptpParser.Thf_conn_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_conditional.
    def visitThf_conditional(self, ctx:tptpParser.Thf_conditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_let.
    def visitThf_let(self, ctx:tptpParser.Thf_letContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_arguments.
    def visitThf_arguments(self, ctx:tptpParser.Thf_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_type_formula.
    def visitThf_type_formula(self, ctx:tptpParser.Thf_type_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_typeable_formula.
    def visitThf_typeable_formula(self, ctx:tptpParser.Thf_typeable_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_subtype.
    def visitThf_subtype(self, ctx:tptpParser.Thf_subtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_top_level_type.
    def visitThf_top_level_type(self, ctx:tptpParser.Thf_top_level_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_unitary_type.
    def visitThf_unitary_type(self, ctx:tptpParser.Thf_unitary_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_apply_type.
    def visitThf_apply_type(self, ctx:tptpParser.Thf_apply_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_binary_type.
    def visitThf_binary_type(self, ctx:tptpParser.Thf_binary_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_mapping_type.
    def visitThf_mapping_type(self, ctx:tptpParser.Thf_mapping_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_xprod_type.
    def visitThf_xprod_type(self, ctx:tptpParser.Thf_xprod_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_union_type.
    def visitThf_union_type(self, ctx:tptpParser.Thf_union_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_sequent.
    def visitThf_sequent(self, ctx:tptpParser.Thf_sequentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_tuple.
    def visitThf_tuple(self, ctx:tptpParser.Thf_tupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_formula_list.
    def visitThf_formula_list(self, ctx:tptpParser.Thf_formula_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tfx_formula.
    def visitTfx_formula(self, ctx:tptpParser.Tfx_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tfx_logic_formula.
    def visitTfx_logic_formula(self, ctx:tptpParser.Tfx_logic_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_formula.
    def visitTff_formula(self, ctx:tptpParser.Tff_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_logic_formula.
    def visitTff_logic_formula(self, ctx:tptpParser.Tff_logic_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_binary_formula.
    def visitTff_binary_formula(self, ctx:tptpParser.Tff_binary_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_binary_nonassoc.
    def visitTff_binary_nonassoc(self, ctx:tptpParser.Tff_binary_nonassocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_binary_assoc.
    def visitTff_binary_assoc(self, ctx:tptpParser.Tff_binary_assocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_or_formula.
    def visitTff_or_formula(self, ctx:tptpParser.Tff_or_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_and_formula.
    def visitTff_and_formula(self, ctx:tptpParser.Tff_and_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_unitary_formula.
    def visitTff_unitary_formula(self, ctx:tptpParser.Tff_unitary_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_quantified_formula.
    def visitTff_quantified_formula(self, ctx:tptpParser.Tff_quantified_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_variable_list.
    def visitTff_variable_list(self, ctx:tptpParser.Tff_variable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_variable.
    def visitTff_variable(self, ctx:tptpParser.Tff_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_typed_variable.
    def visitTff_typed_variable(self, ctx:tptpParser.Tff_typed_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_unary_formula.
    def visitTff_unary_formula(self, ctx:tptpParser.Tff_unary_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_atomic_formula.
    def visitTff_atomic_formula(self, ctx:tptpParser.Tff_atomic_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_conditional.
    def visitTff_conditional(self, ctx:tptpParser.Tff_conditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_let.
    def visitTff_let(self, ctx:tptpParser.Tff_letContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_let_term_defns.
    def visitTff_let_term_defns(self, ctx:tptpParser.Tff_let_term_defnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_let_term_list.
    def visitTff_let_term_list(self, ctx:tptpParser.Tff_let_term_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_let_term_defn.
    def visitTff_let_term_defn(self, ctx:tptpParser.Tff_let_term_defnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_let_term_binding.
    def visitTff_let_term_binding(self, ctx:tptpParser.Tff_let_term_bindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_let_formula_defns.
    def visitTff_let_formula_defns(self, ctx:tptpParser.Tff_let_formula_defnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_let_formula_list.
    def visitTff_let_formula_list(self, ctx:tptpParser.Tff_let_formula_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_let_formula_defn.
    def visitTff_let_formula_defn(self, ctx:tptpParser.Tff_let_formula_defnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_let_formula_binding.
    def visitTff_let_formula_binding(self, ctx:tptpParser.Tff_let_formula_bindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_sequent.
    def visitTff_sequent(self, ctx:tptpParser.Tff_sequentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_formula_tuple.
    def visitTff_formula_tuple(self, ctx:tptpParser.Tff_formula_tupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_formula_tuple_list.
    def visitTff_formula_tuple_list(self, ctx:tptpParser.Tff_formula_tuple_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_typed_atom.
    def visitTff_typed_atom(self, ctx:tptpParser.Tff_typed_atomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_subtype.
    def visitTff_subtype(self, ctx:tptpParser.Tff_subtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_top_level_type.
    def visitTff_top_level_type(self, ctx:tptpParser.Tff_top_level_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tf1_quantified_type.
    def visitTf1_quantified_type(self, ctx:tptpParser.Tf1_quantified_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_monotype.
    def visitTff_monotype(self, ctx:tptpParser.Tff_monotypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_unitary_type.
    def visitTff_unitary_type(self, ctx:tptpParser.Tff_unitary_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_atomic_type.
    def visitTff_atomic_type(self, ctx:tptpParser.Tff_atomic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_type_arguments.
    def visitTff_type_arguments(self, ctx:tptpParser.Tff_type_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_mapping_type.
    def visitTff_mapping_type(self, ctx:tptpParser.Tff_mapping_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_xprod_type.
    def visitTff_xprod_type(self, ctx:tptpParser.Tff_xprod_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tcf_formula.
    def visitTcf_formula(self, ctx:tptpParser.Tcf_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tcf_logic_formula.
    def visitTcf_logic_formula(self, ctx:tptpParser.Tcf_logic_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tcf_quantified_formula.
    def visitTcf_quantified_formula(self, ctx:tptpParser.Tcf_quantified_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_formula.
    def visitFof_formula(self, ctx:tptpParser.Fof_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_logic_formula.
    def visitFof_logic_formula(self, ctx:tptpParser.Fof_logic_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_binary_formula.
    def visitFof_binary_formula(self, ctx:tptpParser.Fof_binary_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_binary_nonassoc.
    def visitFof_binary_nonassoc(self, ctx:tptpParser.Fof_binary_nonassocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_binary_assoc.
    def visitFof_binary_assoc(self, ctx:tptpParser.Fof_binary_assocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_or_formula.
    def visitFof_or_formula(self, ctx:tptpParser.Fof_or_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_and_formula.
    def visitFof_and_formula(self, ctx:tptpParser.Fof_and_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_unitary_formula.
    def visitFof_unitary_formula(self, ctx:tptpParser.Fof_unitary_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_quantified_formula.
    def visitFof_quantified_formula(self, ctx:tptpParser.Fof_quantified_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_variable_list.
    def visitFof_variable_list(self, ctx:tptpParser.Fof_variable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_unary_formula.
    def visitFof_unary_formula(self, ctx:tptpParser.Fof_unary_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_infix_unary.
    def visitFof_infix_unary(self, ctx:tptpParser.Fof_infix_unaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_atomic_formula.
    def visitFof_atomic_formula(self, ctx:tptpParser.Fof_atomic_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_plain_atomic_formula.
    def visitFof_plain_atomic_formula(self, ctx:tptpParser.Fof_plain_atomic_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_defined_atomic_formula.
    def visitFof_defined_atomic_formula(self, ctx:tptpParser.Fof_defined_atomic_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_defined_plain_formula.
    def visitFof_defined_plain_formula(self, ctx:tptpParser.Fof_defined_plain_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_defined_infix_formula.
    def visitFof_defined_infix_formula(self, ctx:tptpParser.Fof_defined_infix_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_system_atomic_formula.
    def visitFof_system_atomic_formula(self, ctx:tptpParser.Fof_system_atomic_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_plain_term.
    def visitFof_plain_term(self, ctx:tptpParser.Fof_plain_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_defined_term.
    def visitFof_defined_term(self, ctx:tptpParser.Fof_defined_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_defined_atomic_term.
    def visitFof_defined_atomic_term(self, ctx:tptpParser.Fof_defined_atomic_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_defined_plain_term.
    def visitFof_defined_plain_term(self, ctx:tptpParser.Fof_defined_plain_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_system_term.
    def visitFof_system_term(self, ctx:tptpParser.Fof_system_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_arguments.
    def visitFof_arguments(self, ctx:tptpParser.Fof_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_term.
    def visitFof_term(self, ctx:tptpParser.Fof_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_function_term.
    def visitFof_function_term(self, ctx:tptpParser.Fof_function_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_conditional_term.
    def visitTff_conditional_term(self, ctx:tptpParser.Tff_conditional_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_let_term.
    def visitTff_let_term(self, ctx:tptpParser.Tff_let_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_tuple_term.
    def visitTff_tuple_term(self, ctx:tptpParser.Tff_tuple_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_sequent.
    def visitFof_sequent(self, ctx:tptpParser.Fof_sequentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_formula_tuple.
    def visitFof_formula_tuple(self, ctx:tptpParser.Fof_formula_tupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_formula_tuple_list.
    def visitFof_formula_tuple_list(self, ctx:tptpParser.Fof_formula_tuple_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#cnf_formula.
    def visitCnf_formula(self, ctx:tptpParser.Cnf_formulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#cnf_disjunction.
    def visitCnf_disjunction(self, ctx:tptpParser.Cnf_disjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#cnf_literal.
    def visitCnf_literal(self, ctx:tptpParser.Cnf_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_quantifier.
    def visitThf_quantifier(self, ctx:tptpParser.Thf_quantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#th0_quantifier.
    def visitTh0_quantifier(self, ctx:tptpParser.Th0_quantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#th1_quantifier.
    def visitTh1_quantifier(self, ctx:tptpParser.Th1_quantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_pair_connective.
    def visitThf_pair_connective(self, ctx:tptpParser.Thf_pair_connectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#thf_unary_connective.
    def visitThf_unary_connective(self, ctx:tptpParser.Thf_unary_connectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#th1_unary_connective.
    def visitTh1_unary_connective(self, ctx:tptpParser.Th1_unary_connectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#tff_pair_connective.
    def visitTff_pair_connective(self, ctx:tptpParser.Tff_pair_connectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#fof_quantifier.
    def visitFof_quantifier(self, ctx:tptpParser.Fof_quantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#binary_connective.
    def visitBinary_connective(self, ctx:tptpParser.Binary_connectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#assoc_connective.
    def visitAssoc_connective(self, ctx:tptpParser.Assoc_connectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#unary_connective.
    def visitUnary_connective(self, ctx:tptpParser.Unary_connectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#type_constant.
    def visitType_constant(self, ctx:tptpParser.Type_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#type_functor.
    def visitType_functor(self, ctx:tptpParser.Type_functorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#defined_type.
    def visitDefined_type(self, ctx:tptpParser.Defined_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#system_type.
    def visitSystem_type(self, ctx:tptpParser.System_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#atom.
    def visitAtom(self, ctx:tptpParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#untyped_atom.
    def visitUntyped_atom(self, ctx:tptpParser.Untyped_atomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#defined_proposition.
    def visitDefined_proposition(self, ctx:tptpParser.Defined_propositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#defined_predicate.
    def visitDefined_predicate(self, ctx:tptpParser.Defined_predicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#defined_infix_pred.
    def visitDefined_infix_pred(self, ctx:tptpParser.Defined_infix_predContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#constant.
    def visitConstant(self, ctx:tptpParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#functor.
    def visitFunctor(self, ctx:tptpParser.FunctorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#system_constant.
    def visitSystem_constant(self, ctx:tptpParser.System_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#system_functor.
    def visitSystem_functor(self, ctx:tptpParser.System_functorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#defined_constant.
    def visitDefined_constant(self, ctx:tptpParser.Defined_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#defined_functor.
    def visitDefined_functor(self, ctx:tptpParser.Defined_functorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#defined_term.
    def visitDefined_term(self, ctx:tptpParser.Defined_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#variable.
    def visitVariable(self, ctx:tptpParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#source.
    def visitSource(self, ctx:tptpParser.SourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#sources.
    def visitSources(self, ctx:tptpParser.SourcesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#dag_source.
    def visitDag_source(self, ctx:tptpParser.Dag_sourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#inference_record.
    def visitInference_record(self, ctx:tptpParser.Inference_recordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#inference_rule.
    def visitInference_rule(self, ctx:tptpParser.Inference_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#inference_parents.
    def visitInference_parents(self, ctx:tptpParser.Inference_parentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#parent_list.
    def visitParent_list(self, ctx:tptpParser.Parent_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#parent_info.
    def visitParent_info(self, ctx:tptpParser.Parent_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#parent_details.
    def visitParent_details(self, ctx:tptpParser.Parent_detailsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#internal_source.
    def visitInternal_source(self, ctx:tptpParser.Internal_sourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#intro_type.
    def visitIntro_type(self, ctx:tptpParser.Intro_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#external_source.
    def visitExternal_source(self, ctx:tptpParser.External_sourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#file_source.
    def visitFile_source(self, ctx:tptpParser.File_sourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#file_info.
    def visitFile_info(self, ctx:tptpParser.File_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#theory.
    def visitTheory(self, ctx:tptpParser.TheoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#theory_name.
    def visitTheory_name(self, ctx:tptpParser.Theory_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#creator_source.
    def visitCreator_source(self, ctx:tptpParser.Creator_sourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#creator_name.
    def visitCreator_name(self, ctx:tptpParser.Creator_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#optional_info.
    def visitOptional_info(self, ctx:tptpParser.Optional_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#useful_info.
    def visitUseful_info(self, ctx:tptpParser.Useful_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#info_items.
    def visitInfo_items(self, ctx:tptpParser.Info_itemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#info_item.
    def visitInfo_item(self, ctx:tptpParser.Info_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#formula_item.
    def visitFormula_item(self, ctx:tptpParser.Formula_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#description_item.
    def visitDescription_item(self, ctx:tptpParser.Description_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#iquote_item.
    def visitIquote_item(self, ctx:tptpParser.Iquote_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#inference_item.
    def visitInference_item(self, ctx:tptpParser.Inference_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#inference_status.
    def visitInference_status(self, ctx:tptpParser.Inference_statusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#status_value.
    def visitStatus_value(self, ctx:tptpParser.Status_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#inference_info.
    def visitInference_info(self, ctx:tptpParser.Inference_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#assumptions_record.
    def visitAssumptions_record(self, ctx:tptpParser.Assumptions_recordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#refutation.
    def visitRefutation(self, ctx:tptpParser.RefutationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#new_symbol_record.
    def visitNew_symbol_record(self, ctx:tptpParser.New_symbol_recordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#new_symbol_list.
    def visitNew_symbol_list(self, ctx:tptpParser.New_symbol_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#principal_symbol.
    def visitPrincipal_symbol(self, ctx:tptpParser.Principal_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#include.
    def visitInclude(self, ctx:tptpParser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#formula_selection.
    def visitFormula_selection(self, ctx:tptpParser.Formula_selectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#name_list.
    def visitName_list(self, ctx:tptpParser.Name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#general_term.
    def visitGeneral_term(self, ctx:tptpParser.General_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#general_data.
    def visitGeneral_data(self, ctx:tptpParser.General_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#general_function.
    def visitGeneral_function(self, ctx:tptpParser.General_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#formula_data.
    def visitFormula_data(self, ctx:tptpParser.Formula_dataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#general_list.
    def visitGeneral_list(self, ctx:tptpParser.General_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#general_terms.
    def visitGeneral_terms(self, ctx:tptpParser.General_termsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#name.
    def visitName(self, ctx:tptpParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#atomic_word.
    def visitAtomic_word(self, ctx:tptpParser.Atomic_wordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#atomic_defined_word.
    def visitAtomic_defined_word(self, ctx:tptpParser.Atomic_defined_wordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#atomic_system_word.
    def visitAtomic_system_word(self, ctx:tptpParser.Atomic_system_wordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#number.
    def visitNumber(self, ctx:tptpParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tptpParser#file_name.
    def visitFile_name(self, ctx:tptpParser.File_nameContext):
        return self.visitChildren(ctx)



del tptpParser