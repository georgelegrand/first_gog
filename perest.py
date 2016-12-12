import numpy as np
import math
#from random import randint

'''
ОТКРЫТЫЙ ТЕКСТ: двойная перестановка
МАРШРУТ ВПИСЫВАНИЯ: слева - направо
МАРШРУТ ВЫПИСЫВАНИЯ: сверху - вниз
СТОЛБЦЫ: ( 3, 1, 4, 2)
СТРОКИ: ( 3, 2, 4, 1, 5)
'''

def checker():
	return 1


def d_print(x,y):
	print("Расшифрованный текст: ", x)
	return 1


def setToCh(smt):
	smt_ch = []
	for n in smt:
		smt_ch.append(int(n))
	print(type(smt_ch), smt_ch)
	return smt_ch

def strToTable(msg, row_dim, col_dim):						#вписывает слева-направо
	msg_table = []
	for i in range(0, row_dim):
		msg_table.append([])
		for j in range(0, col_dim):
			msg_table[i].append(msg[col_dim*i +j])
	print(msg_table)
	return msg_table

def changeCols(msg_table, col_ch, row_dim):		#working!!!
	new_msg_table = []
	for i in range(0, row_dim):
		new_msg_table.append([])
		for j in col_ch:
			new_msg_table[i].append(msg_table[i][j])
	print("Таблица после перестановки столбцов: ", new_msg_table)
	return new_msg_table

def changeRows(msg_table, row_set):
	new_msg_table = []
	for i in range(0, len(row_set)):
		a = int(row_set[i])
		new_msg_table.append(msg_table[a])
	print("Таблица после перестановки строк: ", new_msg_table)
	return new_msg_table
'''
def printCrypt(msg_table, col_dim, row_dim):					#выписывает слева-направо
	print_msg = []
	for i in range(0, len(msg_table)):
		for j in range(0, len(msg_table[i])):
			if msg_table[i][j] != "+":
				print_msg.append(msg_table[i][j])
	print_msg = "".join(print_msg)
	print("Зашифрованный текст: ", print_msg)
'''

def printCrypt(msg_table, col_dim, row_dim):					#выписывает сверху-вниз
	print_msg = []
	for i in range(0, col_dim):
		for j in range(0, row_dim):
			if msg_table[j][i] != "+":
				print_msg.append(msg_table[j][i])
	print_msg = "".join(print_msg)
	print("Зашифрованный текст: ", print_msg)


def decryptTable(msg, msg_table, col_dim, row_dim, col_ch, row_set):
	d_msg_table = changeRows(msg_table, row_set)	#меняем строки
	d_msg_table = changeCols(msg_table, col_ch, row_dim)	#меняем столбцы

	d_print(msg, d_msg_table)

	return d_msg_table

def genOrder(msg):
	col_dim = int(input("Введите количество столбцов таблицы: "))
	#col_dim = random.randint(2,len(msg)-1)
	if len(msg) % col_dim == 0:
		row_dim = int(len(msg) / col_dim)
	else:
		row_dim = int(len(msg) // col_dim + 1)
		for add in range(col_dim - (len(msg) % col_dim)):
			#msg = msg + "+"
			msg = msg + " " 
	print(msg)

	col_set = str(input("Введите порядок столбцов от 0 до " + str(col_dim-1) +" включительно (без пробелов): "))
	col_ch = setToCh(col_set)

	row_set = str(input("Введите порядок строк от 0 до " + str(row_dim-1) +" включительно (без пробелов): "))
	row_ch = setToCh(row_set)

	msg_table = strToTable(msg,row_dim,col_dim)
	msg_table = changeCols(msg_table, col_ch, row_dim)
	msg_table = changeRows(msg_table, row_set)
	return msg_table, col_dim, row_dim, col_ch, row_set


print("\n")
print("Праздник шифрования начинается!!!")
print("\n")

msg = input("Введите текст: ")

res = genOrder(msg)

printCrypt(res[0], res[1], res[2])
decryptTable(msg, res[0], res[1], res[2], res[3], res[4])