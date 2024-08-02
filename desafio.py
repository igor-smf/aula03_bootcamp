CONSTANTE_BUNUS = 1000

nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido is not True:
    nome = input("Digite o seu nome: ")

    if nome.isdigit():
        print("Você digitou seu nome errado.")
    elif len(nome) == 0:
        print("Você não digitou nada.")
    elif nome.isspace():
        print("Você digitou só espaço.")
    else:
        nome_valido = True

while salario_valido is not True:
    try:
        salario = float(input("Digite o seu salário: "))
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            salario_valido = True
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")

while bonus_valido is not True:
    try:
        bonus = float(input("Digite o seu bonus: "))
        if bonus < 0:
            print("Por favor, digite um valor positivo para o bonus.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")


valor_bonus = CONSTANTE_BUNUS + (salario * bonus)

print()
print(f"Olá {nome}, o seu valor bônus foi de {valor_bonus}")
