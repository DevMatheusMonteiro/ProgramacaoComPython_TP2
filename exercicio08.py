import random
aleatorio = random.randint(1,20)
print("***Tente adivinhar o número mágico***")
acerto = False
for i in range(4):
    num = int(input(f"Tentativa {i + 1}: "))
    if(num < aleatorio):
        print("Tente um número maior")
    elif(num > aleatorio):
        print("Tente um número menor")
    else:
        print("Parabéns, acertou!")
        acerto = True
        break
    if i == 2:
        print("Essa é a última tentativa!!")

if not acerto:
    print(f"Que pena, não foi dessa vez, o número mágico era {aleatorio}")