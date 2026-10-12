from database.sqlitedb import SQLiteDB

class AlunoDAO:
    def __init__(self):
        self.db = SQLiteDB()

    def create(self, data):
        """
        Insere um novo aluno no banco de dados.
        Retorna o número de linhas afetadas (1 se inserido com sucesso, 0 caso contrário).
        """
        self.db.conectar()
        sql = "INSERT INTO alunos (matricula, nome_completo) VALUES (?, ?);"
        matricula = data.get('matricula')
        nome = data.get('nome')
        resultado = self.db.executar(query=sql, params=(matricula, nome))
        self.db.desconectar()
        return resultado  # Retorna o número de linhas afetadas (1 se inserido com sucesso, 0 caso contrário)

    def read_all(self):
        """
        Retorna todos os alunos do banco de dados.
        Retorna uma lista de objetos Aluno. Se não houver alunos, retorna uma lista vazia e None se ocorrer um erro.
        """
        from models.aluno import Aluno  # Importa a classe Aluno aqui para evitar dependência circular
        self.db.conectar()
        sql = "SELECT matricula, nome_completo FROM alunos;"
        resultados = self.db.consultar(query=sql)
        self.db.desconectar()
        # Converte os resultados em objetos Aluno
        alunos = []
        for row in resultados:
            matricula = row["matricula"]
            nome = row["nome_completo"]
            data = {
                'matricula': matricula,
                'nome': nome
            }
            alunos.append(data)
        return alunos

    def read_one_by_matricula(self, matricula: str):
        """
        Procura um aluno do banco de dados com base na matrícula.

        Retorna um dicionário (Aluno.data) com os dados do aluno se encontrado, False caso contrário.
        Obs.: Se ocorrer um erro na execução da consulta, retorna None.
        """
        self.db.conectar()
        sql = "SELECT matricula, nome_completo FROM alunos WHERE matricula = ?;"
        resultado = self.db.consultar(query=sql, params=(matricula,))
        self.db.desconectar()
        if len(resultado) > 0:
            # consulta encontrou o aluno
            row = resultado[0]
            data = {
                'matricula': row["matricula"],
                'nome': row["nome_completo"]
            }
            return data
        else: return None  # consulta não encontrou o aluno

    def update(self, data: dict):
        # TODO: Implementar a atualização de um aluno no banco de dados
        # a partir da matricula atualizar o nome do aluno
        pass

    def delete(self, matricula: str):
        # TODO: Implementar a exclusão de um aluno no banco de dados
        # a partir da matricula excluir o aluno do banco de dados
        pass