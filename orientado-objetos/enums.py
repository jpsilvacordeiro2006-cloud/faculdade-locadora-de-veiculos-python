from enum import Enum


# situações possíveis de um veículo
class StatusVeiculo(Enum):
    DISPONIVEL = "DISPONIVEL"
    ALUGADO = "ALUGADO"
    MANUTENCAO = "MANUTENCAO"

    def __str__(self):
        return self.value


# situações possíveis de uma locação
class StatusLocacao(Enum):
    ATIVA = "ATIVA"
    FINALIZADA = "FINALIZADA"

    def __str__(self):
        return self.value
