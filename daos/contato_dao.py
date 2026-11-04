from database.sqlitedb import SQLiteDB

class ContatoDAO:
    def __init__(self):
        self.db = SQLiteDB()

    def create(self, data: dict):
        """
        Insere um novo contato associado a um aluno no banco de dados.
        Retorna o número de linhas afetadas (1 se inserido com sucesso, 0 caso contrário).
        """
        self.db.conectar()
        sql = "INSERT INTO contatos (nome, telefone, matricula) VALUES (?, ?, ?);"
        matricula = data.get('matricula')
        nome = data.get('nome')
        telefone = data.get('telefone')
        resultado = self.db.executar(query=sql, params=(nome, telefone, matricula))
        self.db.desconectar()
        return resultado  # Retorna o número de linhas afetadas (1 se inserido com sucesso, 0 caso contrário)

    def read_all_by_matricula(self, matricula: str):
        """Retorna os contatos associados a um aluno dado pela matrícula."""
        self.db.conectar()
        sql = "SELECT id, nome, telefone FROM contatos WHERE matricula = ?;"
        resultados = self.db.consultar(query=sql, params=(matricula,))
        self.db.desconectar()
        if resultados is None:
            return None
        else:
            contatos = []
            for row in resultados:
                id = row["id"]
                nome = row["nome"]
                telefone = row["telefone"]
                contato_data = {"id": id, "nome": nome, "telefone": telefone, "matricula": matricula}
                contatos.append(contato_data)
            return contatos

    def read_one_by_id(self, contato_id: int):
        """Retorna os dados de um contato específico pelo seu ID."""
        # TODO : Implementar a lógica para buscar um contato pelo ID no banco de dados.
        pass

    def update(self, contato_id: int, dados_do_contato: dict):
        """Atualiza os dados de um contato específico pelo seu ID."""
        # TODO : Implementar a lógica para atualizar um contato no banco de dados.
        pass

    def delete(self, contato_id: int):
        """Remove um contato específico pelo seu ID."""
        # TODO : Implementar a lógica para remover um contato do banco de dados.
        pass