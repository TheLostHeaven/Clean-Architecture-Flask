# src/features/auth/__init__.py
"""
Feature de Autenticación
"""

# Importar blueprint desde endpoints
try:
    from .presentation.api.v1.endpoints import auth_bp
    __all__ = ['auth_bp']
except ImportError as e:
    print(f"⚠️  Error importando auth_bp: {e}")
    auth_bp = None
    __all__ = []

    