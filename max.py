a=[2,4,3,7,5,9]
first=second=a[0]
for i in range(len(a)):
    if(a[i]>first):
        first=a[i]
        second=first
    elif(a[i]>second and a[i]<first):
        second=a[i]
        
print(second)
