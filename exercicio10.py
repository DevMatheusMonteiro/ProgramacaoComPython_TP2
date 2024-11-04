turma = [
            {"nome": "Ana", "nota": 10},
            {"nome": "Julia", "nota": 6},
            {"nome": "Joana", "nota": 2},
            {"nome": "Maria", "nota": 9},
            {"nome": "Sabrina", "nota": 10},
        ]
        
def ordenarPorNotaMaiorAMenor(turma):
    continua = True
    i = 0
    fim = len(turma)-1
    contadorMenorQueZero = 0
    while(continua):
        if i < fim:
            comparacao = turma[i].get('nota') - turma[i+1].get('nota')
            if comparacao < 0:
                contadorMenorQueZero+=1
                temp = turma[i+1]
                turma[i+1] = turma[i]
                turma[i] = temp
        elif i == fim:
            if contadorMenorQueZero == 0:
                continua = False
            else:
                i = -1
            contadorMenorQueZero = 0
        i+=1

def exibirTurma(turma):
    for i in turma:
        print(i)

exibirTurma(turma)
ordenarPorNotaMaiorAMenor(turma)
print()
exibirTurma(turma)