"""Forms."""
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms.fields import FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from dafamilia.models import Usuario


class FormCriarConta(FlaskForm):
    """Cria o Form de Criar Conta."""
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField(
        'E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao = PasswordField('Confirmação da Senha', validators=[
                                DataRequired(), EqualTo('senha')])
    botao_submit_criar_conta = SubmitField('Criar Conta')

    def validate_email(self, email):
        """Validação de email existente."""
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError(
                'Email já cadastrado. Cadastre-se com outro email ou faça login para continuar')


class FormLogin(FlaskForm):
    """Cria o Form de Login."""
    email = StringField(
        'E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')

class FormEditarPerfil(FlaskForm):
    """Editar Perfil."""
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto do Perfil',
                            validators=[FileAllowed(['jpg', 'png', 'gif'])])
    curso_excel = BooleanField('Excel')
    curso_vba = BooleanField('VBA')
    curso_powerbi = BooleanField('Power BI')
    curso_python = BooleanField('Python')
    curso_ppt = BooleanField('Apresentações')
    curso_sql = BooleanField('SQL')
    botao_submit_editar_perfil = SubmitField('Salvar')

    def validate_email(self, email):
        """Validação de email existente."""
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError(
                    'Já existe um usuario com esse email. Cadastre-se com outro email.')


class FormCriarPost(FlaskForm):
    """."""
    titulo = StringField('Título do Post', validators=[
                         DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Escreva seu Post Aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Postar')
