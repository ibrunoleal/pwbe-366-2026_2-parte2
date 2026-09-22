from flask import Flask
from controllers import aluno_controller

def adicionar_rotas(app: Flask):
    app.add_url_rule('/aluno/novo', view_func=aluno_controller.novo, methods=['GET'])
    app.add_url_rule('/aluno/salvar', view_func=aluno_controller.salvar, methods=['POST'])
    app.add_url_rule('/aluno/alunos', view_func=aluno_controller.listar_alunos, methods=['GET'])