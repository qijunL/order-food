from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo
from wtforms import StringField, PasswordField, Form


class LoginForm(Form):
    login_name = StringField('电子邮件', validators=[DataRequired(), Length(1, 64)])

    login_pwd = PasswordField('密码', validators=[
        DataRequired(message='密码不为空，请输入密码'), Length(6, 20)])
