import numpy as np
import random

'''
ОТКРЫТЫЙ ТЕКСТ: двойная перестановка
МАРШРУТ ВПИСЫВАНИЯ: слева - направо
МАРШРУТ ВЫПИСЫВАНИЯ: сверху - вниз
СТОЛБЦЫ: ( 3, 1, 4, 2) 		//сейчас рандом
СТРОКИ: ( 3, 2, 4, 1, 5)	//сейчас рандом
'''

def setToCh(smt):	#конвертирует строку из последовательности цифр, хранящей перестановку, в список
	smt_ch = []
	for n in smt:
		smt_ch.append(int(n))
	#print(type(smt_ch), smt_ch)
	return smt_ch

def d_print(x,y):
	print("Расшифрованный текст: ", x)
	return 1

def strToTable(msg, row_dim, col_dim):						#вписывает слева-направо в таблицу
	msg_table = []
	for i in range(0, row_dim):
		msg_table.append([])
		for j in range(0, col_dim):
			msg_table[i].append(msg[col_dim*i +j])
	#print(msg_table)
	return msg_table

def changeCols(msg_table, col_ch, row_dim):						#перестановка столбцов
	new_msg_table = []
	for i in range(0, row_dim):
		new_msg_table.append([])
		for j in col_ch:
			new_msg_table[i].append(msg_table[i][j])
	#print("Таблица после перестановки столбцов: ", new_msg_table)
	return new_msg_table

def changeRows(msg_table, row_set):								#перестановка строк
	new_msg_table = []
	for i in range(0, len(row_set)):
		a = int(row_set[i])
		new_msg_table.append(msg_table[a])
	#print("Таблица после перестановки строк: ", new_msg_table)
	return new_msg_table

def printCryptLR(msg_table, col_dim, row_dim):					#выписывает слева-направо
	print_msg = []
	for i in range(0, len(msg_table)):
		for j in range(0, len(msg_table[i])):
			if msg_table[i][j] != "+":
				print_msg.append(msg_table[i][j])
	print_msg = "".join(print_msg)
	print("Зашифрованный текст: ", print_msg)


def printCrypt(msg_table, col_dim, row_dim):					#выписывает сверху-вниз
	print_msg = []
	for i in range(0, col_dim):
		for j in range(0, row_dim):
			#if msg_table[j][i] != "+":
			print_msg.append(msg_table[j][i])
	print_msg = "".join(print_msg)
	print("Зашифрованный текст: ", print_msg)

def genCrypt(msg):				#шифрование
	#col_dim = int(input("Введите количество столбцов таблицы: "))
	col_dim = random.randint(2,len(msg)-1)				#генерим размерность таблицы в зависимости от количества столбцов
	#print("col_dim: ",col_dim)
	if len(msg) % col_dim == 0:							#считаем соответствующее столбцам число строк
		row_dim = int(len(msg) / col_dim)
	else:
		row_dim = int(len(msg) // col_dim + 1)
		for add in range(col_dim - (len(msg) % col_dim)):
			msg = msg + " " 
	#print(msg)

	#col_set = str(input("Введите порядок столбцов от 0 до " + str(col_dim-1) +" включительно (без пробелов): "))
	#col_ch = setToCh(col_set)

	col_temp = list(range(0, col_dim))			#генерим случайную перестановку столбцов
	random.shuffle(col_temp)
	col_dict = dict(zip(list(range(0, col_dim)),col_temp))
	#print(col_dict)

	#row_set = str(input("Введите порядок строк от 0 до " + str(row_dim-1) +" включительно (без пробелов): "))
	#row_ch = setToCh(row_set)

	row_temp = list(range(0, row_dim))			#генерим случайную перестановку строк
	random.shuffle(row_temp)
	row_dict = dict(zip(list(range(0, row_dim)),row_temp))

	msg_table = strToTable(msg,row_dim,col_dim)
	msg_table = changeCols(msg_table, col_temp, row_dim)	#меняем столбцы
	msg_table = changeRows(msg_table, row_temp)	#меняем строки
	printCrypt(msg_table, col_dim, row_dim)

	return msg_table, col_temp, row_temp, col_dim, row_dim

def decryptTable(msg, msg_table, col_temp, row_temp, col_dim, row_dim):
	d_msg_table = changeRows(msg_table, row_temp)	#меняем строки
	d_msg_table = changeCols(msg_table, col_temp, row_dim)	#меняем столбцы

	d_print(msg, d_msg_table)

	return d_msg_table



print("\n")
print("Праздник шифрования начинается!!!")
print("\n")

msg = input("Введите текст для шифрования: ")

res = genCrypt(msg)

#d_msg = input("Введите текст для расшифрования: ")

decryptTable(msg, res[0],res[1],res[2], res[3], res[4])

#printCrypt(msg_table, col_dim, row_dim)
#printCrypt(res[0], res[1], res[2])