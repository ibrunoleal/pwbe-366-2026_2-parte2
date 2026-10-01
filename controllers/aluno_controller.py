from flask import render_template, request, redirect

from daos.aluno_dao import AlunoDAO
from models.aluno import Aluno

lista_de_alunos = []

def novo():
    return render_template('/aluno/novo_aluno.html')

def salvar():
    matricula = request.form.get('matricula')
    nome = request.form.get('nome')
    novo_aluno = Aluno(matricula=matricula, nome=nome)
    novo_aluno.save()
    return redirect('/aluno/alunos')

def listar_alunos():
    alunos = Aluno.get_all()
    contexto = {
        'alunos': alunos
    }
    return render_template('/aluno/alunos.html', context=contexto)