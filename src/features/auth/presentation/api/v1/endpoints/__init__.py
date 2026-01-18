# src/features/auth/presentation/api/v1/endpoints/__init__.py
from flask import Blueprint

# Crear blueprint principal para auth
auth_bp = Blueprint(
    'auth',
    __name__,
    url_prefix='/api/v1/auth'
)

# Importar TODAS las rutas después de crear el blueprint
# para evitar circular imports
from .auth import *

__all__ = ['auth_bp']