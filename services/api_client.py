import os
import requests
from flask import current_app

class APIClient:
    """
    Cliente HTTP centralizado en Python utilizando la librería 'requests'.
    Cumple estrictamente con la restricción de la cátedra de NO realizar peticiones
    desde el navegador (Cero fetch/axios/AJAX en JS). Toda interacción con la API
    backend pasa por el servidor Flask del Frontend.
    """

    @classmethod
    def _get_backend_url(cls):
        return current_app.config.get("BACKEND_URL", "http://localhost:5000/api")

    @classmethod
    def get(cls, endpoint, params=None, headers=None):
        try:
            url = f"{cls._get_backend_url()}{endpoint}"
            response = requests.get(url, params=params, headers=headers, timeout=5)
            if response.status_code == 200:
                return response.json()
            return {"status": "error", "message": f"Error HTTP {response.status_code}"}
        except requests.exceptions.RequestException as e:
            print(f"[APIClient GET Error]: {e}")
            return {"status": "error", "message": "No se pudo conectar con el servidor backend"}

    @classmethod
    def post(cls, endpoint, data=None, headers=None):
        try:
            url = f"{cls._get_backend_url()}{endpoint}"
            response = requests.post(url, json=data, headers=headers, timeout=5)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"[APIClient POST Error]: {e}")
            return {"status": "error", "message": "No se pudo conectar con el servidor backend"}

    # --- MÉTODOS DE NEGOCIO ---
    @classmethod
    def obtener_peliculas(cls):
        res = cls.get("/peliculas")
        if res.get("status") == "success":
            return res.get("data", [])
        return []

    @classmethod
    def obtener_pelicula_por_id(cls, id_pelicula):
        res = cls.get(f"/peliculas/{id_pelicula}")
        if res.get("status") == "success":
            return res.get("data")
        return None
