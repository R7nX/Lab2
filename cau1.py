from asyncio import constants


r = float(input("Enter the circle radius: "))

pi = 3.1416

def square(a):
    a = a*a
    return a

print(f"Perimeter: {2*pi*r}")
print(f"Area: {pi*square(r)}" )