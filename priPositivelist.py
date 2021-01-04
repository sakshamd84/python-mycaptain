a = [];
lin = (int)(input("Enter the limit of the range : "));
i=0;
while(i<lin):
    b = (int)(input("Enter elements of the range : "));
    a.append(b);
    b=0;
    i=i+1;
j=0;
while(j<lin):
    if(a[j]>0):
        print(a[j],",", end = " ")
        j=j+1;
    else:
        j=j+1;
