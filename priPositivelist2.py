a = [];
lin = (int)(input("Enter the limit of the range : "));
i=0;
while(i<lin):
    b = (int)(input("Enter elements of the range : "));
    a.append(b);
    b=0;
    i=i+1;
print(a)
k=0;
while(k<lin):
    c = a[k-1];
    if(c < 0):
        a.remove(c);
    k=k+1;
print(a)
