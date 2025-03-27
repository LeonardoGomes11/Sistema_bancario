menu = """
Escolha a opção desejada:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

# def deposito(valor):
    

while True:
    opcao = input(menu)
    if opcao == "1":
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito: .2f}\n"
        else:    
            print("Valor inválido para depósito. Tente novamente")  
              
    elif opcao == "2":
        valor_saque = float(input("Digite o valor que deseja sacar: ")) 
        if valor_saque > saldo:
            print("Operação falhou! Saldo insuficiente")   
            
        elif valor_saque > limite:
            print("Operação falhou! Valor excedeu o limite de saque") 
         
        elif numero_saque >= limite_saque:
            print("Operação falhou! Você excedeu a quantidade de saques")   
        
        elif valor_saque > 0:
            saldo -= valor_saque
            numero_saque += 1
            extrato += f"Saque: R$ {valor_saque: .2f}\n"    
        
        else:
            print("Operação falhou! Valor digitado invalido.") 
    elif opcao == "3":
        if extrato != "":
            print("\n========EXTRATO========\n")
            print(extrato)
            print(f"\nSaldo: R$ {saldo: .2F}")
            print("=======================")
        else:
            print("Você não possui transações para serem visualizadas")    
        
    elif opcao == "4":
        break
    else:
        print("Operação invalida! Por favor, selecione novamente a opção desejada")
        

