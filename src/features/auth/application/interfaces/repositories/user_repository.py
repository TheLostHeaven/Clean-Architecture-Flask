from abc import ABC, abstractmethod
from typing import Optional, List
from ....domain.entities.user import User

class IUserRepository(ABC):
    """Interface/Port para repositorio de usuarios"""
    
    @abstractmethod
    def save(self, user: User) -> User:
        """Guardar usuario"""
        pass
    
    @abstractmethod
    def find_by_id(self, user_id: str) -> Optional[User]:
        """Buscar usuario por ID"""
        pass
    
    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        """Buscar usuario por email"""
        pass
    
    @abstractmethod
    def find_by_username(self, username: str) -> Optional[User]:
        """Buscar usuario por username"""
        pass
    
    @abstractmethod
    def exists_by_email(self, email: str) -> bool:
        """Verificar si existe usuario con email"""
        pass
    
    @abstractmethod
    def exists_by_username(self, username: str) -> bool:
        """Verificar si existe usuario con username"""
        pass
    
    @abstractmethod
    def delete(self, user_id: str) -> bool:
        """Eliminar usuario"""
        pass
    
    @abstractmethod
    def update_last_login(self, user_id: str) -> None:
        """Actualizar último login"""
        pass
    
    @abstractmethod
    def add_refresh_token(self, user_id: str, token: str) -> None:
        """Agregar token de refresh"""
        pass
    
    @abstractmethod
    def remove_refresh_token(self, user_id: str, token: str) -> bool:
        """Remover token de refresh"""
        pass
    
    @abstractmethod
    def has_refresh_token(self, user_id: str, token: str) -> bool:
        """Verificar si usuario tiene token de refresh"""
        pass