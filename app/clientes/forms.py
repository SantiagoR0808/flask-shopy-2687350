from flask_wtf import FlaskForm
from wtforms import StringField, EmailField ,PasswordField,SubmitField
from wtforms.validators  import InputRequired,Length

class NewClientForm(FlaskForm):
    username = StringField("nombre de usuario:" , validators = [InputRequired(message="nombre de producto requerido")] )
    password = StringField("Ingrese su contraseña",validators = [InputRequired(message="clave obligatoria")])
    email = EmailField("correo electronico:",validators = [InputRequired(message="Ingrese su correo"),
                                                               Length(max=10, message="El correo debe tener maximo 10 caracteres")])
  
    submit = SubmitField("Guardar")

class EditClientForm( NewClientForm):
    submit = SubmitField("Actualizar")