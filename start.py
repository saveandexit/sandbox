intlist = []
def fill(hhg):
	import random
	while len(hhg)<9:
		num = random.randint(0,9)  #1. Получение списка случайных целых
		if num not in hhg:
			hhg.append(num)
	return hhg
fill(intlist)

def swap(bfg,a,b):
	bfg[a],bfg[b]=bfg[b],bfg[a]
def bubble_swap(bfg):
	a = len(bfg)
	while a>1:
		for b in range(a-1):
			if bfg[b]>bfg[b+1]:
				swap(bfg,b,b+1)    #2. Сортировка методом пузырька
		a -= 1
bubble_swap(intlist)

def dictfill(bco):
	newdict = {}
	for index, value in enumerate(bco):       #3. Создание из списка словаря вида ключ-индекс
		newdict[value] = index
	return newdict
intdict = dictfill(intlist)
