def entrarNome():
    nome = ""
    while(True):
        nome = input("Entre com o nome do aluno (digite 'fim' para encerrar): ")
        if len(nome.strip()) == 0:
            print("Nome não pode ser vazio!")
        else:
            break
    return nome

def entrarNota(msg):
    nota = 0
    while(True):
        try:
            nota = float(input(msg))
            if (nota < 0 or nota > 10):
                print("Nota deve ser de 0 a 10!")
            else:
                break
        except:
            print("Nota inválida")
    return nota

def criarTurma():
    FIM = 'fim'
    turma = []
    nome = entrarNome()
    while(nome.lower() != 'fim'):
        nota1 = entrarNota("Entre com a nota 1: ")
        nota2 = entrarNota("Entre com a nota 2: ")
        turma.append([nome,nota1,nota2])
        nome = entrarNome()
    return turma

def exibirTurma(turma):
    for aluno in turma:
        print(f"Nome: {aluno[0]}\nNota 1: {aluno[1]}\nNota 2: {aluno[2]}\n")

turma = criarTurma()
exibirTurma(turma)
    
