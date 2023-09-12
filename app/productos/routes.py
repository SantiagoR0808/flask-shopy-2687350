from flask import render_template,redirect,flash
from . import productos
import app
from .forms import NewproductForm,EditProductForm
import os


#rutas del modulo "productos"
@productos.route("/listar")
def listar():
   
    # listar los productos utilizando
    # modelos
    productos = app.models.Producto.query.all()
    return render_template("index.html" , 
                           productos = productos)

@productos.route("/nuevo" ,
                  methods= ["GET" , "POST"])
def nuevo():
    
     #definir el formulario
    form = NewproductForm()
    #definir el objeto producto vacio
    p= app.models.Producto()
    if form.validate_on_submit():
        form.populate_obj(p)
        p.imagen = form.imagen.data.filename
        app.db.session.add(p)
        app.db.session.commit()
       
        ##return os.getcwd()
        #extraer el objeto FileStorage
        file = form.imagen.data
        file.save(os.path.abspath(os.getcwd() +
                                "/app/productos/imagenes/" +
                                form.imagen.data.filename))
        
        flash("producto registrado correctamente")
        return redirect("/productos/listar")

    return render_template("new.html",
                           operacion="Nuevo",
                           form = form) 

@productos.route("/editar/<producto_id>",
                  methods= ["GET" , "POST"])
def editar(producto_id):
    p = app.models.Producto.query.get(producto_id)
    form = EditProductForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash("Producto actualizado correctamente")
        return redirect("/productos/listar")

    return render_template("new.html",
                           operacion="Actualizar",
                           form = form)

@productos.route("/eliminar/<producto_id>",
                  methods= ["GET" , "POST"])
def eliminar(producto_id):
    p = app.models.Producto.query.get(producto_id)
    app.db.session.delete(p)
    app.db.session.commit()
    
    flash("producto eliminado correctamente")
    return redirect("/productos/listar")