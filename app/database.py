import json


def traer_data_JSON():
    file_path = 'data.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data