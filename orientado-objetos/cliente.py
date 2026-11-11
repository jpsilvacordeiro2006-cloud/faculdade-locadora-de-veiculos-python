class Cliente:

    def __init__(self, id, nome, cpf, cnh, telefone):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._cnh = cnh
        self._telefone = telefone

    def exibir_info(self):
        print(f"[{self._id}] {self._nome} - CPF: {self._cpf} - "
              f"CNH: {self._cnh} - Tel: {self._telefone}")

    @property
    def id(self):
        return self._id

    @property
    def cpf(self):
        return self._cpf

    @property
    def cnh(self):
        return self._cnh

    # nome e telefone podem ser alterados
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone
