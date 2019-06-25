from unittest import TestCase

from src.antlr_generated.tptpLexer import tptpLexer
from src.antlr_generated.tptpParser import tptpParser, ParseTreeWalker, FileStream, CommonTokenStream
from src.dimacs_converter import DimacsConverter
from main import convert_tptp_to_dimacs


class TestDimacsConverter(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        self.output_file = 'out_dimacs.txt'
        self.example_tptp_file1 = '../examples/cnf/TPTP-library/PUZ031-1.p'
        self.example_tptp_file2 = '../examples/cnf/TPTP-library/SYN000-1.p'
        self.example_tptp_file3 = '../examples/cnf/dimacs-convertable/roles000.p'
        self.example_tptp_file4 = '../examples/cnf/dimacs-convertable/trivial000-0.p'
        self.example_tptp_file5 = '../examples/cnf/dimacs-convertable/trivial000-1.p'
        self.example_tptp_file6 = '../examples/cnf/dimacs-convertable/trivial001.p'
        self.example_tptp_file7 = '../examples/cnf/dimacs-convertable/trivial002-0.p'
        self.example_tptp_file8 = '../examples/cnf/dimacs-convertable/trivial002-1.p'
        self.example_tptp_file9 = '../examples/cnf/dimacs-convertable/trivial002-2.p'

        self.tptp_files = [self.example_tptp_file1, self.example_tptp_file2,
                           self.example_tptp_file3, self.example_tptp_file4, self.example_tptp_file5,
                           self.example_tptp_file6, self.example_tptp_file7, self.example_tptp_file8,
                           self.example_tptp_file9]

    def test_number_of_variables(self):
        var_numbers = [43, 18, 12, 4, 4, 4, 3, 3, 3]

        for tptp_file, curr_var_num in zip(self.tptp_files, var_numbers):
            input_stream = FileStream(tptp_file)
            lexer = tptpLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = tptpParser(stream)
            tree = parser.tptp_file()

            printer = DimacsConverter(self.output_file)

            self.assertEqual(0, printer.number_of_variables)

            walker = ParseTreeWalker()
            walker.walk(printer, tree)

            self.assertEqual(curr_var_num, printer.number_of_variables)

    def test_number_of_clauses(self):
        var_numbers = [26, 8, 12, 1, 1, 2, 2, 2, 1]

        for tptp_file, curr_var_num in zip(self.tptp_files, var_numbers):
            input_stream = FileStream(tptp_file)
            lexer = tptpLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = tptpParser(stream)
            tree = parser.tptp_file()

            printer = DimacsConverter(self.output_file)

            self.assertEqual(0, printer.number_of_clauses)

            walker = ParseTreeWalker()
            walker.walk(printer, tree)

            self.assertEqual(curr_var_num, printer.number_of_clauses)

    def test_example_conversion(self):
        expected = 'p cnf 43 26\n1 -2 0\n1 -3 0\n1 -4 0\n1 -5 0\n1 -6 0\n7 0\n8 0\n9 0\n10 0\n11 0\n12 0\n13 -14 0\n15 16 -17 -18 -19 -20 -21 -22 0\n23 -24 -25 0\n26 -27 -25 0\n28 -25 -29 0\n30 -29 -31 0\n-31 -29 -32 0\n-31 -33 -34 0\n35 -25 -24 0\n-25 -27 -36 0\n37 -24 0\n38 -24 0\n39 -27 0\n40 -27 0\n-17 -41 -33 -42 -43 0\n'

        convert_tptp_to_dimacs(self.example_tptp_file1, self.output_file)

        with open(self.output_file, 'r+') as file:
            output = file.readlines()

        self.assertEqual(expected, ''.join(output))

    def test_example_conversion1(self):
        expected = 'p cnf 3 2\n1 2 0\n3 0\n'
        convert_tptp_to_dimacs(self.example_tptp_file7, self.output_file)

        with open(self.output_file, 'r+') as file:
            output = file.readlines()

        self.assertEqual(expected, ''.join(output))
