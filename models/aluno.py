from daos.aluno_dao import AlunoDAO

class Aluno:
    def __init__(self, matricula: str, nome: str):
        self.matricula = matricula
        self.nome = nome

    def save(self):
        """
        Salva o aluno no banco de dados.
        Retorna True se o aluno foi salvo com sucesso, False caso contrário.
        """
        dao = AlunoDAO()
        resultado = dao.create(self)
        if resultado == 1:
            print(f"Aluno {self.nome} com matrícula {self.matricula} salvo com sucesso.")
            return True
        else:
            print(f"Falha ao salvar o aluno {self.nome} com matrícula {self.matricula}.")
            return False

    def get_all():
        """
        Retorna todos os alunos do banco de dados.
        Retorna uma lista de objetos Aluno. Se não houver alunos, retorna uma lista vazia e None se ocorrer um erro.
        """
        dao = AlunoDAO()
        resultado = dao.read_all()
        if resultado is None:
            print("Falha ao consultar os alunos.")
            return None
        return resultado

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