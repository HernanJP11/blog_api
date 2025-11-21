import pytest
from tests.conftest import TestModel



def test_create_success(repository, test_session):
    # 1. CREAR datos de prueba
    test_obj = TestModel(name="Test", value=100)
    
    # 2. EJECUTAR create()
    result = repository.create(test_obj)
    
    # 3. VERIFICAR que tiene ID asignado
    assert result.id is not None
    
    # 4. VERIFICAR que los datos son correctos
    assert result.name == "Test"
    assert result.value == 100
    
    # 5. VERIFICAR que está en BD (opcional)
    db_obj = test_session.get(TestModel, result.id)
    assert db_obj is not None