import random
def entrarNomeFruta():
        return input("Entre com as frutas separadas por vírgula: ")

def entrarQuantidadeFruta():
        return input("Entre com as quantidades separadas por vírgula: ")
        

def criarListaFrutas():
    erro = True
    while(erro):
        listaNomes = entrarNomeFruta()
        frutas = listaNomes.split(",")
        for i in range(len(frutas)):
            nome = frutas[i].strip()
            if(nome == ""):
                print("Erro: campo nome vazio! Refaça a lista.")
                break
            if (i == len(frutas)-1):
                 erro = False
            frutas[i] = nome
    return frutas


def criarListaQuantidades():
    erro = True
    while(erro):
        listaQuantidades = entrarQuantidadeFruta()
        quantidades = listaQuantidades.split(",")
        for i in range(len(quantidades)):
            try: 
                quantidade = int(quantidades[i].strip())
                if (i == len(quantidades)-1):
                    erro = False
                quantidades[i] = quantidade
            except:
                 print("Erro: número inválido! Refaça a lista")
                 break
    return quantidades

def criarListas():
    frutas = criarListaFrutas()
    quantidades = criarListaQuantidades()
    
    if(len(frutas) > len(quantidades)):
        print(f"O número de frutas ({len(frutas)}) é maior que quantidades ({len(quantidades)})\nRefaça a lista de quantidades")
        quantidades = criarListaQuantidades()
    return (frutas, quantidades)

def sortearFruta(frutas,quantidades):
    aleatorio = random.randint(0, (len(frutas)-1))
    quantidades[aleatorio] -= 1
    return frutas[aleatorio]

(frutas,quantidades) = criarListas()
frutaSorteada = sortearFruta(frutas, quantidades)
print(f"A fruta sorteada é: {frutaSorteada}")