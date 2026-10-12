from flask import render_template, request, redirect, url_for

from models.aluno import Aluno


def novo():
    return render_template("/aluno/novo_aluno.html")


def exibir_erros(erros: list):
    contexto = {"erros": erros}
    return render_template("/aluno/erros.html", context=contexto)


def salvar():
    data = (
        request.form
    )  # Pega os dados do formulário enviado tanto via GET quanto via POST
    novo_aluno = Aluno(data=data)
    novo_aluno.validate()
    if len(novo_aluno.errors) == 0:
        novo_aluno.save()
        return redirect("/aluno/alunos")
    else:
        return exibir_erros(erros=novo_aluno.errors)


def listar_alunos():
    alunos = Aluno.get_all()
    contexto = {"alunos": alunos}
    return render_template("/aluno/alunos.html", context=contexto)


def pesquisar():
    return render_template("/aluno/pesquisar.html")


def buscar_aluno_pela_matricula():
    matricula = request.form.get("matricula")
    aluno_data = Aluno.get_one_by_matricula(matricula=matricula)
    if aluno_data is None:
        erros = ["Aluno não encontrado para a matrícula: {}".format(matricula)]
        contexto = {"erros": erros}
        return render_template("/aluno/erros.html", context=contexto)
    else:
        contexto = {"aluno": aluno_data}
        return render_template("/aluno/aluno.html", context=contexto)
