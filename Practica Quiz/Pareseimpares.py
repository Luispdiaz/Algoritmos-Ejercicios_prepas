from random import randrange


pares = []
impares=[]
aleatorios1 = []
for i in range(20):
    aleatorios = randrange(1,30)
    aleatorios1.append(aleatorios)
for i in aleatorios1:
    if i % 2==0:
        pares.append(i)
    else:
        impares.append(i)
print("Pares \n",*pares)
print("Impares \n",*impares)