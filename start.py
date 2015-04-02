intlist = []
import random
while len(intlist)<9:
  num = random.randint(1,10)
  if num not in intlist:
    intlist.append(num)              # 1. Создание списка целых чисел

