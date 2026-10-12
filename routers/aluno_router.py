from flask import Flask
from controllers import aluno_controller

def adicionar_rotas(app: Flask):
    app.add_url_rule('/aluno/novo', endpoint='aluno_novo', view_func=aluno_controller.novo, methods=['GET'])
    app.add_url_rule('/aluno/salvar', endpoint='aluno_salvar', view_func=aluno_controller.salvar, methods=['POST'])
    app.add_url_rule('/aluno/alunos', endpoint='aluno_listagem', view_func=aluno_controller.listar_alunos, methods=['GET'])
    app.add_url_rule('/aluno/erros', endpoint='aluno_errros', view_func=aluno_controller.exibir_erros, methods=['POST'])
    app.add_url_rule('/aluno/pesquisar', endpoint='aluno_pesquisar', view_func=aluno_controller.pesquisar, methods=['GET'])
    app.add_url_rule('/aluno/buscar', endpoint='aluno_buscar', view_func=aluno_controller.buscar_aluno_pela_matricula, methods=['POST'])