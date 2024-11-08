from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Editora, Revistas

bp_revistas = Blueprint('revista', __name__ , template_folder="templates")

@bp_revistas.route('/')
def index():
    r = Revistas.query.all()
    return render_template('revista.html', revista=r)

@bp_revistas.route('/add')
def add():
    e = Editora.query.all()
    return render_template('revista_add.html', editora = e)

# \*PAREI AQUI*\


@bp_pedido.route('/save', methods=['POST'])
def save():
    usuario_id = request.form.get('usuario_id')
    pizza_id = request.form.get('pizza_id')
    data = request.form.get('data')
    if usuario_id and pizza_id and data:
        objeto = Pedido(usuario_id, pizza_id, data)
        db.session.add(objeto)
        db.session.commit()
        flash('Pedido salvo com sucesso!')
        return redirect('/pedidos')
    else:
        flash('Preencha todos os campos.')
        return redirect('/pedidos/add')
