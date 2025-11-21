from app.repositories.base_repository import BaseRepository
from app.models.database import PostModel
from sqlmodel import Session, select, or_
"""
Implementar búsqueda por término en título, contenido y categoría

Probar cada método del repositorio

"""

class PostRepository(BaseRepository):
    def __init__(self, session: Session):
        super().__init__(session, PostModel)
        
    
    def search_by_term(self, termino: str):
        termino = "%" + termino.lower() + "%"
        
        consulta = select(PostModel).where(
            or_(
                PostModel.title.ilike(termino),
                PostModel.content.ilike(termino),
                PostModel.category.ilike(termino)
            )
            
        )
        
        resultado = self.session.exec(consulta)
        return resultado.all()
        