# src/api/router.py
from flask import Flask
from typing import List, Dict, Optional, Callable

class FeatureRouter:
    """Router que registra todas las features"""
    
    def __init__(self, app: Flask):
        self.app = app
        self.registered_features: List[str] = []
    
    def register(self, feature_name: str, enabled: bool = True) -> bool:
        """Registrar una feature individual"""
        if not enabled:
            return False
        
        try:
            # Importar la feature
            module = __import__(
                f"src.features.{feature_name}",
                fromlist=['']
            )
            
            # Buscar blueprint con diferentes nombres posibles
            blueprint_names = [
                f'{feature_name}_bp',  # users_bp, products_bp, etc.
                'auth_bp',             # Especial para auth
                'api_bp',              # General
                'bp',                  # Simple
            ]
            
            blueprint = None
            for bp_name in blueprint_names:
                if hasattr(module, bp_name):
                    blueprint = getattr(module, bp_name)
                    break
            
            if blueprint:
                self.app.register_blueprint(blueprint)
                self.registered_features.append(feature_name)
                print(f"✅ Feature '{feature_name}' registrada")
                return True
            else:
                print(f"⚠️  Feature '{feature_name}' no tiene blueprint")
                return False
                
        except ImportError as e:
            print(f"❌ Feature '{feature_name}' no encontrada: {e}")
            return False
    
    def register_many(self, features_config: Dict[str, bool]) -> List[str]:
        """Registrar múltiples features"""
        successful = []
        for feature_name, enabled in features_config.items():
            if self.register(feature_name, enabled):
                successful.append(feature_name)
        return successful
    
    @property
    def features(self) -> List[str]:
        """Obtener features registradas"""
        return self.registered_features.copy()

# Función de conveniencia
def register_features(app: Flask, features: List[str]) -> List[str]:
    """
    Función helper para registrar features
    
    Args:
        app: Aplicación Flask
        features: Lista de nombres de features
        
    Returns:
        List[str]: Features registradas exitosamente
    """
    router = FeatureRouter(app)
    features_config = {name: True for name in features}
    return router.register_many(features_config)