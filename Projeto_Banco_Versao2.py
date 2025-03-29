def deposito (valor, saldo, extrato):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
            print("\nDepósito realizado com sucesso!")
            return saldo, extrato
    else:    
            print("Valor inválido para depósito. Tente novamente")  
           
def menu ():
    menu = """
Escolha a opção desejada:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Cliente
[5] Abrir Conta
[6] Listar Contas
[7] Sair

=> """
    return menu

def saque (valor, saldo, limite, extrato, numero_saque, limite_saque):
    if valor > saldo:
            print(f"Operação falhou! Saldo insuficiente. Seu saldo atual é de: R$ {saldo: .2f}")  
           
    elif valor > limite:
            print("Operação falhou! Valor excedeu o limite de saque")
         
    elif numero_saque >= limite_saque:
            print("Operação falhou! Você excedeu a quantidade de saques")  
       
    elif valor > 0:
            saldo -= valor
            numero_saque += 1
            extrato += f"Saque: R$ {valor: .2f}\n"
            print("\nSaque efetuado com sucesso!")  
       
    else:
            print("Operação falhou! Valor digitado invalido.")
    return saldo, extrato, numero_saque

def extratof (saldo, extrato):
    if extrato != "":
            print("\n========EXTRATO========\n")
            print(extrato)
            print(f"\nSaldo: R$ {saldo: .2F}")
            print("=======================")
    else:
            print("Você não possui transações para serem visualizadas")
           
def  procurar_usuario (cpf, clientes):
    for cliente in clientes:
        if cliente["CPF"] == cpf:  
            return cliente  
       
def cadastrar_cliente (clientes):
    cpf = int(input("Digite seu CPF (somente número): "))
    cliente = procurar_usuario(cpf, clientes)
    if cliente:
        print(f"\nCliente já cadastrado!")
        return
       
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereço = input("Digite o endereço (logradouro, nro - bairo - cidade/UF): ")
   
    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "CPF": cpf, "endereço": endereço})
    print("\nCliente cadastrado com sucesso!")
    return clientes

def cadastrar_conta(AGENCIA, contas, clientes, num_conta):
    cpf = int(input("Digite seu CPF (somente número): "))
    cliente = procurar_usuario(cpf, clientes)
    if cliente:
          num_conta += 1
          nome_cliente = cliente["nome"]
          contas.append({"Agencia": AGENCIA, "Conta": num_conta, "Cliente": nome_cliente })
    else:
        print("Cliente não cadastrado!")
    return contas, num_conta
   
def listar_conta(contas):
    for conta in contas:
        linha = f"""
==============================================

            Agencia: {conta["Agencia"]}
            C/C:     {conta["Conta"]}
            Titular: {conta["Cliente"]}
"""
        print(linha)
        
def main():
        AGENCIA = "0001"
        saldo = 0
        limite = 500
        extrato = ""
        numero_saque = 0
        limite_saque = 3
        clientes = []
        contas = []
        num_conta = 0
        
        while True:
                opcao = input(menu())
                if opcao == "1":
                        valor = float(input("Digite o valor que deseja depositar: "))
                        saldo, extrato = deposito(valor, saldo, extrato)
       
                elif opcao == "2":
                        valor = float(input("Digite o valor que deseja sacar: "))
                        saldo, extrato, numero_saque = saque(valor, saldo, limite, extrato, numero_saque, limite_saque)
       
                elif opcao == "3":
                        extratof(saldo, extrato)
       
                elif opcao == "4":
                        cadastrar_cliente(clientes)
           
                elif opcao == "5":
                        contas, num_conta = cadastrar_conta(AGENCIA, contas, clientes, num_conta)
       
                elif opcao == "6":
                        listar_conta(contas)
           
                elif opcao == "7":
                        break
                else:
                        print("Operação invalida! Por favor, selecione novamente a opção desejada")

main()
       