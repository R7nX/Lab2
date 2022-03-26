a = float(input("Length of a square edge: "))


def squareroot(a):
    a = a**(1/2)
    return a

print(f"Length of diagonal line: {squareroot(a+a)}")