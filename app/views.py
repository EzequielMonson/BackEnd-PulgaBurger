from app.database import *

def traer_hamburguesas_carne():
    data = traer_data_JSON()
    nueva_data = []
    for dato in data:
        if dato['type'] == 'burger':
            nueva_data.append(dato)
    return nueva_data

def traer_hamburguesas_vegan():
    data = traer_data_JSON()
    nueva_data = []
    for dato in data:
        if dato['type'] == 'burger-vegan':
            nueva_data.append(dato)
    return nueva_data

def traer_acompañamientos():
    data = traer_data_JSON()
    nueva_data = []
    for dato in data:
        if dato['type'] == 'other':
            nueva_data.append(dato)
    return nueva_data