a = (int)(input("Enter the total number of elements of the Fibonacci series: "));
n1=0;
n2=1;
print(n1,",",n2,",", end =" ")
i=2;
while i<=a:
    n3=n1+n2;
    n1=n2;
    n2=n3;
    if i!=a:
        print(n3,",",end = " ")
    else:
        print(n3, end = " ")
    i=i+1;
    
