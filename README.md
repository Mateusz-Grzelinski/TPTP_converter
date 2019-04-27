# TPTP to dimacs converter

TPTP and dimacs are syntax for describing SAT problems

This project converts TPTP syntax to dimacs when it is possible

TPTP BNF: http://www.tptp.org/TPTP/SyntaxBNF.html
Dimacs syntax: http://www.domagoj-babic.com/uploads/ResearchProjects/Spear/dimacs-cnf.pdf

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