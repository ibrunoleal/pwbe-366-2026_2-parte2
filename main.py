from flask import Flask
from routers import index_router

app = Flask(__name__)

index_router.adicionar_rotas(app=app)
