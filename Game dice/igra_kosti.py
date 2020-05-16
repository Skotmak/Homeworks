while 1 == 1:

	print('Игра "кости" на python')
	print('Версия:1.0')
	
	import random

	input("Нажмите ENTER,чтобы начать игру")

	gamer1 = random.randint(1,6)
	print("Ваше число:")
	print(gamer1)

	input("Нажмите ENTER,чтобы продолжить игру")

	gamer2 = random.randint(1,6)
	print("Число противника:")
	print(gamer2)

	if gamer1 > gamer2:
		print("Поздравляю!Вы выиграли!")
	elif gamer1 == gamer2:
		print("Ничья!")
	else:
		print("К сожалению,вы проиграли!")

	igra = input('Сыграть ещё?(Введите "y" ,если да.Введите "n" ,если нет):')

	if igra == "n":
		break
	elif igra == "y":
		pass
	else:
		print("Ты дебил?")
		input()
		print("Ну нахер...")
		break
    	



	

