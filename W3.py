#1
sp=[2,3,5,9,3]
su=0
for i in range(len(sp)):
    if i%2!=0:
        su=sp[i]+su
print(su)
