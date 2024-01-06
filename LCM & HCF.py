a=int(input("Enter 1st no:"))
b=int(input("Enter 2nd no:"))

if a>b:
    for i in range(2,a+1):
        if a%i==0 and b%i==0:
            print("HCF=",i)
if b>a:
    for i in range(2,b+1):
        if a%i==0 and b%i==0:
            print("HCF=",i)
if b>a:
    for i in range(1,11):
        x=b*i
        if x%a==0:
            print("LCM=",x)
 
if a>b:
    for i in range(1,11):
        x=a*i
        if x%b==0:
            print("LCM=",x)
       
