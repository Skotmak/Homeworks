x = int(input("Введите x="))
y = int(input("Введите y="))
if x>0 and y>0:
    print('Ответ: I')
elif x<0 and y>0:
    print('Ответ: II')
elif x<0 and y<0:
    print('Ответ: III')
elif x>0 and y<0:
    print('Ответ: IV')
