# Importación de módulos necesarios
from flask import Flask, request, jsonify, render_template, session, redirect, url_for, flash  # Flask para la aplicación web, request para manejar peticiones, jsonify para respuestas JSON, render_template para renderizar HTML, session para manejar sesiones, redirect para redirigir, url_for para generar URLs, flash para mostrar mensajes
from functools import wraps  # Para crear decoradores
from auth_service import DatabaseAuth  # Módulo personalizado para autenticación
from dotenv import load_dotenv  # Para cargar variables de entorno
import os  # Para interactuar con el sistema operativo
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
from psycopg2 import sql

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Inicialización de la aplicación Flask
app = Flask(__name__)
# Configura la clave secreta para las sesiones desde las variables de entorno
app.secret_key = os.getenv('SECRET_KEY')
# Instancia del servicio de autenticación
auth = DatabaseAuth()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:PanchoLaika4445.@@localhost:5423/CazaTroll'


# Configuración de la base de datos
DATABASE_URI = "dbname='nombre_bd' user='usuario' password='contraseña' host='localhost'"

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        port=5423,  # Cambia esto a 5423
        dbname="CazaTroll",
        user="postgres",
        password="PanchoLaika4445.@"
    )

# Decorador para proteger rutas que requieren autenticación
def login_required(f):
    @wraps(f)  # Preserva los metadatos de la función original
    def decorated_function(*args, **kwargs):
        # Verifica si el usuario está autenticado (user_id en sesión)
        if 'user_id' not in session:
            return jsonify({'error': 'No autorizado'}), 401  # Respuesta 401 si no está autenticado
        return f(*args, **kwargs)  # Ejecuta la función original si está autenticado
    return decorated_function

# Ruta principal de la aplicación
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Aquí va la lógica para manejar el POST
        # ... procesar el formulario ...
        return redirect(url_for('index'))  # O redirige a donde necesites
    return render_template('index.html')

# Ruta para la página de login
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        # Procesar el formulario de inicio de sesión
        username = request.form.get('username')
        password = request.form.get('password')

        success, message = auth.login_user(
            username=username,
            password=password
        )

        if success:
            session['user_id'] = message['user_id']
            session['role_id'] = message['role_id']
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('index'))
        else:
            flash(message, 'error')
            return redirect(url_for('login_page'))

    return render_template('login.html')

# Ruta para la página de registro
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        # Procesar el formulario de registro
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role_id = 2  # Todos los nuevos usuarios serán usuarios normales por defecto

        success, message = auth.register_user(
            username=username,
            password=password,
            email=email,
            role_id=role_id
        )

        if success:
            session['role_id'] = role_id
            flash('Registro exitoso. Por favor, inicia sesión.', 'success')
            return redirect(url_for('login_page'))
        else:
            flash(message, 'error')
            return redirect(url_for('register_page'))

    return render_template('register.html')

# Ruta para la página de la tienda
@app.route('/store')
def store():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM productos;')
    productos = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('store.html', productos=productos)

# Ruta API para cerrar sesión
@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()  # Limpia todos los datos de la sesión
    return jsonify({'success': True, 'message': 'Sesión cerrada correctamente'})  # Respuesta JSON de éxito

# Ruta API para obtener todos los usuarios con más detalles (solo admin)
@app.route('/api/users', methods=['GET'])
@login_required
def get_users():
    if session.get('role_id') != 1:
        return jsonify({'error': 'No autorizado'}), 403
    success, message = auth.get_all_users()
    if success:
        return jsonify({'success': True, 'users': message})
    return jsonify({'success': False, 'message': message}), 400

# Ruta API para actualizar un usuario (solo admin)
@app.route('/api/users/<int:user_id>', methods=['PUT'])
@login_required
def update_user(user_id):
    if session.get('role_id') != 1:
        return jsonify({'error': 'No autorizado'}), 403
    data = request.json
    success, message = auth.update_user(
        user_id=user_id,
        username=data.get('username'),
        email=data.get('email'),
        role_id=data.get('role_id')
    )
    return jsonify({'success': success, 'message': message})

# Ruta API para eliminar un usuario (solo admin)
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    if session.get('role_id') != 1:
        return jsonify({'error': 'No autorizado'}), 403
    success, message = auth.delete_user(user_id)
    return jsonify({'success': success, 'message': message})

# Ruta para la página de administración (solo admin)
@app.route('/admin')
@login_required
def admin_page():
    if session.get('role_id') != 1:  # Verifica si el usuario es admin
        return jsonify({'error': 'No autorizado'}), 403
    return render_template('admin.html')  # Renderiza la plantilla admin.html

# Ruta API para hacer admin a un usuario (solo admin)
@app.route('/api/users/<int:user_id>/make_admin', methods=['POST'])
@login_required
def make_admin(user_id):
    if session.get('role_id') != 1:  # Verifica si el usuario es admin
        return jsonify({'error': 'No autorizado'}), 403
    # Actualiza el rol del usuario a admin (role_id = 1)
    success, message = auth.update_user_role(user_id, 1)
    return jsonify({'success': success, 'message': message})  # Retorna el resultado

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

# Ruta para la tienda
@app.route('/tienda')
def tienda():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM productos;')
    productos = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('store.html', productos=productos)

# Ruta para comprar un producto
@app.route('/comprar/<int:id>', methods=['POST'])
def comprar(id):
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        # Obtener la cantidad actual del producto
        cur.execute('SELECT cantidad FROM productos WHERE id = %s;', (id,))
        cantidad_actual = cur.fetchone()[0]
        
        if cantidad_actual > 0:
            # Restar 1 a la cantidad disponible
            nueva_cantidad = cantidad_actual - 1
            cur.execute('UPDATE productos SET cantidad = %s WHERE id = %s;', (nueva_cantidad, id))
            conn.commit()
            flash('¡Compra realizada con éxito!', 'success')
        else:
            flash('El producto está agotado.', 'error')
    
    except Exception as e:
        conn.rollback()
        flash('Ocurrió un error al procesar la compra.', 'error')
        print(f"Error: {e}")
    
    finally:
        cur.close()
        conn.close()
    
    return redirect(url_for('store'))

# Ruta para administrar productos (solo admin)
@app.route('/admin')
def admin():
    if not session.get('is_admin'):
        return redirect(url_for('tienda'))
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM productos;')
    productos = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('admin.html', productos=productos)

# Ruta para agregar un producto (solo admin)
@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    if not session.get('is_admin'):
        return redirect(url_for('tienda'))
    nombre = request.form['nombre']
    precio = float(request.form['precio'])
    cantidad = int(request.form['cantidad'])
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO productos (nombre, precio, cantidad) VALUES (%s, %s, %s);', (nombre, precio, cantidad))
    conn.commit()
    cur.close()
    conn.close()
    flash('Producto agregado correctamente', 'success')
    return redirect(url_for('admin'))

# Ruta para eliminar un producto (solo admin)
@app.route('/eliminar_producto/<int:id>')
def eliminar_producto(id):
    if not session.get('is_admin'):
        return redirect(url_for('tienda'))
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM productos WHERE id = %s;', (id,))
    conn.commit()
    cur.close()
    conn.close()
    flash('Producto eliminado correctamente', 'success')
    return redirect(url_for('admin'))

# Punto de entrada de la aplicación
# Inicia la aplicación en modo debug
if __name__ == '__main__':
    app.run(debug=True)