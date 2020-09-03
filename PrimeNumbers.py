Num = int(input("Enter the Number: "))
if Num > 1:
   for i in range(2,Num):
       if (Num % i) == 0:
           print(Num,"is not a prime number")
           break
   else:
       print(Num,"is a prime number")
else:
   print(Num,"is not a prime number")
