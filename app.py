# Importamos la clase flask y las librerias correspondientes
from flask import Flask,  render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# Creamos la instancia
app = Flask(__name__)

# Configuramos la conexion a la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'bd_proyecto_final'
mysql = MySQL(app)


# Configuramos el inicio de sesion
app.secret_key = 'mysecretkey'

# Programamos cada ruta

# Ruta para el index


@app.route('/')
def Index():
    return render_template('index.html')

# Ruta para ir al formulario de nuevo contacto


@app.route('/nuevo_contacto')
def nuevo_contacto():
    return render_template('nuevo_contacto.html')

# Ruta para ir a la pagina de nuestro servicio


@app.route('/nuestros_servicios')
def nuestros_servicios():
    return render_template('nuestros_servicios.html')

# Ruta para la pagina de quienes somos


@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')


# Ruta para la funcion de agregar un nuevo contacto


@app.route('/add_contact', methods=['POST'])
def agregar_contacto():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        email = request.form['email']
        telefono = request.form['telefono']
        mensaje = request.form['mensaje']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tb_contactos (nombres, apellidos, email, telefono, mensaje) VALUES(%s, %s, %s, %s, %s)',
                    (nombres, apellidos, email, telefono, mensaje))
        mysql.connection.commit()
        flash('Tus datos fueron guardados correctamente!')
        return redirect(url_for('listar_contactos'))


# @app.route('/edit/<id>')
# def devolver_contacto(id):
#     cur = mysql.connection.cursor()
#     cur.execute('SELECT * FROM tb_contactos WHERE id = %s', (id))
#     data = cur.fetchall()

#     return render_template('edit_contact.html', contact=data[0])


# @ app.route('/delete/<string:id>')
# def eliminar_contacto(id):
#     cur = mysql.connection.cursor()
#     cur.execute('DELETE FROM contact_tb WHERE id = {0}'.format(id))
#     mysql.connection.commit()
#     flash('Contacto eliminado satisfactoriamente')
#     return redirect(url_for('Index'))


# @app.route('/update/<id>', methods=['POST'])
# def actualizar_contacto(id):
#     request.method == 'POST'

#     nombres = request.form['nombres']
#     apellidos = request.form['apellidos']
#     email = request.form['email']

#     telefono = request.form['telefono']
#     mensaje = request.form['mensaje']

#     cur = mysql.connection.cursor()
#     cur.execute("""
#         UPDATE tb_contacto
#         SET nombres = %s,
#             apellidos = %s,
#             email = %s,
#             telefono = %s,
#             mensaje = %s
#         WHERE id = %s
#     """, (nombres, apellidos, email, telefono, mensaje, id))
#     cur.connection.commit()
#     flash('Contacto actualizado satisfactoriamente')
#     return redirect(url_for('Index'))

# Ruta para listar los contactos

@app.route('/lista_contactos')
def listar_contactos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tb_contactos')
    data = cur.fetchall()
    return render_template('lista_contactos.html', contacts=data)


# Ejecutamos la app
if __name__ == '__main__':
    app.run(port=3000, debug=True)
