from database import db
class Editoras(db.Model):
    __tablename__ = 'editora'
    id_editora = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cidade = db.Column(db.String(100))

    def __init__ (self, nome, cidade):
        self.nome = nome
        self.cidade = cidade


    def __repr__ (self):
        return "<Editora {}>".format(self.nome)
    
class Revistas(db.Model):
    _tablename__ = 'revista'
    id_revista = db.Column(db.Integer, primary_key=True)
    id_editora = db.Column(db.Integer, db.ForeignKey('editora.id_editora'))
    titulo = db.Column(db.String(100))
    edicao = db.Column(db.Integer)

    editora = db.relationship('Editoras', foreign_keys=id_editora)
   

    def __init__ (self, id_editora, titulo, edicao):
        self.id_editora = id_editora
        self.titulo = titulo
        self.edicao = edicao

    def __repr__ (self):
        return "<Revista {} - {} - {} - {}>".format(self.titulo, self.editora, self.edicao)
    
