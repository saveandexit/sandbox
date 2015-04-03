intlist = []
import random
while len(intlist)<9:
  num = random.randint(1,10)
  if num not in intlist:
    intlist.append(num)              # 1. Создание списка целых чисел

n = 1
while len(intlist)>n:
	for i in range(len(intlist)-n):
		if intlist[i]>intlist[i+1]:
			intlist[i],intlist[i+1]=intlist[i+1],intlist[i]   #2. Сортировка методом пузырька
	n+=1
