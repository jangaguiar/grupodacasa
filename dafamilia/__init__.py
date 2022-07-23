"""Grupodafamilia."""
from flask_bootstrap import Bootstrap5
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_material import Material

app = Flask(__name__)


bootstrap = Bootstrap5(app)
# chave criada com o Python secrets - hex(16)
app.config['SECRET_KEY'] = 'a96187d522ac0db61233c854d5ed9e2b'
# configurando o local  da criação do DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dafamilia.db'
# para desabilitar o warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Criando o DB
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

# importar aqui pois os routs precisam do app para funcionar
# pylint: disable=wrong-import-position
from dafamilia import routes
# pylint: enable=wrong-import-position
