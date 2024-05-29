from flask import Flask, render_template
from view_web import vista_menu

import sys
sys.path.append("prueba_import")

app  = Flask(__name__)
app.register_blueprint(vista_menu.ruta_menu)

if __name__ == '__main__':
    app.run( debug=True )