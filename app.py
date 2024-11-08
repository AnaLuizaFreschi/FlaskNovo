from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = "Qualquercoisa"
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/bin3g1"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
db.init_app(app)
migrate = Migrate(app, db)
from models import Editoras, Revistas
from modulos.editora.editora import bp_editora
app.register_blueprint(bp_editora, url_prefix='/editora')
from modulos.revista.revista import bp_revista
app.register_blueprint(bp_revista, url_prefix='/revista')

@app.route('/')
def index():
    return render_template("ola.html")