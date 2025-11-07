from pydantic import BaseModel
from datetime import datetime

# Schema base con campos en comun de creacion y respuesta
class PostBase(BaseModel):
    title : str
    content: str
    category: str
    tags : List[str] | None = None
    
# Schema para creacion
class PostCreate(PostBase):
    pass

# Schema para respuesta
class PostResponse(PostBase):
    id : int 
    created_at: datetime
    updated_at: datetime
    
# Schema para actualizar
class PostUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    category : str | None = None
    tags: lis[str] | None = None