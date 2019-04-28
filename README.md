# TPTP to dimacs converter

TPTP and dimacs are syntax for describing SAT problems

This project converts TPTP syntax to dimacs when it is possible


## Online resources

TPTP BNF: http://www.tptp.org/TPTP/SyntaxBNF.html

TPTP quick start (not very useful): http://www.tptp.org/TPTP/QuickGuide/

TPTP detail description (technical document): http://www.tptp.org/TPTP/TR/TPTPTR.shtml

I haven't found any tutorial for TPTP syntax.

Dimacs syntax: http://www.domagoj-babic.com/uploads/ResearchProjects/Spear/dimacs-cnf.pdf

Dimacs tutorial: https://fairmut3x.wordpress.com/2011/07/29/cnf-conjunctive-normal-form-dimacs-format-explained/

## Dependencies

Python 3.6 or higher required

```sh
pip install -r requirements.txt
```

## Usage

```sh
python main.py -h
```

## Alternatives

TPTP2X is utility that comes with TPTP package and it is able to convert TPTP to many different formats. Unfortunately is is written is prolog.