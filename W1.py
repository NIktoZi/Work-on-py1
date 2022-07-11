dat=int(input('Введите день номер дня недели '))
if dat>7 or dat<0:
    print('Ошибка:Нет такого номера дня нендели ')
else:
    if dat==6 or dat==7:
        print('Выходной')
        if dat==6: 
            print('суббота')
        else:
            print('Воскресенье')
    else:
        print('День недели не является выходным')