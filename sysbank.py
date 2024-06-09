def main():
    saldo = 0
    extrato = []
    saques_diarios = 0
    limite_saques_diarios = 3
    limite_saque = 500.00
    
    while True:
        print("\n--- MENU ---")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            valor = float(input("Digite o valor para depósito: R$ "))
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: +R$ {valor:.2f}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Valor de depósito inválido.")
        
        elif opcao == '2':
            if saques_diarios >= limite_saques_diarios:
                print("Limite diário de saques atingido. Não é possível realizar mais saques hoje.")
            else:
                valor = float(input("Digite o valor para saque: R$ "))
                if valor > saldo:
                    print("Saldo insuficiente para realizar o saque.")
                elif valor > limite_saque:
                    print(f"Valor do saque excede o limite máximo de R$ {limite_saque:.2f} por saque.")
                elif valor > 0:
                    saldo -= valor
                    extrato.append(f"Saque: -R$ {valor:.2f}")
                    saques_diarios += 1
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                else:
                    print("Valor de saque inválido.")
        
        elif opcao == '3':
            print("\n--- EXTRATO ---")
            if not extrato:
                print("Nenhuma transação realizada.")
            else:
                for transacao in extrato:
                    print(transacao)
            print(f"Saldo atual: R$ {saldo:.2f}")
        
        elif opcao == '0':
            print("Saindo do sistema. Até mais!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
