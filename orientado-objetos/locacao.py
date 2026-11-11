from enums import StatusLocacao, StatusVeiculo


class Locacao:

    def __init__(self, id, cliente, veiculo, dias_previstos):
        self._id = id
        self._cliente = cliente
        self._veiculo = veiculo
        self._dias_previstos = dias_previstos
        self._dias_efetivos = 0
        # enquanto a locação está ativa, o total é o valor previsto
        self._valor_total = veiculo.calcular_valor_aluguel(dias_previstos)
        self._status = StatusLocacao.ATIVA
        veiculo.status = StatusVeiculo.ALUGADO

    def calcular_multa(self):
        dias_extras = max(0, self._dias_efetivos - self._dias_previstos)
        return dias_extras * self._veiculo.valor_diaria * 1.5

    def finalizar(self, dias_efetivos):
        self._dias_efetivos = dias_efetivos
        # não importa se é carro ou moto, cada um calcula do seu jeito
        self._valor_total = self._veiculo.calcular_valor_aluguel(dias_efetivos) + self.calcular_multa()
        self._status = StatusLocacao.FINALIZADA
        self._veiculo.status = StatusVeiculo.DISPONIVEL
        return self._valor_total

    def exibir_info(self):
        v = self._veiculo
        print(f"Locação #{self._id} - {self._cliente.nome} | {v.marca} {v.modelo} "
              f"({v.placa}) | {self._dias_previstos} dia(s) previsto(s) | "
              f"R$ {self._valor_total:.2f} | {self._status}")

    @property
    def id(self):
        return self._id

    @property
    def cliente(self):
        return self._cliente

    @property
    def veiculo(self):
        return self._veiculo

    @property
    def dias_previstos(self):
        return self._dias_previstos

    @property
    def dias_efetivos(self):
        return self._dias_efetivos

    @property
    def valor_total(self):
        return self._valor_total

    @property
    def status(self):
        return self._status
