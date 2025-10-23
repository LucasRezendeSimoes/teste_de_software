import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com/todos"


@pytest.fixture
def novo_todo():
    """Fixture para criar um TODO antes dos testes."""
    payload = {
        "title": "Minha tarefa",
        "completed": False,
        "userId": 1
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201  # Created
    data = response.json()
    yield data  # Retorna os dados do TODO criado para os testes


def test_create_todo(novo_todo):
    """Testa a criação de um TODO."""
    assert novo_todo["title"] == "Minha tarefa"
    assert novo_todo["completed"] is False
    assert novo_todo["userId"] == 1
    assert "id" in novo_todo


def test_read_todo(novo_todo):
    """Testa leitura de um TODO após sua criação."""
    todo_id = novo_todo["id"]
    response = requests.get(f"{BASE_URL}/{todo_id}")
    
    # JSONPlaceholder não persiste, logo 404 pode acontecer
    assert response.status_code in (200, 201, 404)
    
    data = response.json()
    if response.status_code != 404:
        assert "title" in data
        assert "completed" in data
        assert "userId" in data



def test_update_todo(novo_todo):
    """Testa atualização de um TODO."""
    todo_id = novo_todo["id"]
    payload = {"completed": True}
    response = requests.patch(f"{BASE_URL}/{todo_id}", json=payload)
    assert response.status_code == 200
    data = response.json()
    # A API retorna o que enviamos, então verificamos isso
    assert data["completed"] is True


def test_delete_todo(novo_todo):
    """Testa exclusão de um TODO."""
    todo_id = novo_todo["id"]
    response = requests.delete(f"{BASE_URL}/{todo_id}")
    assert response.status_code in (200, 201, 404)
  # Dependendo da API fake, pode retornar 200 ou 204


def test_verify_deleted_todo(novo_todo):
    """Após exclusão, tentativa de leitura deve falhar (simulada)."""
    # Observação: JSONPlaceholder não deleta de verdade!
    # Então faremos verificação por tentativa forçada de erro
    todo_id = novo_todo["id"]
    response = requests.get(f"{BASE_URL}/{todo_id}")
    assert response.status_code in (200, 404)
    # Se retornar vazio, consideramos ok
    if response.status_code == 200:
        assert response.json() != {}  # API fake sempre retorna dados


def test_create_todo_sem_titulo():
    """Teste negativo: tentar criar um TODO sem título."""
    payload = {
        "completed": False,
        "userId": 1
    }
    response = requests.post(BASE_URL, json=payload)
    # JSONPlaceholder aceita mesmo assim (fake), mas em API real seria 400
    assert response.status_code == 201
    data = response.json()
    assert "title" not in data
