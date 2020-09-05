#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    arg = sys.argv
    L = len(sys.argv)
    if L != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(arg[1])
    op = arg[2]
    b = int(arg[3])
    if op not in '+*-/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if op == "+":
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, add(a, b)))
    if op == "-":
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, sub(a, b)))
    if op == "*":
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, mul(a, b)))
    if op == "/":
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, div(a, b)))
