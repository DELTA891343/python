p = float(input("enter amount:"))
n = float(input("enter number of years"))
r = float(input("enter rate of interest"))
si = (p * n * r)/100
print("simple intrest is:",si)

ci = p*(pow((1+r/100),n))
print("compound interest is:",ci) 
