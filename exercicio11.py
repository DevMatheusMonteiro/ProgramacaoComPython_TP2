turma = [
            {"nome": "Ana", "nota": 10},
            {"nome": "Julia", "nota": 6},
            {"nome": "Joana", "nota": 2},
            {"nome": "Maria", "nota": 9},
            {"nome": "Sabrina", "nota": 10},
        ]

def entrarIndice():
    while(True):
        try:
            indice = int(input("Entre com o indice: "))
            return indice
        except:
            print("Erro: número inválido")

def buscarElemento(lista):
    while(True):
        try:
            indice = entrarIndice()
            elemento = lista[indice]
            return elemento
        except:
            print("Erro: índice fora do intervalo da lista")

elemento = buscarElemento(turma)
print(elemento)