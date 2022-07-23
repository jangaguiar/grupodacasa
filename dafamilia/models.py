"""Models DB."""
# pylint: disable=no-member
from datetime import datetime
from flask_login import UserMixin
from dafamilia import database, login_manager


@login_manager.user_loader
def load_usuario(id_usuario):
    """."""
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    """Criando Usuario."""
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='Não Informado')

    def contar_posts(self):
        """Conta os Posts do Usuário."""
        return len(self.posts)

class Post(database.Model):
    """Criando o Post."""
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.Integer, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(
        database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(
        database.Integer, database.ForeignKey('usuario.id'), nullable=False)
