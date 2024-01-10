print("WELCOME TO MIN MAX FINDER")
print("\n")

list1=[]

num=int(input("Enter the number of element to add:"))
for i in range(1,num+1):
    ele=int(input("Enter the number:"))
    list1.append(ele)
print("\n")
print("THE LIST:",list1)
print("\n")

list1.sort()

print("Minimum Value in list is:",list1[0])
print("Maximum Value in list is:",list1[-1])
