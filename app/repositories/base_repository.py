from sqlmodel import SQLModel, Session, select
from sqlalchemy.exc import OperationalError, DataError, SQLAlchemyError
from app.exceptions.exceptions import DatabaseConnectionError, PostNotFoundError
from typing import Type, Optional, List

class BaseRepository:
    def __init__(self, session: Session, model: Type[SQLModel]): #Aprender Type Hint
        self.session = session
        self.model = model
    
    
    
    def get_by_id(self, id: int) -> Optional[SQLModel]:
        object_db = self.session.get(self.model, id)
        # Si no se encuentra, lanzar excepción
        if not object_db:
            raise PostNotFoundError("Error el post a actualizar no existe")
        
        return object_db
    
    
    def get_all(self) -> List[SQLModel]:
        list_object = self.session.exec(select(self.model)).all()
        return list_object
    
    
    def create(self, obj: SQLModel) -> SQLModel:
        try:
            self.session.add(obj)
            self.session.commit()
            self.session.refresh(obj)
            return obj
        
        except OperationalError as e:
            self.session.rollback()
            raise DatabaseConnectionError("No se pudo conectar a la base de datos")
        except DataError as e:
            self.session.rollback()
            raise InvalidDataError("Los datos proporcionados no son válidos.")
        except SQLAlchemyError:
            # Cualquier otro error general del ORM
            self.session.rollback()
            raise DatabaseError("Error desconocido en la base de datos.")
            
        
    
    
    def update(self, id: int, obj_update: SQLModel) -> Optional[SQLModel]:
        # Buscar el objeto en la base de datos
        object_db = self.session.get(self.model, id)
    
        # Si no se encuentra, lanzar excepción
        if not object_db:
            raise PostNotFoundError("Error el post a actualizar no existe")
        
        try:
            for campo, valor in object_update.__dict__.items():
                if valor is not None:
                    setattr(object_db, campo, valor)        
            self.session.commit()
            self.session.refresh(object_db)
            return object_db
        
        except OperationalError as e:
            self.session.rollback()
            raise DatabaseConnectionError("No se pudo conectar a la base de datos")
        except DataError as e:
            self.session.rollback()
            raise InvalidDataError("Los datos proporcionados no son válidos.")
        except SQLAlchemyError:
            # Cualquier otro error general del ORM
            self.session.rollback()
            raise DatabaseError("Error desconocido en la base de datos.")
    
    
    
    
    def delete(self, id: int) -> bool:
        object_db = self.session.get(self.model, id)
        
        # Si no se encuentra, lanzar excepción
        if not object_db:
            raise PostNotFoundError("Error el post a eliminar no existe")
        
        try:
            self.session.delete(object_db)
            self.session.commit()
            return True
        
        
        except OperationalError as e:
            self.session.rollback()
            raise DatabaseConnectionError("No se pudo conectar a la base de datos")
        except DataError as e:
            self.session.rollback()
            raise InvalidDataError("Los datos proporcionados no son válidos.")
        except SQLAlchemyError:
            # Cualquier otro error general del ORM
            self.session.rollback()
            raise DatabaseError("Error desconocido en la base de datos.")
    
    # hacer pruebas