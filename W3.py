#1
# sp=[2,3,5,9,3]
# su=0
# for i in range(len(sp)):
#     if i%2!=0:
#         su=sp[i]+su
# print(su)
#2
# sp=[2,3,4,5,6]
# sp2=[]
# su=0
# for i in range(len(sp)):
#     su=0
#     su=sp[i]+sp[-i]
#     sp2.append(su)
# print(sp2)
#3
# sp=[1.1, 1.2, 3.1, 5.567, 10.003]
# ma=-10
# mi=1000
# fr=0
# for i in range(len(sp)):
#     fr=sp[i]%1
#     if fr>ma:
#         ma=fr
#     elif fr<ma and fr<mi:
#         mi=fr
# print(ma-mi)
#4
def dectodv(d):
     if d>1:
         dectodv(d//2)
     print(d%2,end=' ')

# des=int(input('число в дес сс '))
# if des<0:
#     des=-des
# dectodv(des)
#5
def fi(k):
    if k>-1:
        if k==0:
            return 1
        elif k==1:
            return 1
        else:
            return fi(k-1)+fi(k-2)
    if k<=-1:
        return((-1)**k+1)*fi(-k)
    lis=[k]
    print(lis)

fibo=int(input("Введите индекс "))
print(fi(fibo))
