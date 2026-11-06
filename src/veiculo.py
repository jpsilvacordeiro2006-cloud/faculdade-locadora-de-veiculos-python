from abc import ABC, abstractmethod

from enums import StatusVeiculo


# Classe abstrata: ninguém cria um "veículo genérico", só Carro ou Moto
class Veiculo(ABC):

    def __init__(self, id, placa, marca, modelo, ano, valor_diaria):
        self._id = id
        self._placa = placa
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._valor_diaria = valor_diaria
        self._status = StatusVeiculo.DISPONIVEL  # todo veículo começa disponível

    # cada tipo de veículo calcula o aluguel do seu jeito
    @abstractmethod
    def calcular_valor_aluguel(self, dias):
        pass

    def esta_disponivel(self):
        return self._status == StatusVeiculo.DISPONIVEL

    def exibir_info(self):
        print(f"[{self._id}] {self._marca} {self._modelo} ({self._ano}) - "
              f"Placa: {self._placa} - Diária: R$ {self._valor_diaria:.2f} - "
              f"{self._status}")

    # getters
    @property
    def id(self):
        return self._id

    @property
    def placa(self):
        return self._placa

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def ano(self):
        return self._ano

    # diária e status podem mudar depois do cadastro, então têm setter
    @property
    def valor_diaria(self):
        return self._valor_diaria

    @valor_diaria.setter
    def valor_diaria(self, valor):
        self._valor_diaria = valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status


class Carro(Veiculo):

    def __init__(self, id, placa, marca, modelo, ano, valor_diaria,
                 numero_portas, ar_condicionado):
        super().__init__(id, placa, marca, modelo, ano, valor_diaria)
        self._numero_portas = numero_portas
        self._ar_condicionado = ar_condicionado

    def calcular_valor_aluguel(self, dias):
        valor = self.valor_diaria * dias
        if self._ar_condicionado:
            valor += 15.0 * dias  # ar-condicionado cobra 15 reais por dia
        return valor

    def exibir_info(self):
        print("CARRO ", end="")
        super().exibir_info()
        ar = "Sim" if self._ar_condicionado else "Não"
        print(f"      Portas: {self._numero_portas} | Ar-condicionado: {ar}")

    @property
    def numero_portas(self):
        return self._numero_portas

    @property
    def ar_condicionado(self):
        return self._ar_condicionado


class Moto(Veiculo):

    def __init__(self, id, placa, marca, modelo, ano, valor_diaria, cilindradas):
        super().__init__(id, placa, marca, modelo, ano, valor_diaria)
        self._cilindradas = cilindradas

    def calcular_valor_aluguel(self, dias):
        valor = self.valor_diaria * dias
        if self._cilindradas > 500:
            valor *= 1.10  # moto acima de 500cc paga 10% a mais
        return valor

    def exibir_info(self):
        print("MOTO  ", end="")
        super().exibir_info()
        print(f"      Cilindradas: {self._cilindradas} cc")

    @property
    def cilindradas(self):
        return self._cilindradas
