from mocks.empleado_mock import empleados

def mostrarTodosEmpleados():
    return empleados

def mostrarEmpleadosCasados():
    empleados_casados = []
    for empleado in empleados:
        if empleado['estado_civil'] == 'casado' and empleado['genero'] == 'masculino':
            empleados_casados.append(empleado)

    return empleados_casados