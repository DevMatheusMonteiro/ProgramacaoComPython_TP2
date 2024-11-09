def lerTexto():
    while True:
        texto = input("Entre com o texto: ")
        if texto.strip() == "":
            print("Erro: texto não pode ser nulo ou vazio")
        else:
            return texto
def exibirTexto():
    texto = lerTexto()
    print(texto)
exibirTexto()