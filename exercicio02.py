tupla1 = (5,3,2)
tupla2 = (3,2,3)
diferente = False
if(len(tupla1) != len(tupla2)):
    diferente = True
else:
    for item in tupla1:
        if(item not in tupla2):
            diferente = True
            break
print("Diferente" if diferente else "Igual")