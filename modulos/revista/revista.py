from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Editoras, Revistas

bp_revista = Blueprint('revista', __name__ , template_folder="templates")

@bp_revista.route('/')
def index():
    r = Revistas.query.all()
    return render_template('revista.html', revista=r)

@bp_revista.route('/add')
def add():
    e = Editoras.query.all()
    return render_template('revista_add.html', editoras=e)



@bp_revista.route('/save', methods=['POST'])
def save():
    id_editora = request.form.get('id_editora')
    titulo = request.form.get('titulo')
    edicao = request.form.get('edicao')
    if id_editora and titulo and edicao:
        objeto = Revistas(id_editora, titulo, edicao)
        db.session.add(objeto)
        db.session.commit()
        flash('Revista salva com sucesso!')
        return redirect('/revista')
    else:
        flash('Preencha todos os campos.')
        return redirect('/revista/add')
