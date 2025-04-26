clientes = {}

def criar():
    nome = input("Nome: ")
    clientes[nome] = 0

def depositar():
    nome = input("Nome: ")
    valor = float(input("Valor: "))
    if nome in clientes:
        clientes[nome] += valor
        print("Depositado")
    else:
        print("Cliente não existe")

def sacar():
    nome = input("Nome: ")
    valor = float(input("Valor: "))
    if nome in clientes:
        if clientes[nome] >= valor:
            clientes[nome] -= valor
            print("Sacado")
        else:
            print("Saldo insuficiente")
    else:
        print("Cliente não existe")

def saldo():
    for cliente in clientes:
        print(cliente, "->", clientes[cliente])

while True:
    print("1-Criar 2-Depositar 3-Sacar 4-Saldo 5-Sair")
    opcao = input("Opção: ")
    if opcao == "1":
        criar()
    elif opcao == "2":
        depositar()
    elif opcao == "3":
        sacar()
    elif opcao == "4":
        saldo()
    elif opcao == "5":
        break
