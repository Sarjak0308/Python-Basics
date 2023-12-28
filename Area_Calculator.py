'''This Programme is to caculate Areas od some 2d figures'''


print("Welcome to area calculator")
print("\n")
print("Square=1")
print("Rectangle=2")
print("Circle=3")
print("Triangle=4")
print("\n")

z=int(input("Enter your shape no.:"))
print("\n")

if z==1:
    x=float(input("Enter Length:"))
    A=x*x
    print("Area is=",A,"Units")
elif z==2:
    x=float(input("Enter Length:"))
    y=float(input("Enter Breadth:"))
    A=x*y
    print("Area is=",A,"Units")
elif z==3:
    r=float(input("Enter Radius:"))
    A=(3.14)*(r**2)
    print("Area is=",A,"Units")
elif z==4:
    h=float(input("Enter height:"))
    s=float(input("Enter base:"))
    A=(0.5)*s*h
    print("Area is=",A,"Units")
else:
    print("Invalid input!!")
    
