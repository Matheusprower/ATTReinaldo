# ----------------------------------------------------------
# Programa: Calculadora com operações básicas (usando soma e subtração)
#   Este programa realiza soma, subtração, multiplicação e potência
#   entre dois números inteiros, utilizando apenas as operações
#   de soma e subtração.
# ----------------------------------------------------------

def soma(a, b):
    """Retorna a soma entre a e b"""
    return a + b


def subtracao(a, b):
    """Retorna a subtração de b em relação a a"""
    return a - b


def multiplicacao(a, b):
    """Retorna o produto entre a e b, usando apenas soma"""
    resultado = 0
    negativo = False

    # Tratando o caso de multiplicação com número negativo
    if b < 0:
        b = -b
        negativo = True

    for _ in range(b):
        resultado = soma(resultado, a)

    if negativo:
        resultado = -resultado

    return resultado


def potencia(a, b):
    """Retorna a^b usando apenas multiplicação"""
    if b < 0:
        print("Potência negativa não é suportada.")
        return None

    resultado = 1
    for _ in range(b):
        resultado = multiplicacao(resultado, a)

    return resultado


def exibir_menu():
    """Exibe o menu de opções para o usuário"""
    print("\n=== MENU DE OPERAÇÕES ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Potência")
    print("===========================")


def main():
    print("=== CALCULADORA ACADÊMICA ===")
    try:
        a = int(input("Digite o primeiro número inteiro: "))
        b = int(input("Digite o segundo número inteiro: "))
    except ValueError:
        print("Erro: Digite apenas números inteiros!")
        return

    exibir_menu()
    try:
        opcao = int(input("Escolha a operação desejada: "))
    except ValueError:
        print("Opção inválida!")
        return

    if opcao == 1:
        print(f"Resultado: {soma(a, b)}")
    elif opcao == 2:
        print(f"Resultado: {subtracao(a, b)}")
    elif opcao == 3:
        print(f"Resultado: {multiplicacao(a, b)}")
    elif opcao == 4:
        resultado = potencia(a, b)
        if resultado is not None:
            print(f"Resultado: {resultado}")
    else:
        print("Opção inválida! Tente novamente.")


# Execução principal
if __name__ == "__main__":
    main()
