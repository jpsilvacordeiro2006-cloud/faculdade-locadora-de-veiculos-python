from enums import StatusLocacao
from locacao import Locacao


class Locadora:

    def __init__(self):
        self._veiculos = []
        self._clientes = []
        self._locacoes = []
        self._proximo_id_veiculo = 1
        self._proximo_id_cliente = 1
        self._proximo_id_locacao = 1

    # ---------- Veículos ----------

    def buscar_veiculo_por_placa(self, placa):
        for veiculo in self._veiculos:
            if veiculo.placa.lower() == placa.lower():
                return veiculo
        return None

    def cadastrar_veiculo(self, veiculo):
        if self.buscar_veiculo_por_placa(veiculo.placa) is not None:
            print("Erro: já existe um veículo com essa placa.")
            return
        self._veiculos.append(veiculo)
        self._proximo_id_veiculo += 1
        print("Veículo cadastrado com sucesso!")

    def listar_veiculos(self):
        if not self._veiculos:
            print("Nenhum veículo cadastrado.")
            return
        for veiculo in self._veiculos:
            veiculo.exibir_info()

    def listar_veiculos_disponiveis(self):
        achou = False
        for veiculo in self._veiculos:
            if veiculo.esta_disponivel():
                veiculo.exibir_info()
                achou = True
        if not achou:
            print("Nenhum veículo disponível.")

    # ---------- Clientes ----------

    def buscar_cliente_por_cpf(self, cpf):
        for cliente in self._clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def cadastrar_cliente(self, cliente):
        if self.buscar_cliente_por_cpf(cliente.cpf) is not None:
            print("Erro: já existe um cliente com esse CPF.")
            return
        self._clientes.append(cliente)
        self._proximo_id_cliente += 1
        print("Cliente cadastrado com sucesso!")

    def listar_clientes(self):
        if not self._clientes:
            print("Nenhum cliente cadastrado.")
            return
        for cliente in self._clientes:
            cliente.exibir_info()

    # ---------- Locação ----------

    def realizar_locacao(self, cpf, placa, dias):
        cliente = self.buscar_cliente_por_cpf(cpf)
        if cliente is None:
            print("Erro: cliente não encontrado.")
            return None

        veiculo = self.buscar_veiculo_por_placa(placa)
        if veiculo is None:
            print("Erro: veículo não encontrado.")
            return None

        if not veiculo.esta_disponivel():
            print("Erro: veículo não está disponível.")
            return None

        if dias < 1:
            print("Erro: a quantidade de dias deve ser pelo menos 1.")
            return None

        locacao = Locacao(self._proximo_id_locacao, cliente, veiculo, dias)
        self._proximo_id_locacao += 1
        self._locacoes.append(locacao)
        print(f"Locação #{locacao.id} realizada! Valor previsto: R$ {locacao.valor_total:.2f}")
        return locacao

    def listar_locacoes_ativas(self):
        achou = False
        for locacao in self._locacoes:
            if locacao.status == StatusLocacao.ATIVA:
                locacao.exibir_info()
                achou = True
        if not achou:
            print("Nenhuma locação ativa.")

    def devolver_veiculo(self, id_locacao, dias_efetivos):
        locacao = None
        for loc in self._locacoes:
            if loc.id == id_locacao:
                locacao = loc
                break

        if locacao is None:
            print("Erro: locação não encontrada.")
            return -1
        if locacao.status != StatusLocacao.ATIVA:
            print("Erro: essa locação já foi finalizada.")
            return -1
        if dias_efetivos < 1:
            print("Erro: a quantidade de dias deve ser pelo menos 1.")
            return -1

        total = locacao.finalizar(dias_efetivos)
        print(f"Devolução registrada! Multa: R$ {locacao.calcular_multa():.2f} | Total: R$ {total:.2f}")
        return total

    @property
    def proximo_id_veiculo(self):
        return self._proximo_id_veiculo

    @property
    def proximo_id_cliente(self):
        return self._proximo_id_cliente
