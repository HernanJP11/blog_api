"""
Crear repositorio base con operaciones CRUD genéricas

Implementar PostRepository específico:

Create: Insertar nuevo post

Read: Obtener por ID y obtener todos

Update: Actualizar post existente

Delete: Eliminar post

Implementar búsqueda por término en título, contenido y categoría

Probar cada método del repositorio

Resultado esperado: Capa de datos completamente funcional y testeada.
"""
from sqlmodel import Session

class PostRepository():
    pass