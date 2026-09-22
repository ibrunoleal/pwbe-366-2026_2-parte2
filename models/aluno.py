class Aluno:
    def __init__(self, matricula: str, nome: str):
        self.matricula = matricula
        self.nome = nome

    @property
    def matricula(self) -> str:
        return self._matricula

    @matricula.setter
    def matricula(self, matricula: str) -> None:
        if matricula is None or not isinstance(matricula, str):
            raise ValueError('A matrícula deve ser uma string.')
        if not matricula.strip():
            raise ValueError('A matrícula não pode ser vazia ou conter apenas espaços.')
        if len(matricula) != 10:
            raise ValueError('A matrícula deve ter exatamente 10 caracteres.')
        self._matricula = matricula

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if nome is None or not isinstance(nome, str):
            raise ValueError('O nome deve ser uma string.')
        if not nome.strip():
            raise ValueError('O nome não pode ser vazio.')
        if len(nome) < 5 or len(nome) > 50:
            raise ValueError('O nome deve ter entre 5 e 50 caracteres.')
        self._nome = nome

    def __str__(self):
        return f'Aluno(matricula={self.matricula}, nome={self.nome})'