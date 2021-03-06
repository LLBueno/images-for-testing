from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FloatField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(message="Esse campo é requirido.")])
    password = PasswordField('Senha', validators=[DataRequired(message="Esse campo é requirido.")])
    remember_me = BooleanField('Lembre de mim')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(message="Esse campo é requirido.")])
    email = StringField('E-mail', validators=[DataRequired(message="Esse campo é requirido."), Email(message="E-mail inválido.")])
    password = PasswordField('Senha', validators=[DataRequired(message="Esse campo é requirido.")])
    password2 = PasswordField(
        'Senha Novamente', validators=[DataRequired(message="Esse campo é requirido."), EqualTo('password', message='Senhas não coincidem.')])
    submit = SubmitField('Cadastrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Usuário já existente.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('E-mail já existente.')


class ImageForm(FlaskForm):
    image = FileField(validators=[FileRequired(), FileAllowed(['png', 'jpg', 'jpeg'], 'Somente imagem!')])
    submit = SubmitField('Salvar')

class GenerateImageForm(FlaskForm):
    rotacionar = IntegerField('Rotacionar (graus)', default=0)
    zoom = FloatField(default=1.0)
    preto_branco = BooleanField('Preto e Branco', default=False)
    desfoque = BooleanField('Aplicar Desfoque', default=False)
    submit = SubmitField('Gerar')
