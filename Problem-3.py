a= int(input("Enter the number: "))
if a%2==0:
    a=a-1
for i in range(1,a+1):
    if i<a:
        print(2*i-1,end=",")
    else:
        print(2*i-1)