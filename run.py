from flask import Flask
from flask_cors import CORS
from app.views import *

app = Flask(__name__)
CORS(app)
app.route('/carne', methods=['GET'])(traer_hamburguesas_carne)
app.route('/vegan', methods=['GET'])(traer_hamburguesas_vegan)
app.route('/acompañamientos', methods=['GET'])(traer_acompañamientos)


if __name__ == '__main__':
    app.run(debug=True)
    