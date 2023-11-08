p = float(input("Enter Initial Principal: "))

r = float(input("Enter Interest Rate: "))

t = float(input("Enter Time: "))

n = float(input("Enter Number of Times: "))

Simple_Interest = str(p * (1 + r * t))
Compound_Interest = str(p * (1 + r/n) ** n * t)

print("YUSUF AND SONS")
print("SIMPLE INTEREST = " + Simple_Interest)
print("COMPOUND INTEREST = " + Compound_Interest)