# ===============================
# BANCO DIGITAL EM PYTHON
# Projeto para Portfólio - GitHub
# ===============================

# Usuário de demonstração
usuarios = [
    {
        "nome": "Irineu",
        "cpf": "12345678910"
    }
]

# Conta de demonstração
contas = [
    {
        "numero": 1,
        "usuario": usuarios[0],
        "saldo": 1000.00,
        "extrato": "",
        "saques": 0
    }
]


def localizar_conta(numero):
    for conta in contas:
        if conta["numero"] == numero:
            return conta
    return None


def criar_usuario():
    cpf = input("Digite o CPF: ")

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Usuário já cadastrado!")
            return

    nome = input("Digite o nome do usuário: ")

    usuarios.append({
        "nome": nome,
        "cpf": cpf
    })

    print("Usuário criado com sucesso!")


def criar_conta():
    cpf = input("Informe o CPF do usuário: ")

    usuario = None

    for item in usuarios:
        if item["cpf"] == cpf:
            usuario = item
            break

    if usuario:
        numero_conta = len(contas) + 1

        contas.append({
            "numero": numero_conta,
            "usuario": usuario,
            "saldo": 0.0,
            "extrato": "",
            "saques": 0
        })

        print(f"Conta criada com sucesso!")
        print(f"Número da conta: {numero_conta}")

    else:
        print("Usuário não encontrado!")


def depositar():
    numero = int(input("Número da conta: "))
    conta = localizar_conta(numero)

    if conta:
        valor = float(input("Valor do depósito: R$ "))

        if valor > 0:
            conta["saldo"] += valor
            conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"

            print("Depósito realizado com sucesso!")

        else:
            print("Valor inválido!")
    else:
        print("Conta não encontrada!")


def sacar():
    numero = int(input("Número da conta: "))
    conta = localizar_conta(numero)

    if conta:
        valor = float(input("Valor do saque: R$ "))

        if valor > conta["saldo"]:
            print("Saldo insuficiente!")

        elif valor > 500:
            print("O limite por saque é de R$ 500,00.")

        elif conta["saques"] >= 3:
            print("Limite diário de saques atingido!")

        elif valor > 0:
            conta["saldo"] -= valor
            conta["saques"] += 1

            conta["extrato"] += (
                f"Saque: R$ {valor:.2f}\n"
            )

            print("Saque realizado com sucesso!")

        else:
            print("Valor inválido!")
    else:
        print("Conta não encontrada!")


def transferir():
    origem = int(input("Conta de origem: "))
    destino = int(input("Conta de destino: "))
    valor = float(input("Valor da transferência: R$ "))

    conta_origem = localizar_conta(origem)
    conta_destino = localizar_conta(destino)

    if conta_origem and conta_destino:

        if valor <= conta_origem["saldo"]:

            conta_origem["saldo"] -= valor
            conta_destino["saldo"] += valor

            conta_origem["extrato"] += (
                f"Transferência enviada: R$ {valor:.2f}\n"
            )

            conta_destino["extrato"] += (
                f"Transferência recebida: R$ {valor:.2f}\n"
            )

            print("Transferência realizada com sucesso!")

        else:
            print("Saldo insuficiente!")

    else:
        print("Conta não encontrada!")


def mostrar_extrato():

    numero = int(input("Número da conta: "))
    conta = localizar_conta(numero)

    if conta:

        print("\n========== EXTRATO ==========")
        print(f"Titular: {conta['usuario']['nome']}")
        print(f"CPF: {conta['usuario']['cpf']}")
        print()

        if conta["extrato"] == "":
            print("Nenhuma movimentação realizada.")
        else:
            print(conta["extrato"])

        print(f"Saldo atual: R$ {conta['saldo']:.2f}")
        print("============================")

    else:
        print("Conta não encontrada!")


def listar_contas():

    print("\n====== CONTAS CADASTRADAS ======")

    for conta in contas:

        print(f"""
Conta: {conta["numero"]}
Titular: {conta["usuario"]["nome"]}
CPF: {conta["usuario"]["cpf"]}
Saldo: R$ {conta["saldo"]:.2f}
--------------------------------
""")


# Programa principal
while True:

    print("""
===================================
        BANCO DIGITAL PYTHON
===================================

Usuário para testes:

Nome: Irineu
CPF: 12345678910
Conta: 1
Saldo Inicial: R$ 1.000,00

-----------------------------------

1 - Criar Usuário
2 - Criar Conta
3 - Depositar
4 - Sacar
5 - Transferir
6 - Extrato
7 - Listar Contas
0 - Sair

===================================
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_usuario()

    elif opcao == "2":
        criar_conta()

    elif opcao == "3":
        depositar()

    elif opcao == "4":
        sacar()

    elif opcao == "5":
        transferir()

    elif opcao == "6":
        mostrar_extrato()

    elif opcao == "7":
        listar_contas()

    elif opcao == "0":
        print("Obrigado por utilizar o Banco Digital Python!")
        break

    else:
        print("Opção inválida!")