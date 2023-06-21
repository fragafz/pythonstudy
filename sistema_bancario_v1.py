menu = """"
BEM VINDO AO SNAKE BANK! V1.0
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Digite o valor desejado: "))

        if valor > 0:
            saldo += valor
            extrato += f"depósito: R$ {valor}\n"
            print(extrato)

    elif opcao == "2":
        valor = float(input("Digite o valor a ser sacado: "))


        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print("Limite excedido!")
        elif excedeu_saques:
            print("Limite de saque!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor}\n"
            print(extrato)
            numero_saques += 1

        else:
            print("Operação inválida!")

    elif opcao == "3":
        print(f"o seu saldo é: R${saldo}")

    elif opcao == "4":
        print("Obrigado por ser nosso cliente! \nVolte sempre!")
        break
    else:
        print("Operação inválida, por favor selecione novamente o operação desejada.")
