lista = [4, 1, 5, 2, 3, 2, 4, 4]
dicionario = {}
for num in lista:
    dicionario[num] = lista.count(num)
print(dicionario)
