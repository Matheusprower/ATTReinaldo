_varNotaTotal = 0
Lista_Alunos = []

for i in range(3):
    _varNomeAluno = input(f"Digite o nome do {i + 1}º aluno: ")
    _varNotaAluno = input(f"Digite a nota do {i + 1}º aluno: ")
    Dic_Aluno = {"Nome": _varNomeAluno, "Nota": _varNotaAluno}
    Lista_Alunos.append(Dic_Aluno)

for i in Lista_Alunos:
    _varNotaTotal += float(i["Nota"])

_varMediaNotas = _varNotaTotal / len(Lista_Alunos)
print(f"A média das notas recebidas foi: {_varMediaNotas}")
_varMaiorNota = max(i["Nota"] for i in Lista_Alunos)
_varMenorNota = min(i["Nota"] for i in Lista_Alunos)
print(f"A maior nota foi {_varMaiorNota}.\nAlunos com menores notas:")

for i in Lista_Alunos:
    if i["Nota"] == _varMaiorNota:
        print(i["Nome"])

print(f"A menor nota foi {_varMenorNota}.\nAlunos com menores notas:")

for i in Lista_Alunos:
    if i["Nota"] == _varMenorNota:
        print(i["Nome"])

print("Alunos abaixo da média:")

for i in Lista_Alunos:
    if float(i["Nota"]) < _varMediaNotas:
        print(f"{i["Nome"]}, {i["Nota"]}")

print("Alunos acima da média:")

for i in Lista_Alunos:
    if float(i["Nota"]) >= _varMediaNotas:
        print(f"{i["Nome"]}, {i["Nota"]}")
