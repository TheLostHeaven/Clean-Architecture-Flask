import bcrypt
from argon2 import PasswordHasher as Argon2Hasher
from argon2.exceptions import VerifyMismatchError, InvalidHashError
from typing import Tuple
import os

class PasswordHasher:
    """Servicio para hashing y verificación de passwords"""
    
    def __init__(self, algorithm: str = "argon2"):
        self.algorithm = algorithm
        if algorithm == "argon2":
            self.argon2_hasher = Argon2Hasher(
                time_cost=2,
                memory_cost=102400,
                parallelism=8,
                hash_len=32,
                salt_len=16
            )
    
    def hash(self, password: str) -> Tuple[str, str]:
        """
        Hash de password
        
        Returns:
            Tuple[str, str]: (hashed_password, algorithm_used)
        """
        if self.algorithm == "bcrypt":
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password.encode(), salt)
            return hashed.decode(), "bcrypt"
        
        elif self.algorithm == "argon2":
            hashed = self.argon2_hasher.hash(password)
            return hashed, "argon2"
        
        else:
            raise ValueError(f"Unsupported algorithm: {self.algorithm}")
    
    def verify(self, password: str, hashed_password: str) -> bool:
        """
        Verificar password contra hash
        
        Args:
            password: Password en texto plano
            hashed_password: Hash almacenado
            
        Returns:
            bool: True si el password es válido
        """
        # Detectar algoritmo por el formato del hash
        if hashed_password.startswith("$2b$") or hashed_password.startswith("$2a$"):
            # bcrypt
            try:
                return bcrypt.checkpw(password.encode(), hashed_password.encode())
            except ValueError:
                return False
        
        elif hashed_password.startswith("$argon2"):
            # argon2
            try:
                self.argon2_hasher.verify(hashed_password, password)
                return True
            except (VerifyMismatchError, InvalidHashError):
                return False
        
        else:
            # Hash desconocido
            return False
    
    def needs_rehash(self, hashed_password: str) -> bool:
        """
        Verificar si necesita re-hash (para migración de algoritmos)
        """
        if self.algorithm == "argon2":
            return self.argon2_hasher.check_needs_rehash(hashed_password)
        
        # Para bcrypt, siempre retornar False (no tiene método de verificación)
        return False
    
    def generate_salt(self) -> str:
        """Generar sal aleatoria"""
        return os.urandom(16).hex()