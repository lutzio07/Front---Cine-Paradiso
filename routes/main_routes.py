from flask import Blueprint, render_template, request, current_app
from services.api_client import (
    obtener_pelicula_por_id, 
    obtener_peliculas,
    obtener_funciones,
    obtener_sucursales,
    )
from datetime import datetime
from requests.exceptions import RequestException

main_bp = Blueprint("main", __name__)

GENEROS_DISPONIBLES = [
    "Acción",
    "Animación",
    "Aventura",
    "Bélica",
    "Ciencia ficción",
    "Comedia",
    "Crimen",
    "Documental",
    "Drama",
    "Familia",
    "Fantasía",
    "Historia",
    "Misterio",
    "Música",
    "Oeste",
    "Película de TV",
    "Romance",
    "Suspenso",
    "Terror"
]
@main_bp.route("/")
def index():
    limite = current_app.config.get("PELICULAS_POR_PAGINA", 8)
    genero = request.args.get("genero", default=None, type=str)
    sucursal = request.args.get("sucursal", default=None, type=str)
    fecha = request.args.get("fecha", default=None, type=str)
    pagina = request.args.get("pagina", default=1, type=int)

    peliculas = []
    generos = []
    sucursales = []
    error = False
    try:
        peliculas = obtener_peliculas(genero=genero, sucursal=sucursal, fecha=fecha, pagina=pagina, limite=limite)
        generos = sorted({p.get("genero") for p in peliculas if p.get("genero")})
    except (RequestException, RuntimeError, ValueError):
        error = True
    
    hay_siguientes = (len(peliculas) == limite)

    return render_template(
        "pages/index.html",
        peliculas=peliculas,
        generos_disponibles=generos,
        error=error,
        pagina=pagina,
        hay_siguientes=hay_siguientes,
    )

@main_bp.route("/peliculas/<int:id_pelicula>")
def pelicula_detalle(id_pelicula):
    pelicula = None
    funciones = []
    error = False
    try:
        pelicula = obtener_pelicula_por_id(id_pelicula)
        if pelicula:
            funciones = obtener_funciones(id_pelicula, sucursal=request.args.get("sucursal"), fecha=request.args.get("fecha"))
    except (RequestException, RuntimeError, ValueError):
        error = True

    if error:
        return render_template("pages/pelicula_detalle.html", pelicula=pelicula, funciones=[], error=True), 503

    if not pelicula:
        return render_template("pages/pelicula_detalle.html", pelicula=None, funciones=[], error=False), 404
    
    return render_template("pages/pelicula_detalle.html", pelicula=pelicula, funciones=funciones)

@main_bp.app_template_filter("datetimeformat")
def datetimeformat(value, format="%d/%m/%Y %H:%M"):
    try:
        fecha = datetime.fromisoformat(value)
        return fecha.strftime(format)
    except (ValueError, TypeError):
        return value