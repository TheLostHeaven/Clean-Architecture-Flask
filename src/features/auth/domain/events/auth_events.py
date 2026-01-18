from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class AuthEvent:
    """Evento base de autenticación"""
    event_type: str
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.utcnow()

@dataclass
class UserRegisteredEvent(AuthEvent):
    """Evento: Usuario registrado"""
    event_type: str = "user.registered"
    user_id: str = None
    email: str = None
    username: str = None

@dataclass
class UserLoggedInEvent(AuthEvent):
    """Evento: Usuario hizo login"""
    event_type: str = "user.logged_in"
    user_id: str = None
    email: str = None

@dataclass
class UserLoggedOutEvent(AuthEvent):
    """Evento: Usuario hizo logout"""
    event_type: str = "user.logged_out"
    user_id: str = None

@dataclass
class PasswordChangedEvent(AuthEvent):
    """Evento: Password cambiado"""
    event_type: str = "user.password_changed"
    user_id: str = None

@dataclass
class EmailVerifiedEvent(AuthEvent):
    """Evento: Email verificado"""
    event_type: str = "user.email_verified"
    user_id: str = None