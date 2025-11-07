from sqlmodel import SQLModel, create_engine, Session
# URL de conexión a SQLite
DATABASE_URL = "sqlite:///./blog.db"

# Crear el motor de conexión
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Muestra en consola las consultas SQL
    connect_args={"check_same_thread": False}  # Necesario para SQLite en modo local
)

def init_db() -> None:
    """Inicializa la base de datos creando las tablas si no existen."""
    SQLModel.metadata.create_all(engine)
    
def get_session():
    with Seccion(engine) as session:
        yield session
