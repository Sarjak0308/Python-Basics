num = int(input("Enter a number: "))  

if  num==2:
    print("No is prime no")
if num==1:
   print("It is neutral number")
if num > 2:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")
