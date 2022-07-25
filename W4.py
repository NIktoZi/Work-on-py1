#1
#  from math import factorial as fact

# i=1
# f=-1
# a=13591409
# b=545140134
# c=640320
# d=c**(3/2)
# s=a/d
# pi=3
# while str(pi)[:12]!= '3.1415926535':
#     numb=(f*fact(6*i)*(a+b*i)/(fact(3*i)*fact(i)**3*d*c**(3*i)))
#     s+=numb
#     f*=-1
#     i+=1
#     pi=1/(12*s)
# print(pi)
# print(i-1)
#3

Numb=int(input("Введите число "))
i=2
list_del=[]
while i<Numb:
    if Numb%i==0:
        list_del.append(i)
        Numb //=i
        i+=1
    else:
        i+=1
print('Делители получились-',list_del)