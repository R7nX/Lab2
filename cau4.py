a = input("Date in MM/DD/YYYY format: ")

sliceA = slice(0,3)
sliceB = slice(3,6)
sliceC = slice(6,10)
print(f"Date in DD/MM/YYYY format: {a[sliceB]+a[sliceA]+a[sliceC]}" )