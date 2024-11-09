def receberNomeEIdade(nome, idade,cidade=None):
    if cidade == None:
        print(f"{nome} tem {idade} anos e sua cidade é desconhecida.")
        return
    print(f"{nome} tem {idade} anos e sua cidade é {cidade}.")

receberNomeEIdade("Matheus", 24, "Rio de Janeiro")
receberNomeEIdade("Matheus", 24)