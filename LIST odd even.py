
list1=[]
num=int(input("Enter number of element to add:"))
for i in range(1,num+1):
    ele=int(input("Enter the number:"))
    list1.append(ele)
print("\n")
print("THE LIST:",list1)
print("\n")

odd=[]
even=[]


for ele in (list1):
    if ele%2==0:
        even.append(ele)
        
        
    elif ele%2!=0:
        odd.append(ele)
        
    else:
        print("INALID INPUT")
print("ODD=",odd,"EVEN=",even)


