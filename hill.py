import numpy as np
from math import sqrt as sqrt

print("\n")
print("Праздник шифрования начинается!!!")
print("\n")

alphabet = 'abcdefghijklmnopqrstuvwxyz,. '

def Euclid(a,b):	#(det, len(alphabet)), a>=b, расширенный алгоритм Евклида поиска мультипликативной инверсии числа
	if b == 0:
		x = 1
		y = 0
		d = a
	else:
		x_2 = 1
		x_1 = 0
		y_2 = 0
		y_1 = 1
		while b > 0:
			q = a//b
			r = a - q*b
			x = x_2 - q*x_1
			y = y_2 - q*y_1
			a = b
			b = r
			x_2 = x_1
			x_1 = x
			y_2 = y_1
			y_1 = y
		d = a
		x = x_2
		y = y_2
	return(x,y,d)

def make_dict(row):	#парсит строку в словарь, нумерует символы строки
	#print("Длина строки: "+ str(len(row)))
	row_dict = dict(zip(list(range(0, len(row))),list(row)))
	#print(row_dict)
	return(row_dict)

def row_code(row, alphabet): #ставим символам текста соответствие номеров из алфавита
	row_dict = make_dict(row)
	alphabet_dict = make_dict(alphabet)
	row_code = np.array([])
	for j in range(0, len(row)):	
		for i in range(0, len(alphabet)):
			if row_dict[j] == alphabet_dict[i]:
				row_code = np.append(row_code, [[i]])
	#print(row_code)
	return(row_code)

def check_det(matrix, dim, alphabet):	#проверка матрицы ключа на определенность
	dim = 3
	det = int(np.linalg.det(matrix))
	#print(det)
	if det >=len(alphabet):
		checker = Euclid(det,len(alphabet))
	else:
		checker = Euclid(len(alphabet),det)
	#print("checker", checker)
	if checker[2] != 1:
		matrix = np.random.random((dim,dim))
		#i = 0
		print("Неправильный ключ, генерируется новый...")
		check_det(matrix, dim, alphabet)
	else:
		#print(det)
		return(matrix)

def user_key(alphabet):
	dim = 3
	keyword = input("Введите ключ длиной 9 символов: ")
	keydict = row_code(keyword, alphabet)
	key = []
	for i in range(3):
		key.append([])
		for j in range(3):
			key[i].append(keydict[3*i+j])
	matrix = np.array(key)
	if np.linalg.det(matrix)!=0:
		key = check_det(matrix,dim, alphabet)
		#print("Ключ: ", key)					#gybnqkurp
		return(key)
	else:
		print("Неверный ключ!")

def rand_key_gen(row, alphabet):	#генератор случайной матрицы ключа
	dim = 3
	#matrix = np.random.random((dim,dim))
	matrix = np.random.random_integers(29, size=(3,3))
	#matrix = np.around(matrix*10) % len(alphabet)
	matrix = matrix % len(alphabet)
	key = check_det(matrix,dim, alphabet)
	print("Ключ: ", key)
	return(key)

def row_decode(crypt_result, alphabet):	#декодируем цифры в зашифрованный текст
	row_decode = []
	for j in range(0, len(crypt_result)):
		row_decode.append(alphabet[round(float(crypt_result[j]))%len(alphabet)])
	res = ''.join(row_decode)
	#print(res)
	return(res)

def anti_key_gen(key, alphabet):	#читаем мультипликативную инверсию матрицы ключа по модулю длины алфавита
	det = np.linalg.det(key)
	key_inv = np.linalg.inv(key)
	key_plus = key_inv * det
	det_mod = Euclid(int(det),len(alphabet))[0] % len(alphabet)
	key_plus_mod = key_plus * det_mod
	key_inv_mod = key_plus_mod % len(alphabet)
	#print("key_inv_mod: ", key_inv_mod)
	return(key_inv_mod)

while True:
	try:
		#make_dict(alphabet)
		row = input("Введите слово для шифрования: ")
		key_type = input("Введите 0 для ввода своего ключа или 1 для генерирования случайного: ")
		#print(type(key_type))

		if key_type == '1':
			c_row_code = row_code(row, alphabet)
			key = rand_key_gen(row, alphabet)
			#key = np.array([[6,24,1],[13,16,10],[20,17,15]])		#проверка при фиксированном, а не генерированном случайном ключе
			crypt_result = np.dot(key,c_row_code) #% len(alphabet)
			#print("crypt_result", crypt_result)
			code_result = row_decode(crypt_result,alphabet)
			print("Результат шифрования",code_result)
		elif key_type == '0':
			c_row_code = row_code(row, alphabet)
			key = user_key(alphabet)
			#key = np.array([[6,24,1],[13,16,10],[20,17,15]])		#проверка при фиксированном, а не генерированном случайном ключе
			crypt_result = np.dot(key,c_row_code) % len(alphabet)
			#print("crypt_result", crypt_result)
			code_result = row_decode(crypt_result,alphabet)
			print("Результат шифрования",code_result)
		else:
			print("Неправильный параметр, попробуйте снова")

		d_row = input("Введите слово для расшифрования: ")
		d_row_code = row_code(d_row, alphabet)
		anti_key = anti_key_gen(key, alphabet)
		d_crypt_result = np.dot(anti_key,d_row_code) % len(alphabet)
		print("Результат расшифрования: ", row_decode(d_crypt_result, alphabet))
	except(RuntimeError, TypeError, NameError):
		continue
