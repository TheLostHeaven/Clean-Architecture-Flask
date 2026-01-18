from dataclasses import dataclass
from typing import Optional
import re
from ...domain.exceptions.auth_exceptions import WeakPasswordException

@dataclass(frozen=True)
class Password:
    """Value Object para password en texto plano (solo para validación)"""
    value: str
    
    def __post_init__(self):
        self.validate_strength()
    
    def validate_strength(self):
        """Validar fortaleza del password"""
        if len(self.value) < 8:
            raise WeakPasswordException("Password must be at least 8 characters long")
        
        if not re.search(r'[A-Z]', self.value):
            raise WeakPasswordException("Password must contain at least one uppercase letter")
        
        if not re.search(r'[a-z]', self.value):
            raise WeakPasswordException("Password must contain at least one lowercase letter")
        
        if not re.search(r'[0-9]', self.value):
            raise WeakPasswordException("Password must contain at least one number")
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', self.value):
            raise WeakPasswordException("Password must contain at least one special character")
    
    def __str__(self) -> str:
        return "[PROTECTED]"  # Nunca exponer el password real