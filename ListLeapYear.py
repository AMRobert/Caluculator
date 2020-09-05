Y1 = int(input())
Y2 = int(input())
for i in range(Y1,Y2+1):
    if ((i%4==0 and i%100!=0) or i%400==0):
        print(i,"\n")
