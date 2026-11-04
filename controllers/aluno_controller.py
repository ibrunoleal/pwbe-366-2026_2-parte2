from flask import render_template, request, redirect, url_for

from models.aluno import Aluno
from models.contato import Contato


def novo():
    return render_template("/aluno/novo_aluno.html")


def exibir_erros(erros: list):
    contexto = {"erros": erros}
    return render_template("/aluno/erros.html", context=contexto)


def salvar():
    data = request.form
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
    """
    Busca um aluno pela matrícula.
    Recupera, também, os contatos associados ao aluno (relação 1:N entre aluno e contatos).
    """
    matricula = request.form.get("matricula")
    aluno_data = Aluno.get_one_by_matricula(matricula=matricula)
    # confirma se o aluno existe antes de tentar buscar os contatos
    if aluno_data is None:
        erros = ["Aluno não encontrado para a matrícula: {}".format(matricula)]
        contexto = {"erros": erros}
        return render_template("/aluno/erros.html", context=contexto)
    else:
        # recupera os contaos do aluno
        contatos = Contato.get_all_by_matricula(matricula)
        # confirma se a consulta para os contatos do aluno foi bem-sucedida
        if contatos is None:
            erros = [
                "Falha ao consultar os contatos do aluno com matrícula: {}".format(
                    matricula
                )
            ]
            contexto = {"erros": erros}
            return render_template("/aluno/erros.html", context=contexto)
        else:
            # se consulta bem sucedida, adiciona os contados do aluno ao contexto 
            # (se ainda nao tiver contatos para o aluno, a lista de contatos será vazia)
            contexto = {
                "aluno": aluno_data,
                "contatos": contatos,
            }
            return render_template("/aluno/aluno.html", context=contexto)


def editar_aluno():
    """
    Recupera o aluno pela matricula contida na requisicao e, caso o aluno exista, 
    renderiza a pagina de edicao do aluno.
    """
    matricula = request.form.get("matricula")
    aluno_data = Aluno.get_one_by_matricula(matricula=matricula)
    if aluno_data is None:
        erros = ["Aluno não encontrado para a matrícula: {}".format(matricula)]
        contexto = {"erros": erros}
        return render_template("/aluno/erros.html", context=contexto)
    else:
        contexto = {"aluno": aluno_data}
        return render_template("/aluno/editar.html", context=contexto)


def alterar_aluno():
    """
    Recupera os dados de um aluno da requisicao tipo POST, valida os dados e, 
    caso estejam válidos, atualiza o aluno no banco de dados. 
    """
    data = request.form
    aluno = Aluno(data=data)
    aluno.validate()
    if (
        len(aluno.errors) == 0
    ):  # verifica se os novos dados estão válidos antes de atualizar
        # verifica se o aluno com aquela matricula existe antes de tentar atualizar
        aluno_data = Aluno.get_one_by_matricula(matricula=aluno.data.get("matricula"))
        if aluno_data is None:
            erros = [
                "Aluno não encontrado para a matrícula: {}".format(
                    aluno.data.get("matricula")
                )
            ]
            return exibir_erros(erros=erros)
        else:
            resultado = aluno.atualizar()
            if resultado:
                return redirect(url_for("aluno_listagem"))
            else:
                # se a atualização falhar no banco por algum motivo, exibe uma mensagem de erro
                erros = ["Nenhum aluno foi atualizado. Problema ao atualizar no banco."]
                return exibir_erros(erros=erros)
    else:
        return exibir_erros(erros=aluno.errors)


def remover_aluno():
    matricula = request.form.get("matricula")
    data_aluno = Aluno.get_one_by_matricula(matricula=matricula)
    if data_aluno is None:
        erros = ["Aluno não encontrado para a matrícula: {}".format(matricula)]
        return exibir_erros(erros=erros)
    else:
        aluno = Aluno(data=data_aluno)
        resultado = aluno.remover()
        if resultado:
            return redirect(url_for("aluno_listagem"))
        else:
            erros = ["Falha ao remover o aluno com matrícula: {}".format(matricula)]
            return exibir_erros(erros=erros)


def contato_novo():
    """
    Recupera a matrícula do aluno da requisição do tipo POST e, 
    caso o aluno exista, renderiza a página de cadastro de contato.
    """
    matricula = request.form.get("matricula")
    aluno_data = Aluno.get_one_by_matricula(matricula=matricula)
    if aluno_data is None:
        erros = ["Aluno não encontrado para a matrícula: {}".format(matricula)]
        contexto = {"erros": erros}
        return render_template("/aluno/erros.html", context=contexto)
    else:
        contexto = {"aluno": aluno_data}
        return render_template("/aluno/contato/novo_contato.html", context=contexto)


def contato_salvar():
    data = request.form
    matricula = data.get("matricula")
    nome = data.get("nome")
    telefone = data.get("telefone")
    contato_data = {"nome": nome, "telefone": telefone, "matricula": matricula}
    from models.contato import Contato

    contato = Contato(data=contato_data)
    contato.validate()
    if len(contato.errors) > 0:
        return exibir_erros(erros=contato.errors)
    else:
        resultado = contato.salvar()
        if resultado:
            return redirect(url_for("aluno_listagem"))
        else:
            erros = [
                "Falha ao adicionar contato para o aluno com matrícula: {}".format(
                    matricula
                )
            ]
            return exibir_erros(erros=erros)
