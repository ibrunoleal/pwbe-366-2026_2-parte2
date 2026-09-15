from flask import Flask
from controllers import index_controller

def adicionar_rotas(app: Flask):
    app.add_url_rule('/', view_func=index_controller.index, methods=['GET'])