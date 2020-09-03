#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    a = 10
    b = 5
    print("{0} + {1} = {2}".format(a, b, calculator_1.add(a, b)))
    print("{0} - {1} = {2}".format(a, b, calculator_1.sub(a, b)))
    print("{0} * {1} = {2}".format(a, b, calculator_1.mul(a, b)))
    print("{0} / {1} = {2}".format(a, b, calculator_1.div(a, b)))
