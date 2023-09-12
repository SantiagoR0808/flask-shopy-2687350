from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField ,SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed 
from wtforms.validators  import InputRequired, NumberRange

class ProductoForm():
    nombre = StringField("nombre del producto:" , validators = [InputRequired(message="nombre de producto requerido")] )
    precio = IntegerField("precio del producto:" , validators = [InputRequired(message = "precio requerido"), 
                                                                 NumberRange(
                                                                     message = "precio fuera de rango",
                                                                     max = 100000
                                                                )])
    
class NewproductForm(FlaskForm, ProductoForm):                                                                  
    imagen = FileField("Seleccione imagen del producto:" ,
                        validators = [ FileRequired(message = "debe seleccionar una imagen") , 
                                        FileAllowed(['jpg' , 'png'] ,
                                                    "solo se permiten imagenes" ) ]) 
    submit = SubmitField("Guardar")

class EditProductForm(FlaskForm , ProductoForm ):
    submit = SubmitField("Actualizar")