from flask import Blueprint
from flask import request, jsonify
from flask import render_template
from controller.BD import BD 

BaseDatos = BD()

ruta_menu = Blueprint( "HolaMundo", __name__, "templates")

@ruta_menu.route("/")
def Menu():
    return render_template("menu.html")

@ruta_menu.route("/tablero")
def Tablero():
    return render_template("tablero.html")

@ruta_menu.route("/tablero", methods=['POST'])
def Tablero_fin():
    data = request.json
    ganador = data.get('winner')
    if ganador == 'usuario':
        BaseDatos.insert_victoria_jugador()
        BaseDatos.insert_derrota_ia()
        print("El jugador ha ganado")
    elif ganador == 'IA':
        BaseDatos.insert_victoria_ia()
        BaseDatos.insert_derrota_jugador()
        print("La IA ha ganado")
    return jsonify({'status': 'success'})

@ruta_menu.route("/estadisticas")
def Estadisticas():
    datos = BaseDatos.obtener_estadisticas()
    return render_template("estadisticas.html", data = datos)
