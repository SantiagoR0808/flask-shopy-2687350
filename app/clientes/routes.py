from flask import render_template,redirect,flash
from . import clientes
import app
from .forms import NewClientForm,EditClientForm


#rutas del modulo "clientes"
@clientes.route("/listarcliente")
def listarcliente():
   
    # listar los clientes utilizando
    # modelos
    clientes = app.models.Cliente.query.all()
    return render_template("indexClientes.html" , 
                           clientes = clientes)

@clientes.route("/nuevocliente" ,
                  methods= ["GET" , "POST"])
def nuevocliente():
     #definir el formulario
    formcliente = NewClientForm()
    #definir el objeto producto vacio
    p= app.models.Cliente()
    if formcliente.validate_on_submit():
        formcliente.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
       
        flash("cliente registrado correctamente")
        return redirect("/clientes/listarcliente")

    return render_template("newCliente.html",
                           operacion="Nuevo",
                           formcliente = formcliente) 

@clientes.route("/editarcliente/<cliente_id>",
                  methods= ["GET" , "POST"])
def editarcliente(cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    formcliente = EditClientForm(obj = p)
    if formcliente.validate_on_submit():
        formcliente.populate_obj(p)
        app.db.session.commit()
        flash("Cliente actualizado correctamente")
        return redirect("/clientes/listarcliente")

    return render_template("newCliente.html",
                           operacion="Actualizar",
                           formcliente = formcliente)

@clientes.route("/eliminarcliente/<cliente_id>",
                  methods= ["GET" , "POST"])
def eliminarcliente(cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    app.db.session.delete(p)
    app.db.session.commit()
    
    flash("Cliente eliminado correctamente")
    return redirect("/clientes/listarcliente")