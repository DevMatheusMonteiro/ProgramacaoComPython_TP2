palavra = input("Entre com a frase: ").split(" ")
palavra = "".join(palavra)
print("É palíndromo" if palavra.lower() == palavra[::-1].lower() else "Não é palíndromo")