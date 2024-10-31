alunos = {'Ana': 8.5, 'Pedro': 6.0, 'Maria': 7.5, 'José': 5.5}
resultado = {"Aprovado": [], "Reprovado": []}
for nome, nota in alunos.items():
    if nota >= 7:
        resultado['Aprovado'].append(nome)
    else:
        resultado['Reprovado'].append(nome)
print(resultado)