from flask import Blueprint, render_template, request, redirect, url_for
from services.api_client import APIClient

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    """
    Página principal / Cartelera de películas retro.
    Obtiene los datos consumiendo el backend vía Python requests.
    """
    peliculas = APIClient.obtener_peliculas()
    return render_template("pages/index.html", peliculas=peliculas)

@main_bp.route("/pelicula/<int:id_pelicula>")
def pelicula_detalle(id_pelicula):
    """
    Ficha de detalle de una película seleccionada.
    """
    pelicula = APIClient.obtener_pelicula_por_id(id_pelicula)
    if not pelicula:
        return render_template("pages/404.html"), 404
    return render_template("pages/pelicula_detalle.html", pelicula=pelicula)
