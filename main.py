from flask import Flask

from routers import index_router, aluno_router
from database.sqlitedb import SQLiteDB


app = Flask(__name__)


db = SQLiteDB()
db.conectar() # Abre a conexão com o banco de dados
db.executar_script_sql('database/scripts/tabela_aluno.sql') # cria a tabela de alunos
db.desconectar() # Fecha a conexão com o banco de dados


index_router.adicionar_rotas(app=app)
aluno_router.adicionar_rotas(app=app)
