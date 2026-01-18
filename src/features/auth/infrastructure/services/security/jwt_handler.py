# src/features/auth/infrastructure/services/security/jwt_handler.py
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
from jose import JWTError, jwt
from jose.exceptions import JWTError, ExpiredSignatureError
from ....application.interfaces.services.token_service import ITokenService

class JWTService(ITokenService):
    """Implementación del servicio de tokens JWT usando python-jose"""
    
    def __init__(
        self,
        secret_key: str,
        algorithm: str = "HS256",
        issuer: Optional[str] = None,
        audience: Optional[str] = None
    ):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.issuer = issuer
        self.audience = audience
    
    def create_access_token(self, data: Dict[str, Any], expires_in: int = 900) -> str:
        """Crear access token JWT"""
        to_encode = data.copy()
        
        # Agregar claims estándar
        now = datetime.utcnow()
        expire = now + timedelta(seconds=expires_in)
        
        to_encode.update({
            "exp": expire,
            "iat": now,
            "nbf": now,
            "type": "access"
        })
        
        if self.issuer:
            to_encode["iss"] = self.issuer
        if self.audience:
            to_encode["aud"] = self.audience
        
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
    
    def create_refresh_token(self, data: Dict[str, Any], expires_in: int = 2592000) -> str:
        """Crear refresh token JWT"""
        to_encode = data.copy()
        
        now = datetime.utcnow()
        expire = now + timedelta(seconds=expires_in)
        
        to_encode.update({
            "exp": expire,
            "iat": now,
            "nbf": now,
            "type": "refresh"
        })
        
        if self.issuer:
            to_encode["iss"] = self.issuer
        if self.audience:
            to_encode["aud"] = self.audience
        
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
    
    def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Verificar y decodificar token"""
        try:
            payload = jwt.decode(
                token,
                self.secret_key,
                algorithms=[self.algorithm],
                issuer=self.issuer,
                audience=self.audience,
                options={
                    "verify_exp": True,
                    "verify_iss": bool(self.issuer),
                    "verify_aud": bool(self.audience),
                    "verify_signature": True
                }
            )
            return payload
        except (JWTError, ExpiredSignatureError):
            return None
    
    def decode_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Decodificar token sin verificar"""
        try:
            return jwt.decode(
                token,
                self.secret_key,
                algorithms=[self.algorithm],
                options={"verify_signature": False}
            )
        except JWTError:
            return None
    
    def is_token_expired(self, token: str) -> bool:
        """Verificar si token está expirado"""
        payload = self.decode_token(token)
        if not payload or "exp" not in payload:
            return True
        
        expiry = datetime.fromtimestamp(payload["exp"])
        return expiry < datetime.utcnow()
    
    def get_token_expiry(self, token: str) -> Optional[datetime]:
        """Obtener fecha de expiración del token"""
        payload = self.decode_token(token)
        if payload and "exp" in payload:
            return datetime.fromtimestamp(payload["exp"])
        return None