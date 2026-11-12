
veiculos = []
clientes = []
locacoes = []


def cadastrar_carro():
    placa = input("Placa: ").upper()

    for v in veiculos:
        if v["placa"] == placa:
            print("Placa já cadastrada!")
            return

    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    portas = int(input("Número de portas: "))
    ar = input("Tem ar-condicionado? (S/N): ").upper()
    diaria = float(input("Valor da diária: R$ ").replace(",", "."))

    carro = {
        "id": len(veiculos) + 1,
        "tipo": "carro",
        "placa": placa,
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "portas": portas,
        "ar": ar,
        "diaria": diaria,
        "status": "DISPONIVEL"
    }

    veiculos.append(carro)
    print("Carro cadastrado!")


def cadastrar_moto():
    placa = input("Placa: ").upper()

    for v in veiculos:
        if v["placa"] == placa:
            print("Placa já cadastrada!")
            return

    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    cilindradas = int(input("Cilindradas: "))
    diaria = float(input("Valor da diária: R$ ").replace(",", "."))

    moto = {
        "id": len(veiculos) + 1,
        "tipo": "moto",
        "placa": placa,
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "cilindradas": cilindradas,
        "diaria": diaria,
        "status": "DISPONIVEL"
    }

    veiculos.append(moto)
    print("Moto cadastrada!")


def listar_veiculos():
    if len(veiculos) == 0:
        print("Nenhum veículo cadastrado.")
        return

    for v in veiculos:
        print("\nID:", v["id"])
        print("Veículo:", v["marca"], v["modelo"])
        print("Ano:", v["ano"])
        print("Placa:", v["placa"])
        print("Diária: R$", v["diaria"])
        print("Status:", v["status"])

        if v["tipo"] == "carro":
            print("Portas:", v["portas"])
            print("Ar-condicionado:", v["ar"])
        else:
            print("Cilindradas:", v["cilindradas"])


def listar_disponiveis():
    encontrou = False

    for v in veiculos:
        if v["status"] == "DISPONIVEL":
            print("\nID:", v["id"])
            print(v["marca"], v["modelo"])
            print("Placa:", v["placa"])
            print("Diária: R$", v["diaria"])
            encontrou = True

    if encontrou == False:
        print("Nenhum veículo disponível.")


def cadastrar_cliente():
    cpf = input("CPF: ")

    for c in clientes:
        if c["cpf"] == cpf:
            print("CPF já cadastrado!")
            return

    nome = input("Nome: ")
    cnh = input("CNH: ")
    telefone = input("Telefone: ")

    cliente = {
        "id": len(clientes) + 1,
        "nome": nome,
        "cpf": cpf,
        "cnh": cnh,
        "telefone": telefone
    }

    clientes.append(cliente)
    print("Cliente cadastrado!")


def listar_clientes():
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return

    for c in clientes:
        print("\nID:", c["id"])
        print("Nome:", c["nome"])
        print("CPF:", c["cpf"])
        print("CNH:", c["cnh"])
        print("Telefone:", c["telefone"])


def calcular_aluguel(veiculo, dias):
    valor = veiculo["diaria"] * dias

    if veiculo["tipo"] == "carro":
        if veiculo["ar"] == "S":
            valor = valor + (15 * dias)

    if veiculo["tipo"] == "moto":
        if veiculo["cilindradas"] > 500:
            valor = valor + (valor * 0.10)

    return valor


def realizar_locacao():
    cpf = input("CPF do cliente: ")
    cliente = None

    for c in clientes:
        if c["cpf"] == cpf:
            cliente = c

    if cliente == None:
        print("Cliente não encontrado!")
        return

    placa = input("Placa do veículo: ").upper()
    veiculo = None

    for v in veiculos:
        if v["placa"] == placa:
            veiculo = v

    if veiculo == None:
        print("Veículo não encontrado!")
        return

    if veiculo["status"] == "ALUGADO":
        print("Veículo não disponível!")
        return

    dias = int(input("Dias previstos de aluguel: "))
    valor = calcular_aluguel(veiculo, dias)

    locacao = {
        "id": len(locacoes) + 1,
        "cliente": cliente,
        "veiculo": veiculo,
        "dias_previstos": dias,
        "dias_efetivos": 0,
        "valor_total": valor,
        "status": "ATIVA"
    }

    locacoes.append(locacao)
    veiculo["status"] = "ALUGADO"

    print("Locação realizada!")
    print("ID da locação:", locacao["id"])
    print("Valor previsto: R$", valor)


def listar_locacoes():
    encontrou = False

    for l in locacoes:
        if l["status"] == "ATIVA":
            print("\nLocação:", l["id"])
            print("Cliente:", l["cliente"]["nome"])
            print("Veículo:", l["veiculo"]["modelo"])
            print("Placa:", l["veiculo"]["placa"])
            print("Dias previstos:", l["dias_previstos"])
            print("Valor previsto: R$", l["valor_total"])
            encontrou = True

    if encontrou == False:
        print("Nenhuma locação ativa.")


def devolver_veiculo():
    id_locacao = int(input("ID da locação: "))
    locacao = None

    for l in locacoes:
        if l["id"] == id_locacao:
            locacao = l

    if locacao == None:
        print("Locação não encontrada!")
        return

    if locacao["status"] == "FINALIZADA":
        print("Locação já finalizada!")
        return

    dias = int(input("Dias efetivos de aluguel: "))

    veiculo = locacao["veiculo"]

    extras = dias - locacao["dias_previstos"]

    if extras < 0:
        extras = 0

    multa = extras * veiculo["diaria"] * 1.5

    valor = calcular_aluguel(veiculo, dias)
    total = valor + multa

    locacao["dias_efetivos"] = dias
    locacao["valor_total"] = total
    locacao["status"] = "FINALIZADA"

    veiculo["status"] = "DISPONIVEL"

    print("Devolução realizada!")
    print("Multa: R$", multa)
    print("Valor total: R$", total)


def main():
    opcao = -1

    while opcao != 0:
        print("\n===== LOCADORA DE VEÍCULOS =====")
        print("1 - Cadastrar carro")
        print("2 - Cadastrar moto")
        print("3 - Listar veículos")
        print("4 - Listar veículos disponíveis")
        print("5 - Cadastrar cliente")
        print("6 - Listar clientes")
        print("7 - Realizar locação")
        print("8 - Devolver veículo")
        print("9 - Listar locações ativas")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_carro()

        elif opcao == 2:
            cadastrar_moto()

        elif opcao == 3:
            listar_veiculos()

        elif opcao == 4:
            listar_disponiveis()

        elif opcao == 5:
            cadastrar_cliente()

        elif opcao == 6:
            listar_clientes()

        elif opcao == 7:
            realizar_locacao()

        elif opcao == 8:
            devolver_veiculo()

        elif opcao == 9:
            listar_locacoes()

        elif opcao == 0:
            print("Programa encerrado.")

        else:
            print("Opção inválida!")


main()
