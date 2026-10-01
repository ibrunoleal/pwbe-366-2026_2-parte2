from database.sqlitedb import SQLiteDB

class AlunoDAO:
    def __init__(self):
        self.db = SQLiteDB()

    def create(self, aluno):
        """
        Insere um novo aluno no banco de dados.
        Retorna o número de linhas afetadas (1 se inserido com sucesso, 0 caso contrário).
        """
        self.db.conectar()
        sql = "INSERT INTO alunos (matricula, nome_completo) VALUES (?, ?);"
        resultado = self.db.executar(query=sql, params=(aluno.matricula, aluno.nome))
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
        # Converte os resultados em objetos Aluno
        alunos = []
        for row in resultados:
            matricula = row["matricula"]
            nome = row["nome_completo"]
            aluno = Aluno(matricula=matricula, nome=nome)
            alunos.append(aluno)
        self.db.desconectar()
        return alunos