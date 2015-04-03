intlist = []
def fill(hhg):
	import random
	while len(hhg)<9:
		num = random.randint(0,9)
		if num not in hhg:
			hhg.append(num)
	return hhg
fill(intlist)

n = 1
while len(intlist)>n:
	for i in range(len(intlist)-n):
		if intlist[i]>intlist[i+1]:
			intlist[i],intlist[i+1]=intlist[i+1],intlist[i]   #2. Сортировка методом пузырька
	n+=1
