from sqlmodel import SQLModel

class BaseRepository:
    def __init__(self, session: Session, model: Type[SQLModel]): #Aprender Type Hint
        self.session = session
        self.model = model
    
    
    
    def get_by_id(self, id: int) -> Optional[SQLModel]:
        pass
    def get_all(self) -> List[SQLModel]:
        pass
    
    def create(self, obj: SQLModel) -> SQLModel:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj
    
    
    def update(self, id: int, obj_update: SQLModel) -> Optional[SQLModel]:
        object_db = self.session.get(self.model, id)
        for campo, valor in object_update.__dict__.items():
            if valor is not None:
                setattr(object_db, campo, valor)        
        self.session.commit()
        self.session.refresh(object_db)
        return object_db
    
    
    def delete(self, id: int) -> bool:
        pass