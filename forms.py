from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField('Введите имя', validators=[DataRequired()])
    email = StringField('Введите электронную почту', validators=[DataRequired(), Email()])
    password = PasswordField('Введите пароль', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    date_of_birth = DateField('Укажите дату рождения', validators=[DataRequired()])
    agreement = BooleanField('Согласен на обработку моих персональных данных', default=False, validators=[DataRequired()])