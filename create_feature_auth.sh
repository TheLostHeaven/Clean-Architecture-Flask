#!/bin/bash
# scripts/create_feature_auth.sh

echo "🚀 Creando feature auth completa..."

# Crear estructura de directorios
mkdir -p src/features/auth
mkdir -p src/features/auth/domain/entities
mkdir -p src/features/auth/domain/value_objects
mkdir -p src/features/auth/domain/services
mkdir -p src/features/auth/domain/exceptions
mkdir -p src/features/auth/domain/events
mkdir -p src/features/auth/application/use_cases
mkdir -p src/features/auth/application/interfaces/repositories
mkdir -p src/features/auth/application/interfaces/services
mkdir -p src/features/auth/application/dto
mkdir -p src/features/auth/application/mappers
mkdir -p src/features/auth/infrastructure/repositories
mkdir -p src/features/auth/infrastructure/services/security
mkdir -p src/features/auth/infrastructure/models
mkdir -p src/features/auth/presentation/api/v1/endpoints
mkdir -p src/features/auth/presentation/api/v1/schemas
mkdir -p src/features/auth/presentation/api/v1/dependencies

# Crear todos los archivos
touch src/features/auth/__init__.py
touch src/features/auth/domain/__init__.py
touch src/features/auth/domain/entities/__init__.py
touch src/features/auth/domain/value_objects/__init__.py
touch src/features/auth/domain/services/__init__.py
touch src/features/auth/domain/exceptions/__init__.py
touch src/features/auth/domain/events/__init__.py
touch src/features/auth/application/__init__.py
touch src/features/auth/application/use_cases/__init__.py
touch src/features/auth/application/interfaces/__init__.py
touch src/features/auth/application/interfaces/repositories/__init__.py
touch src/features/auth/application/interfaces/services/__init__.py
touch src/features/auth/application/dto/__init__.py
touch src/features/auth/application/mappers/__init__.py
touch src/features/auth/infrastructure/__init__.py
touch src/features/auth/infrastructure/repositories/__init__.py
touch src/features/auth/infrastructure/services/__init__.py
touch src/features/auth/infrastructure/services/security/__init__.py
touch src/features/auth/infrastructure/models/__init__.py
touch src/features/auth/presentation/__init__.py
touch src/features/auth/presentation/api/__init__.py
touch src/features/auth/presentation/api/v1/__init__.py
touch src/features/auth/presentation/api/v1/endpoints/__init__.py
touch src/features/auth/presentation/api/v1/schemas/__init__.py
touch src/features/auth/presentation/api/v1/dependencies/__init__.py

echo "✅ Feature auth creada!"
echo "📁 Estructura: src/features/auth/"
echo ""
echo "📝 Archivos creados:"
find src/features/auth -name "*.py" | wc -l
echo "📦 Para usarla, agrega al container principal"