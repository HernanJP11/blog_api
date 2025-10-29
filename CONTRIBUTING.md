# 🤝 Guía de Contribución - Blog API

## 📋 Convenciones de Código

### Estilo de Código Python

- Seguir **PEP 8**
- Líneas máximo 88 caracteres (Black)
- Usar **type hints** en todas las funciones
- Docstrings en formato Google

### Ejemplo de función con type hints:
```python
from typing import List, Optional

def get_posts(
    skip: int = 0, 
    limit: int = 100
) -> List[Post]:
    """
    Obtiene una lista de posts.
    
    Args:
        skip: Número de registros a saltar
        limit: Número máximo de registros
        
    Returns:
        Lista de objetos Post
    """
    pass
```

## 🏗️ Estructura por Capas
```
app/
├── api/          # Endpoints y rutas
├── services/     # Lógica de negocio
├── models/       # Modelos de base de datos
├── schemas/      # Validación con Pydantic
├── repositories/ # Acceso a datos
└── core/         # Configuración y utilidades
```

## 📝 Commits

Seguir **Conventional Commits**:

- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Documentación
- `refactor:` Refactorización
- `test:` Tests
- `chore:` Tareas de mantenimiento

Ejemplos:
```bash
git commit -m "feat: Add POST /posts endpoint"
git commit -m "fix: Resolve database connection timeout"
git commit -m "docs: Update API documentation"
```

## 🧪 Testing

- Cobertura mínima: 80%
- Tests unitarios para services
- Tests de integración para endpoints

## 📦 Dependencias

Actualizar `requirements.txt` cuando agregues nuevas dependencias:
```bash
pip freeze > requirements.txt
```