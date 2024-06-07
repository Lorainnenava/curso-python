# Ejemplo con lista
employee_list = [
    {"id": 12345, "name": "John", "department": "Kitchen"},
    {"id": 12458, "name": "Paul", "department": "House Floor"},
]


def get_employee(id):
    for employee in employee_list:
        if employee["id"] == id:
            return employee


print(get_employee(12458))

## OUTPUT
{"id": 12458, "name": "Paul", "department": "House Floor"}

# Ejemplo con diccionario
employee_dict = {
    12345: {"id": "12345", "name": "John", "department": "Kitchen"},
    12458: {"id": "12458", "name": "Paul", "department": "House Floor"},
}


def get_employee_from_dict(id):
    return employee_dict[id]


print(get_employee_from_dict(12458))
## OUTPUT
{"id": 12458, "name": "Paul", "department": "House Floor"}

# Ambas funcionan bien, pero el equilibrio a considerar es el tiempo y
# la escala. La primera solución funcionará bien para cantidades pequeñas
# de datos, pero pierde rendimiento a medida que los datos aumentan.
# La segunda solución es más adecuada para grandes cantidades de datos,
# ya que su estructura permite un tiempo de búsqueda constante y de ese
# modo acceder a grandes cantidades de datos a una velocidad constante.
