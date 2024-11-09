def entrarNumero(texto):
    """ 
    # Função para receber um número e retorná-lo.
    ## Parâmetro
    - texto: recebe um texto quer serve como informativo para indicar ao usuário o que ele deve digitar.
    """
    while True:
        try:
            numero = float(input(texto))
            return numero
        except:
            print("Erro: número inválido.")
def dividir():
    """ 
    # Função para realizar a divisão entre dois números.
    Retorna uma tupla contendo o dividendo, divisor, quociente e resto
    """
    while True:
        dividendo = entrarNumero("Informe o dividendo:")
        divisor = entrarNumero("Informe o divisor:")
        if divisor == 0:
            print("Erro: divisor não pode ser 0.")
        else:
            quociente = int(dividendo / divisor)
            resto = int(dividendo % divisor)
            return(dividendo, divisor, quociente, resto)
def exibirResultadoDivisão(dividendo, divisor, quociente, resto):
    """
    # Função para exibir o resultado de uma divisão.
    ## Parâmetros
    - dividendo
    - divisor
    - quociente
    - resto
    """
    print(f"O quociente da divisão entre {dividendo} e {divisor} é {quociente} e o resto é {resto}.")
(dividendo, divisor, quociente, resto) = dividir()
exibirResultadoDivisão(dividendo, divisor, quociente, resto)