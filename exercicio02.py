tupla1 = (5,3,'a',3)
tupla2 = (3,'a',5,3)
diferente = False
if(len(tupla1) != len(tupla2)):
    diferente = True
else:
    for item in tupla1:
        if(tupla1.count(item) != tupla2.count(item)):
            diferente = True
            break
print("Diferente" if diferente else "Igual")