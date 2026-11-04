import re

from models.aluno import Aluno


class Contato:
    def __init__(self, data: dict):
        """
        Inicializa um objeto Contato.
        data: dicionário contendo os dados do contato do Aluno, com as chaves "nome" e "telefone".
        """
        self.data = data
        self.errors = []

    @staticmethod
    def get_all_by_matricula(matricula: str):
        from daos.contato_dao import ContatoDAO

        contato_dao = ContatoDAO()
        resultado = contato_dao.read_all_by_matricula(matricula)
        if resultado is None:
            print("Falha ao consultar os contatos do aluno com matrícula {}.".format(matricula))
            return None
        else:
            return resultado

    def validate(self):
        """
        Valida os dados do contato.
        Se os dados forem válidos, atualiza o atributo `self.data`.
        Se os dados forem inválidos, adiciona mensagens de erro em `self.errors`, ou seja,
        se a lista de erros estiver vazia o contato é considerado válido, caso contário, inválido.

        nome: deve ser uma string com no mínimo 5 e no máximo 50 caracteres e não pode conter dois espaços seguidos.

        telefone: deve ser uma string com no mínimo no formato (XX)XXXXX-XXXX ou (XX)XXXX-XXXX.

        matricula_aluno: deve ser uma string que representa a matrícula do aluno ao qual o contato será associado.
        """
        # validação do nome
        nome = self.data.get("nome")
        if nome is None or not isinstance(nome, str):
            self.errors.append("O nome deve ser uma string.")
        else:
            if not nome.strip():
                self.errors.append("O nome não pode ser vazio.")
            if "  " in nome:
                self.errors.append("O nome não pode conter dois espaços consecutivos.")
            if len(nome) < 5 or len(nome) > 50:
                self.errors.append("O nome deve ter entre 5 e 50 caracteres.")

        # validação do telefone
        telefone = self.data.get("telefone")
        if telefone is None or not isinstance(telefone, str):
            self.errors.append("O telefone deve ser uma string.")
        else:
            if not telefone.strip():
                self.errors.append("O telefone não pode ser vazio.")
            else:
                if re.fullmatch(r"\([0-9]{2}\)[0-9]{4,5}-[0-9]{4}", telefone) is None:
                    self.errors.append(
                        "O telefone deve estar no formato (XX)XXXXX-XXXX ou (XX)XXXX-XXXX."
                    )

        # validação se o aluno existe para associar o contato
        matricula = self.data.get("matricula")
        aluno_data = Aluno.get_one_by_matricula(matricula=matricula)
        if aluno_data is None:
            self.errors.append(
                "Aluno não encontrado para a matrícula: {}".format(matricula)
            )

        if len(self.errors) == 0:
            data = {"nome": nome, "telefone": telefone, "matricula": matricula}
            self.data = data

    def salvar(self):
        from daos.contato_dao import ContatoDAO

        """
        Salva o contato no banco de dados, associando-o ao aluno fornecido.
        aluno: objeto Aluno ao qual o contato será associado.
        Retorna True se o contato foi salvo com sucesso, False caso contrário.
        """
        contato_dao = ContatoDAO()
        resultado = contato_dao.create(data=self.data)
        if resultado == 1:
            return True
        else:
            return False
