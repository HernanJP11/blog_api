import pytest
from sqlmodel import Session, create_engine, SQLModel, Field
from app.repositories.base_repository import BaseRepository 

class TestModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    value: int
    
engine = create_engine("sqlite:///:memory:", echo=True,)  # Muestra en consola las consultas SQL)


@pytest.fixture
def test_session():
    # 1. CREAR TABLAS antes del test
    SQLModel.metadata.create_all(engine)
    
    # 2. CREAR SESIÓN para el test
    with Session(engine) as session:
        yield session  # ← Esta sesión se usa en el test
        
@pytest.fixture
def test_model():
    return TestModel  # ← Retorna la clase, no una instancia


@pytest.fixture
def repository(test_session, test_model):
    return BaseRepository(
        session=test_session,  # ← Sesión de fixture anterior
        model=test_model       # ← Modelo de fixture anterior
    )