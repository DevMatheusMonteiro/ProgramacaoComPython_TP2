turma = [
            {"nome": "Ana", "nota": 5},
            {"nome": "Julia", "nota": 6},
            {"nome": "Joana", "nota": 7},
            {"nome": "Maria", "nota": 9},
            {"nome": "Sabrina", "nota": 10},
        ]

for i in range(len(turma)):
    if(i < (len(turma) - 1)):   
        temp = turma[i]
        diferenca = turma[i].get('nota') < turma[i+1].get('nota')
        if turma[i].get('nota') < turma[i+1].get('nota'):
            turma[i] = turma[i+1]
            turma[i+1] = temp
        elif turma[i].get('nota') > turma[i+1].get('nota'):
            turma[i] = turma[i+1]
            turma[i+1] = temp
        else:
            continue

for i in turma:
    print(i)
