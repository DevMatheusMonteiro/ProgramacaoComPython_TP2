def entrarNomeFruta():
    while(True):
        nome = input("Entre com o nome da fruta (digite \"fim\" para encerrar): ")
        if(nome.strip() == ""):
            print("Erro: nome inválido!")
        else:
            return nome

def entrarQuantidadeFruta():
    while(True):
        try:
            quantidade = int(input("Entre com a quantidade da fruta (digite \"0\" para encerrar: )"))
            return quantidade
        except:
            print("Erro: número inválido!")

def criarListaFrutas():
    frutas = []
    nome = entrarNomeFruta()
    FIM = "fim"
    while(nome.lower() != FIM):
        frutas.append(nome)
        nome = entrarNomeFruta()
    return frutas

def criarListaQuantidades():
    quantidades = []
    quantidade = entrarQuantidadeFruta()
    FIM = 0
    while(quantidade != FIM):
        quantidades.append(quantidade)
        quantidade = entrarQuantidadeFruta()
    return quantidades

def criarListas():
    frutas = criarListaFrutas()
    quantidades = criarListaQuantidades()
    
    if(len(frutas) > len(quantidades)):
        print(f"O número de frutas ({len(frutas)}) é maior que quantidades ({len(quantidades)})\nRefaça a lista de quantidades")
        quantidades = criarListaQuantidades()
    return (frutas, quantidades)

(frutas,quantidades) = criarListas()
print(frutas)
print(quantidades)





