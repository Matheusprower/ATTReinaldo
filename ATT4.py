MEGA SENA

print("Digite os 6 números sorteados na Mega Sena:")
numeros_sorteados = set()
while len(numeros_sorteados) < 6:
    try:
        numero = int(input(f"Digite o {len(numeros_sorteados) + 1}º número: "))
        if 1 <= numero <= 60:
            if numero in numeros_sorteados:
                print("Número repetido. Tente outro.")
            else:
                numeros_sorteados.add(numero)
        else:
            print("Digite um número entre 1 e 60.")
    except ValueError:
        print("Digite apenas números inteiros.")


print("\nDigite os 6 números do seu cartão:")
numeros_jogados = set()
while len(numeros_jogados) < 6:
    try:
        numero = int(input(f"Digite o {len(numeros_jogados) + 1}º número: "))
        if 1 <= numero <= 60:
            if numero in numeros_jogados:
                print("Número repetido. Tente outro.")
            else:
                numeros_jogados.add(numero)
        else:
            print("Digite um número entre 1 e 60.")
    except ValueError:
        print("Digite apenas números inteiros.")

acertos = numeros_sorteados.intersection(numeros_jogados)
print(f"\nVocê acertou {len(acertos)} número(s): {sorted(acertos)}")
