
# PASO 1: Crear rutas, debes de importar  (solo se hace 1 vez)
from flask import jsonify, Blueprint 
from mocks.empleado_mock import empleados
from controllers.empleado_controller import mostrarTodosEmpleados, mostrarEmpleadosCasados

# PASO 2: Tienes que instanciar tu Blueprint (solo se hace 1 vez)
empleado_routes = Blueprint('empleado_routes', __name__)  #Esto me permite crear mis rutas

#PASO 3: Crear nuestra ruta pesonalizada
# Debes de usar la variable donde instanciaste (almacenaste) Blueprint
# Para crear tu primera ruta debes de iniciar con un @

# @instancia.route('/nombreruta', methods=['GET'])
@empleado_routes.route('/hola_mundo', methods=['GET'])
# Ahora pongo la funcion que se ejecutara cuando entre a esta ruta
def hola_mundo():
   # El backend siempre debe de responder a las peticiones del cliente
   # 😁 SIEMPRE debes de retornar usando jsonify -> para que te funcione debes de importarlo
   # Se importa poniendolo al costado del Blueprint
    return jsonify(
        {
            "mensage": "Hola mundo"
        }
    )

@empleado_routes.route('/empleados_casados', methods=['GET'])
def get_empleados_casados():
    empleados_casados = mostrarEmpleadosCasados()
    return jsonify(
        {
            "data": empleados_casados,
            "count": len(empleados_casados)
        }
    )

@empleado_routes.route('/empleados', methods=['GET'])
def obtener_empleados():
    empleados = mostrarTodosEmpleados()
    return jsonify({
        "empleados" : empleados
    })

