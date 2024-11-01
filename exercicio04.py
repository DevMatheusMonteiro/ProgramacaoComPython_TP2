def verificarSubconjunto(dicionario1, dicionario2):
    subconjunto = True
    if(len(dicionario1) > len(dicionario2)):
        for c in dicionario2.keys():
            if(dicionario2.get(c) != dicionario1.get(c)):
                subconjunto = False
                break
        print("Segundo dicionário é subconjunto do primeiro" if subconjunto else "Segundo dicionário não é subconjunto do primeiro")
    elif (len(dicionario1) < len(dicionario2)):
        for c in dicionario1.keys():
            if(dicionario1.get(c) != dicionario2.get(c)):
                subconjunto = False
                break
        print("Primeiro dicionário é subconjunto do segundo" if subconjunto else "Primeiro dicionário não é subconjunto do segundo")
    else:
        for c in dicionario1.keys():
            if(dicionario1.get(c) != dicionario2.get(c)):
                subconjunto = False
                break
        print("São iguais" if subconjunto else "São diferentes")

idades = {'Alice': 22, 'Bob': 17, 'Carol': 19, 'David': 16, "José": 4, "Joana": 7}
adultos = {'Alice': 22, 'Carol': 19, "José": 4}
verificarSubconjunto(adultos, idades)