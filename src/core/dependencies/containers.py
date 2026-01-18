# src/core/dependencies/containers.py
from dependency_injector import containers, providers
from src.features.auth.infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from src.features.auth.infrastructure.services.security.password_hasher import PasswordHasher
from src.features.auth.infrastructure.services.security.jwt_handler import JWTService
from src.features.auth.application.use_cases.login_user import LoginUserUseCase
from src.features.auth.application.use_cases.register_user import RegisterUserUseCase
# from src.features.auth.application.use_cases.refresh_token import RefreshTokenUseCase
# from src.features.auth.application.use_cases.logout_user import LogoutUserUseCase
# from src.features.auth.application.use_cases.verify_token import VerifyTokenUseCase

class AuthContainer(containers.DeclarativeContainer):
    """Contenedor para feature auth"""
    
    # Dependencias compartidas
    config = providers.Configuration()
    db_session = providers.Dependency()
    
    # Repositorios
    user_repository = providers.Factory(
        UserRepositoryImpl,
        db_session=db_session
    )
    
    # Servicios
    password_hasher = providers.Singleton(
        PasswordHasher,
        algorithm=config.auth.password_algorithm
    )
    
    jwt_service = providers.Singleton(
        JWTService,
        secret_key=config.auth.jwt_secret_key,
        algorithm=config.auth.jwt_algorithm,
        issuer=config.auth.jwt_issuer,
        audience=config.auth.jwt_audience
    )
    
    # Casos de uso
    login_use_case = providers.Factory(
        LoginUserUseCase,
        user_repository=user_repository,
        token_service=jwt_service,
        password_hasher=password_hasher
    )
    
    register_use_case = providers.Factory(
        RegisterUserUseCase,
        user_repository=user_repository,
        password_hasher=password_hasher
    )
    
    # refresh_token_use_case = providers.Factory(
    #     RefreshTokenUseCase,
    #     user_repository=user_repository,
    #     token_service=jwt_service
    # )
    
    # logout_use_case = providers.Factory(
    #     LogoutUserUseCase,
    #     user_repository=user_repository,
    #     token_service=jwt_service
    # )
    
    # verify_token_use_case = providers.Factory(
    #     VerifyTokenUseCase,
    #     token_service=jwt_service
    # )

class MainContainer(containers.DeclarativeContainer):
    """Contenedor principal"""
    
    # Configuración
    config = providers.Configuration()
    
    # Database session (compartida entre features)
    db_session = providers.Dependency()
    
    # Features
    auth = providers.Container(AuthContainer, db_session=db_session, config=config.auth)