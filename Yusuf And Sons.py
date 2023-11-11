print('Welcome to Yusuf and Sons Company!')
print('To Calculate your Simple and Compound Interest:')
p = float(input("Enter Initial Principal: "))

r = float(input("Enter Interest Rate: "))

t = float(input("Enter Time: "))

n = float(input("Enter Number of Times: "))

Simple_Interest = str(p * (1 + r * t))
Compound_Interest = str(p * (1 + r/n) ** n * t)

print("YUSUF AND SONS COMPANY")
print("SIMPLE INTEREST = " + Simple_Interest)
print("COMPOUND INTEREST = " + Compound_Interest)
print('Thank You!')