def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

numeros = [3, 7, 12, 19, 25]
print("Lista de números:", numeros)
alvo = int(input("Digite o número que deseja buscar: "))

indice = busca_linear(numeros, alvo)
if indice != -1:
    print(f"Número encontrado na posição {indice}.")
else:
    print("Número não encontrado na lista.")
