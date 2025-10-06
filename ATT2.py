numeros = []

print("Informe 10 números inteiros, a cada numero digitado pressione")

for i in range(10):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(num)

print("\nNúmeros informados:", numeros)

novo_num = int(input("\nDigite um número para verificar se está na lista: "))

if novo_num in numeros:
    posicoes = [i for i, n in enumerate(numeros) if n == novo_num]
    print(f"\nO número {novo_num} foi encontrado nas posições: {posicoes}")

else:
    print(f"\nO número {novo_num} não se encontra na lista.")
