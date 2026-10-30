import os
from dotenv import load_dotenv

load_dotenv()


def get_config():
    return {
        "SECRET_KEY": os.getenv("SECRET_KEY", "default_frontend_secret"),
        "BACKEND_URL": os.getenv("BACKEND_URL", "http://localhost:5000/api"),
        "PELICULAS_POR_PAGINA": int(os.getenv("PELICULAS_POR_PAGINA", 8)),
    }
