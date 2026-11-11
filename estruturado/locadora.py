veiculos = []
clientes = []
locacoes = []

def ler_inteiro(mensagem, minimo=0):
    while True:
        try:
            numero = int(input(mensagem))
            if numero < minimo:
                print(f"Digite um número maior ou igual a {minimo}.")
            else:
                return numero
        except ValueError:
            print("Digite um número inteiro válido.")

def ler_valor_diaria():
    while True:
        try:
            valor = float(input("Valor da diária: R$ ").replace(",", "."))
            if valor <= 0:
                print("O valor da diária deve ser maior que zero.")
            else:
                return valor
        except ValueError:
            print("Digite um valor válido, por exemplo 120 ou 120,50.")

def ler_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta == "s" or resposta == "sim":
            return True
        if resposta == "n" or resposta == "nao" or resposta == "não":
            return False
        print("Responda com S para sim ou N para não.")

def buscar_veiculo_por_placa(placa):
    placa = placa.strip().upper()
    for veiculo in veiculos:
        if veiculo["placa"] == placa:
            return veiculo
    return None

def buscar_cliente_por_cpf(cpf):
    cpf = cpf.strip()
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return None

def cadastrar_carro():
    placa = input("Placa: ").strip().upper()
    if buscar_veiculo_por_placa(placa) is not None:
        print("Erro: já existe um veículo com essa placa.")
        return
    
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()
    ano = ler_inteiro("Ano: ", 1)
    numero_portas = ler_inteiro("Número de portas: ", 1)
    ar_condicionado = ler_sim_nao("Tem ar-condicionado? (S/N): ")
    valor_diaria = ler_valor_diaria()

    carro = {
        "id": len(veiculos) + 1,
        "tipo": "carro",
        "placa": placa,
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "valor_diaria": valor_diaria,
        "numero_portas": numero_portas,
        "ar_condicionado": ar_condicionado,
        "status": "DISPONIVEL"
    }
    veiculos.append(carro)
    print("Carro cadastrado com sucesso!")

def cadastrar_moto():
    placa = input("Placa: ").strip().upper()
    if buscar_veiculo_por_placa(placa) is not None:
        print("Erro: já existe um veículo com essa placa.")
        return

    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()
    ano = ler_inteiro("Ano: ", 1)
    cilindradas = ler_inteiro("Cilindradas: ", 1)
    valor_diaria = ler_valor_diaria()

    moto = {
        "id": len(veiculos) + 1,
        "tipo": "moto",
        "placa": placa,
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "valor_diaria": valor_diaria,
        "cilindradas": cilindradas,
        "status": "DISPONIVEL"
    }
    veiculos.append(moto)
    print("Moto cadastrada com sucesso!")

def exibir_veiculo(veiculo):
    print(
        f"ID {veiculo['id']} | {veiculo['marca']} {veiculo['modelo']} "
        f"({veiculo['ano']}) | Placa: {veiculo['placa']} | "
        f"Diária: R$ {veiculo['valor_diaria']:.2f} | "
        f"Status: {veiculo['status']}"
    )
    if veiculo["tipo"] == "carro":
        if veiculo["ar_condicionado"]:
            ar = "Sim"
        else:
            ar = "Não"
        print(f"   Carro | Portas: {veiculo['numero_portas']} | Ar-condicionado: {ar}")
    else:
        print(f"   Moto | Cilindradas: {veiculo['cilindradas']} cc")

def listar_veiculos(apenas_disponiveis=False):
    encontrou = False
    for veiculo in veiculos:
        if apenas_disponiveis and veiculo["status"] != "DISPONIVEL":
            continue
        exibir_veiculo(veiculo)
        encontrou = True

    if not encontrou:
        if apenas_disponiveis:
            print("Nenhum veículo disponível.")
        else:
            print("Nenhum veículo cadastrado.")

def cadastrar_cliente():
    cpf = input("CPF: ").strip()
    if buscar_cliente_por_cpf(cpf) is not None:
        print("Erro: já existe um cliente com esse CPF.")
        return

    nome = input("Nome: ").strip()
    cnh = input("CNH: ").strip()
    telefone = input("Telefone: ").strip()

    cliente = {
        "id": len(clientes) + 1,
        "nome": nome,
        "cpf": cpf,
        "cnh": cnh,
        "telefone": telefone
    }
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:
        print(
            f"ID {cliente['id']} | {cliente['nome']} | CPF: {cliente['cpf']} | "
            f"CNH: {cliente['cnh']} | Telefone: {cliente['telefone']}"
        )

def calcular_valor_aluguel(veiculo, dias):
    valor = veiculo["valor_diaria"] * dias

    if veiculo["tipo"] == "carro" and veiculo["ar_condicionado"]:
        valor = valor + (15.0 * dias)
    elif veiculo["tipo"] == "moto" and veiculo["cilindradas"] > 500:
        valor = valor * 1.10

    return valor

def realizar_locacao():
    cpf = input("CPF do cliente: ").strip()
    cliente = buscar_cliente_por_cpf(cpf)
    if cliente is None:
        print("Erro: cliente não encontrado.")
        return

    placa = input("Placa do veículo: ").strip().upper()
    veiculo = buscar_veiculo_por_placa(placa)
    if veiculo is None:
        print("Erro: veículo não encontrado.")
        return

    if veiculo["status"] != "DISPONIVEL":
        print("Erro: veículo não está disponível.")
        return

    dias_previstos = ler_inteiro("Dias previstos de aluguel: ", 1)
    valor_previsto = calcular_valor_aluguel(veiculo, dias_previstos)

    locacao = {
        "id": len(locacoes) + 1,
        "cliente": cliente,
        "veiculo": veiculo,
        "dias_previstos": dias_previstos,
        "dias_efetivos": 0,
        "valor_total": valor_previsto,
        "status": "ATIVA"
    }
    locacoes.append(locacao)
    veiculo["status"] = "ALUGADO"

    print(f"Locação #{locacao['id']} realizada!")
    print(f"Valor previsto: R$ {valor_previsto:.2f}")

def listar_locacoes_ativas():
    encontrou = False
    for locacao in locacoes:
        if locacao["status"] == "ATIVA":
            cliente = locacao["cliente"]
            veiculo = locacao["veiculo"]
            print(
                f"Locação #{locacao['id']} | {cliente['nome']} | "
                f"{veiculo['marca']} {veiculo['modelo']} ({veiculo['placa']}) | "
                f"Dias previstos: {locacao['dias_previstos']} | "
                f"Valor previsto: R$ {locacao['valor_total']:.2f}"
            )
            encontrou = True

    if not encontrou:
        print("Nenhuma locação ativa.")

def devolver_veiculo():
    id_locacao = ler_inteiro("ID da locação: ", 1)
    locacao_encontrada = None

    for locacao in locacoes:
        if locacao["id"] == id_locacao:
            locacao_encontrada = locacao
            break

    if locacao_encontrada is None:
        print("Erro: locação não encontrada.")
        return

    if locacao_encontrada["status"] != "ATIVA":
        print("Erro: essa locação já foi finalizada.")
        return

    dias_efetivos = ler_inteiro("Quantos dias o cliente ficou com o veículo? ", 1)
    dias_extras = dias_efetivos - locacao_encontrada["dias_previstos"]
    if dias_extras < 0:
        dias_extras = 0

    veiculo = locacao_encontrada["veiculo"]
    multa = dias_extras * veiculo["valor_diaria"] * 1.5
    valor_aluguel = calcular_valor_aluguel(veiculo, dias_efetivos)
    valor_total = valor_aluguel + multa

    locacao_encontrada["dias_efetivos"] = dias_efetivos
    locacao_encontrada["valor_total"] = valor_total
    locacao_encontrada["status"] = "FINALIZADA"
    veiculo["status"] = "DISPONIVEL"

    print(f"Devolução registrada! Multa: R$ {multa:.2f}")
    print(f"Valor total: R$ {valor_total:.2f}")

def exibir_menu():
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

def main():
    while True:
        exibir_menu()
        opcao = ler_inteiro("Escolha uma opção: ", 0)

        if opcao == 1:
            cadastrar_carro()
        elif opcao == 2:
            cadastrar_moto()
        elif opcao == 3:
            listar_veiculos()
        elif opcao == 4:
            listar_veiculos(True)
        elif opcao == 5:
            cadastrar_cliente()
        elif opcao == 6:
            listar_clientes()
        elif opcao == 7:
            realizar_locacao()
        elif opcao == 8:
            devolver_veiculo()
        elif opcao == 9:
            listar_locacoes_ativas()
        elif opcao == 0:
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Escolha uma opção do menu.")

main()