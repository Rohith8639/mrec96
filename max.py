a=[2,4,3,7,5,9]
max=a[0]
smax=max
for i in range(len(a)):
    if(a[i]>max):
        smax=max
        max=a[i]
print(smax)
