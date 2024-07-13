import json
import os

def traer_data_JSON():
    # Obtener la ruta al archivo actual
    current_dir = os.path.dirname(__file__)
    
    # Construir la ruta al archivo data.json
    file_path = os.path.join(current_dir, 'data.json')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f'Archivo no encontrado en la ruta: {file_path}')
        return {}  # Devolver un valor predeterminado o manejar el error según sea necesario
    except Exception as e:
        print(f'Ocurrió un error al leer el archivo JSON: {str(e)}')
        return {}  # Manejar otros errores de lectura de archivo JSON
