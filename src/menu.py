from cliente import Cliente
from veiculo import Carro, Moto


class Menu:

    def __init__(self, locadora):
        self._locadora = locadora

    def executar(self):
        opcao = -1
        while opcao != 0:
            self._exibir_menu_principal()
            opcao = self._ler_opcao()
            print()

            if opcao == 1:
                self._cadastrar_carro()
            elif opcao == 2:
                self._cadastrar_moto()
            elif opcao == 3:
                self._locadora.listar_veiculos()
            elif opcao == 4:
                self._locadora.listar_veiculos_disponiveis()
            elif opcao == 5:
                self._cadastrar_cliente()
            elif opcao == 6:
                self._locadora.listar_clientes()
            elif opcao == 7:
                self._realizar_locacao()
            elif opcao == 8:
                self._devolver_veiculo()
            elif opcao == 9:
                self._locadora.listar_locacoes_ativas()
            elif opcao == 0:
                print("Saindo... Até logo!")
            else:
                print("Opção inválida.")
            print()

    def _exibir_menu_principal(self):
        print("===== LOCADORA DE VEÍCULOS =====")
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

    # ---------- Ações do menu ----------

    def _cadastrar_carro(self):
        print("--- Cadastro de Carro ---")
        placa = self._ler_texto("Placa: ")
        marca = self._ler_texto("Marca: ")
        modelo = self._ler_texto("Modelo: ")
        ano = self._ler_int("Ano: ")
        diaria = self._ler_float("Valor da diária: ")
        portas = self._ler_int("Número de portas: ")
        ar = self._ler_sim_nao("Tem ar-condicionado? (s/n): ")

        carro = Carro(self._locadora.proximo_id_veiculo, placa, marca, modelo,
                      ano, diaria, portas, ar)
        self._locadora.cadastrar_veiculo(carro)

    def _cadastrar_moto(self):
        print("--- Cadastro de Moto ---")
        placa = self._ler_texto("Placa: ")
        marca = self._ler_texto("Marca: ")
        modelo = self._ler_texto("Modelo: ")
        ano = self._ler_int("Ano: ")
        diaria = self._ler_float("Valor da diária: ")
        cilindradas = self._ler_int("Cilindradas: ")

        moto = Moto(self._locadora.proximo_id_veiculo, placa, marca, modelo,
                    ano, diaria, cilindradas)
        self._locadora.cadastrar_veiculo(moto)

    def _cadastrar_cliente(self):
        print("--- Cadastro de Cliente ---")
        nome = self._ler_texto("Nome: ")
        cpf = self._ler_texto("CPF: ")
        cnh = self._ler_texto("CNH: ")
        telefone = self._ler_texto("Telefone: ")

        cliente = Cliente(self._locadora.proximo_id_cliente, nome, cpf, cnh, telefone)
        self._locadora.cadastrar_cliente(cliente)

    def _realizar_locacao(self):
        print("--- Nova Locação ---")
        cpf = self._ler_texto("CPF do cliente: ")
        placa = self._ler_texto("Placa do veículo: ")
        dias = self._ler_int("Quantidade de dias: ")
        self._locadora.realizar_locacao(cpf, placa, dias)

    def _devolver_veiculo(self):
        print("--- Devolução ---")
        self._locadora.listar_locacoes_ativas()
        id_locacao = self._ler_int("ID da locação: ")
        dias = self._ler_int("Dias efetivamente utilizados: ")
        self._locadora.devolver_veiculo(id_locacao, dias)

    # ---------- Leitura das entradas ----------

    def _ler_opcao(self):
        return self._ler_int("Escolha uma opção: ")

    def _ler_texto(self, msg):
        # fica perguntando até a pessoa digitar alguma coisa
        texto = input(msg).strip()
        while texto == "":
            texto = input(msg).strip()
        return texto

    def _ler_int(self, msg):
        while True:
            try:
                return int(self._ler_texto(msg))
            except ValueError:
                print("Digite um número inteiro válido.")

    def _ler_float(self, msg):
        while True:
            try:
                # aceita 120,50 ou 120.50
                return float(self._ler_texto(msg).replace(",", "."))
            except ValueError:
                print("Digite um valor válido (ex.: 120,50).")

    def _ler_sim_nao(self, msg):
        while True:
            resposta = self._ler_texto(msg).lower()
            if resposta == "s":
                return True
            if resposta == "n":
                return False
            print("Responda com s ou n.")
