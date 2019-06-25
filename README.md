# TPTP to dimacs converter

TPTP and dimacs are syntax for describing SAT problems

This project converts TPTP syntax to dimacs when it is possible


## Online resources

TPTP BNF: http://www.tptp.org/TPTP/SyntaxBNF.html

TPTP detail description (technical document): http://www.tptp.org/TPTP/TR/TPTPTR.shtml


Dimacs syntax: http://www.domagoj-babic.com/uploads/ResearchProjects/Spear/dimacs-cnf.pdf

Dimacs tutorial: https://fairmut3x.wordpress.com/2011/07/29/cnf-conjunctive-normal-form-dimacs-format-explained/

## Dependencies

Python 3.6 or higher required.

```bash
pip install -r requirements.txt
```

Do not edit files in `antrl_generated` they are generated automatically. There is also defined grammar for dimacs but it was not used.

## Usage

```bash
python main.py -h
```

Example command (converted file will be saved to out.dimacs)

```bash
python main.py -f examples/cnf/dimacs-convertable/roles000.p
```


