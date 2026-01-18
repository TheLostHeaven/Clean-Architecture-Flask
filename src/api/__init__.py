# src/api/__init__.py
"""
Módulo principal de la API
"""
from .router import FeatureRouter, register_features

__all__ = ['FeatureRouter', 'register_features']