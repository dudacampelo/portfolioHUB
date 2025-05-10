print("Calculadora de Média")
notas = []
for i in range(3):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"Sua média é: {media:.2f}") 

Adiciona projeto de cálculo de média
