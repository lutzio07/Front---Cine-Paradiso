from flask import Blueprint, render_template, request
from services.api_client import (
    obtener_pelicula_por_id, 
    obtener_peliculas,
    obtener_funciones,
    )
from datetime import datetime
from requests.exceptions import RequestException

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    genero = request.args.get("genero", default=None, type=str)
    sucursal = request.args.get("sucursal", default=None, type=str)
    fecha = request.args.get("fecha", default=None, type=str)
    page = request.args.get("page", default=1, type=int)

    peliculas = []
    generos = []
    error = False
    try:
        peliculas = obtener_peliculas(genero=genero, sucursal=sucursal, fecha=fecha, page=page)
        generos = sorted({p.get("genero") for p in peliculas if p.get("genero")})
    except (RequestException, RuntimeError, ValueError):
        error = True

    return render_template(
        "pages/index.html",
        peliculas=peliculas,
        generos_disponibles=generos,
        error=error,
        request=request,
        page=page,
    )

@main_bp.route("/pelicula/<int:id_pelicula>")
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
def datetimeformat(value, format="%Y/%m/%d %H:%M"):
    try:
        fecha = datetime.fromisoformat(value)
        return fecha.strftime(format)
    except (ValueError, TypeError):
        return value