#Mathematical series   (x/1!)+(x^2/2!)....

n=int(input("Find the Sum of series up to:"))
x=float(input("Enter the value of x:"))

sum=0
p=1
q=1

for i in range(1,n+1):
    p=x*p
    q=i*q
    sum=sum+(p/q)

print("Sum of the series is",sum)
