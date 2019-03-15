from random import randint

liste = []

for i in range (0, 100):
	number = randint(0, 1000)
	liste.append(number)

def isSorted(liste):
	laenge = len(liste) - 1
	for i in range (0, laenge):
		value1 = liste[i]
		value2 = liste[i + 1]
		if value1 > value2:
			return False
	return True

def bubblesort(liste):
	laenge = len(liste) - 1
	for i in range(0,laenge):
		value1 = liste[i]
		value2 = liste[i + 1]
		if value1 > value2:
			valuecurrent = liste[i]
			liste[i] = liste[i + 1]
			liste[i + 1] = valuecurrent

for i in range(0,100):
	print(str(liste[i]) + ", ")
print("Liste fertig :-)")
counter = 0
while not isSorted(liste):
#for t in range(0,100):
	bubblesort(liste)
	counter += 1

for i in range(0,100):
	print(str(liste[i]) + ", ")
print("Wir mussten " + str(counter) + " mal sortieren")
