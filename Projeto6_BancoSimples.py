
# Projeto 6: Banco Simples
clientes = {}

def criar():
    n = input("Nome: ")
    clientes[n] = 0

def depositar():
    n = input("Nome: ")
    v = float(input("Valor: "))
    if n in clientes:
        clientes[n] += v
        print("Depositado")
    else:
        print("Cliente não existe")

def sacar():
    n = input("Nome: ")
    v = float(input("Valor: "))
    if n in clientes:
        if clientes[n] >= v:
            clientes[n] -= v
            print("Sacado")
        else:
            print("Saldo insuficiente")
    else:
        print("Cliente não existe")

def saldo():
    for k in clientes:
        print(k, "->", clientes[k])

while True:
    print("1-Criar 2-Depositar 3-Sacar 4-Saldo 5-Sair")
    o = input("Opção: ")
    if o == "1":
        criar()
    elif o == "2":
        depositar()
    elif o == "3":
        sacar()
    elif o == "4":
        saldo()
    elif o == "5":
        break
