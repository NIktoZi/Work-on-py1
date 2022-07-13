# dat=int(input('Введите день номер дня недели '))
# if dat>7 or dat<0:
#     print('Ошибка:Нет такого номера дня нендели ')
# else:
#     if dat==6 or dat==7:
#         print('Выходной')
#         if dat==6: 
#             print('суббота')
#         else:
#             print('Воскресенье')
#     else:
#         print('День недели не является выходным')

# №2 
# print('x,y,z  результат 1    результат 2')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             res= not (x or y or z)
#             res2= not (x) or not (y) or not (z)
#             print(x,y,z,'  ',res,'   ',res2)
#             if res ==res2:
#                 print('Верное равенство')
#№3
x=int(input('Введите кординату X '))
y=int(input('Введите кординату Y '))
if x==0 and y==0:
    print('Недопустимое значение')
elif x>0 and y>0:
    print('Первая четверть')
elif x>0 and y<0:
    print('Четветрая четверть')
elif x<0 and y>0:
    print('Вторая четверть')
elif x<0 and y<0:
    print('Третья четверть')

