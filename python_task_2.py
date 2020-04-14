import argparse
from random import sample

# функция генерации ключа
def gen_key(file):
	key = sample(range(256), 256)  # генерирация случайного ключа 
	with open(file, 'w') as f:  # запись ключа в файл
		f.write(str(key)[1 : -1])

# функция получения ключа
def get_key(file):
	with open(file, 'r') as f:
		key = f.read()
	return key.split(', ')  # считывание ключа и его привод к нужному формату

# функция шифрования
def encrypt(in_file, out_file, key_file):
	key = get_key(key_file)  # получение ключа из файла
	with open(in_file, 'r') as f:
		x = f.read()[0 : -1].split(' ')
	x = [key[int(i)] for i in x]  # шифрование сообщения
	with open(out_file, 'w') as f:
		f.write(str(x)[1 : -1])  # запись зашифрованного сообщения
	
# функция расшифрования
def decrypt(in_file, out_file, key_file):
	key = get_key(key_file)  # получение ключа из файла
	key = {key[i] : i for i in range(256)}  # создание словаря для расширования сообщения
	with open(in_file, 'r') as f:
		x = f.read()[0 : -1].split(' ')
	x = [key[i] for i in x]  # расшифрование
	with open(out_file, 'w') as f:
		f.write(str(x)[1 : -1])  # запись расшифрованного сообщения

# функция взлома
def cipher_break(in_file, out_file, ciphertext):
	with open(in_file, 'r') as f:
		x = f.read()[0 : -1].split(' ')
	freq_table = [{i : 0 for i in range(256)}, {i : 0 for i in range(256)}] 
	for byte in x:
		freq_table[0][byte] += 1
	with open(ciphertext, 'r') as f:
		cipher = f.read()
	cipher = list(x)
	for byte in cipher:
		freq_table[1][byte] += 1


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("mode", choices = ['gen_key', 'encrypt', 'decrypt', 'cipher_break'])  # обязательный параметр - выбор режима
	parser.add_argument('-i')  # доп параметр - файл с сообщением 
	parser.add_argument('-o')  # доп параметр - закодированный, раскодированный файл
	parser.add_argument('-k')  # доп параметр - файл с ключом
	parser.add_argument('-c')  # доп параметр - файл с ключом
	args = parser.parse_args()
	# вызов нужного режима
	if args.mode == 'gen_key':
		gen_key(args.k)
	elif args.mode == 'encrypt':
		encrypt(args.i, args.o, args.k)
	elif args.mode == 'decrypt':
		decrypt(args.i, args.o, args.k)
	else:
		cipher_break(args.i, args.o, args.k)