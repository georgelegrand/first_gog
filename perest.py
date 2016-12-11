import numpy as np
import math

def setToCh(smt):
	smt_ch = []
	for n in smt:
		smt_ch.append(int(n))
	print(type(smt_ch), smt_ch)
	return smt_ch

def strToTable(msg, row_dim, col_dim):
	msg_table = []
	for i in range(0, row_dim):
		msg_table.append([])
		for j in range(0, col_dim):
			msg_table[i].append(msg[col_dim*i +j])
	print(msg_table)
	return msg_table

def changeRows(msg_table, row_set):
	new_msg_table = []
	for i in range(0, len(row_set)):
		a = int(row_set[i])
		new_msg_table.append(msg_table[a])
	print("New table after changing rows: ", new_msg_table)
	return new_msg_table

def changeCol(msg_table, col_set, row_dim):
	new_msg_table = []
	for j in col_set:
		for i in range(0, row_dim):
			new_msg_table.append(msg_table[i][int(col_set[int(j)])])
	print(new_msg_table)
	return new_msg_table


print("\n")
print("Праздник шифрования начинается!!!")
print("\n")

msg = input("Enter text: ")
col_dim = int(input("Enter num of columns: "))

if len(msg) % col_dim == 0:
	row_dim = int(len(msg) / col_dim)
else:
	row_dim = int(len(msg) // col_dim + 1)
	for add in range(col_dim - (len(msg) % col_dim)):
		msg = msg + "+" 
print(msg)

col_set = str(input("Введите порядок столбцов от 0 до " + str(col_dim-1) +" включительно (без пробелов): "))
col_ch = setToCh(col_set)

row_set = str(input("Введите порядок строк от 0 до " + str(row_dim-1) +" включительно (без пробелов): "))
row_ch = setToCh(row_set)

msg_table = strToTable(msg,row_dim,col_dim)

r_tab = changeRows(msg_table, row_set)
changeCol(r_tab, col_set, row_dim)
