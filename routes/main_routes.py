from flask import Blueprint, render_template
from services.api_client import obtener_pelicula_por_id, obtener_peliculas

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    peliculas = obtener_peliculas()
    return render_template("pages/index.html", peliculas=peliculas)

@main_bp.route("/pelicula/<int:id_pelicula>")
def pelicula_detalle(id_pelicula):
    pelicula = obtener_pelicula_por_id(id_pelicula)
    if not pelicula:
        return render_template("pages/404.html"), 404
    return render_template("pages/pelicula_detalle.html", pelicula=pelicula)
