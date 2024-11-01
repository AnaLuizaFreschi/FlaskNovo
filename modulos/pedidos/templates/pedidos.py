from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Pedido

bp_pedido = Blueprint('pedidos', __name__ , template_folder="templates")

@bp_pedido.route('/')
def index():
    dados = Pedido.query.all()
    return render_template('pedido.html', dados=dados)

@bp_pedido.route('/add')
def add():
    return render_template('pedido_add.html')

@bp_pedido.route('/save', methods=['POST'])
def save():
    data = request.form.get('data')
    usuario = request.form.get('usuario')
    pizza = request.form.get('pizza')
    if data and usuario and pizza:
        objeto = Pedido(data, usuario, pizza)
        db.session.add(objeto)
        db.session.commit()
        flash('Pedido salvo com sucesso!')
        return redirect('/pedidos')
    else:
        flash('Preencha todos os campos.')
        return redirect('/pedidos/add')
