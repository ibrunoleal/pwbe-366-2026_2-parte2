from daos.aluno_dao import AlunoDAO


class Aluno:
    def __init__(self, data: dict):
        """
        Inicializa um objeto Aluno.
        data: dicionário contendo os dados do aluno, com as chaves "matricula" e "nome".
        """
        self.data = data
        self.errors = []

    def validate(self):
        """
        Valida os dados do aluno.
        Se os dados forem válidos, atualiza o atributo `self.data`.
        Se os dados forem inválidos, adiciona mensagens de erro em `self.errors`, ou seja, 
        se a lista de erros estiver vazia o aluno é considerado válido, caso contário, inválido.
        
        matricula: deve ser uma string de exatamente 10 caracteres.
        
        nome: deve ser uma string com no mínimo 5 e no máximo 50 caracteres.
        """
        matricula = self.data.get("matricula")
        if matricula is None or not isinstance(matricula, str):
            self.errors.append("A matrícula deve ser uma string.")
        if not matricula.strip():
            self.errors.append(
                "A matrícula não pode ser vazia ou conter apenas espaços."
            )
        if len(matricula) != 10:
            self.errors.append("A matrícula deve ter exatamente 10 caracteres.")

        nome = self.data.get("nome")
        if nome is None or not isinstance(nome, str):
            self.errors.append("O nome deve ser uma string.")
        if not nome.strip():
            self.errors.append("O nome não pode ser vazio.")
        if len(nome) < 5 or len(nome) > 50:
            self.errors.append("O nome deve ter entre 5 e 50 caracteres.")

        if len(self.errors) == 0:
            data = {"matricula": matricula, "nome": nome}
            self.data = data

    def save(self):
        """
        Salva o aluno no banco de dados.
        Retorna True se o aluno foi salvo com sucesso, False caso contrário.
        """
        dao = AlunoDAO()
        resultado = dao.create(self.data)
        if resultado == 1:
            return True
        else:
            return False

    @staticmethod
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

    @staticmethod
    def get_one_by_matricula(matricula: str):
        """
        Retorna um aluno do banco de dados com base na matrícula.
        Retorna um objeto Aluno se encontrado, None caso contrário.
        """
        dao = AlunoDAO()
        aluno_data = dao.read_one_by_matricula(matricula)
        if aluno_data is None:
            print(f"Não encontrado aluno com matrícula {matricula}.")
            return None
        else:
            return aluno_data

    def atualizar(self):
        """
        Atualiza os dados do aluno no banco de dados.
        Retorna True se o aluno foi atualizado com sucesso, False caso contrário.
        """
        dao = AlunoDAO()
        resultado = dao.update(self.data)
        if resultado == 1:
            return True
        else:
            return False

    def remover(self):
        """
        Remove o aluno do banco de dados.
        Retorna True se o aluno foi removido com sucesso, False caso contrário.
        """
        dao = AlunoDAO()
        resultado = dao.delete(self.data)
        if resultado == 1:
            return True
        else:
            return False