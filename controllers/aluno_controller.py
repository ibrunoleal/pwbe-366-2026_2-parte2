from flask import render_template, request, redirect
from models.aluno import Aluno

lista_de_alunos = []

def novo():
    return render_template('/aluno/novo_aluno.html')

def salvar():
    matricula = request.form.get('matricula')
    nome = request.form.get('nome')
    novo_aluno = Aluno(matricula=matricula, nome=nome)
    lista_de_alunos.append(novo_aluno)
    return redirect('/aluno/alunos')

def listar_alunos():
    contexto = {
        'alunos': lista_de_alunos
    }
    return render_template('/aluno/alunos.html', context=contexto)