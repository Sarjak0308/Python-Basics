s=input("Enter any string:")
cu=cl=cd=ca=sp=0

for i in s:
    if i.isupper():
        cu+=1
    elif i.islower():
        cl+=1
    elif i.isdigit():
        cd+=1
    else:
        sp+=1

print("Upper Case:",cu)
print("Lower Case:",cl)
print("Digits:",cd)
print("Special:",sp)
