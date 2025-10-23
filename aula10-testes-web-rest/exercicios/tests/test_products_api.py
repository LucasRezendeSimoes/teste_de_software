import requests
import jsonschema
from jsonschema import validate

BASE_URL = "https://fakestoreapi.com/products"

# Schema básico esperado para um produto da API
product_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "price": {"type": "number"},
        "description": {"type": "string"},
        "category": {"type": "string"},
        "image": {"type": "string"},
        "rating": {
            "type": "object",
            "properties": {
                "rate": {"type": "number"},
                "count": {"type": "integer"},
            },
            "required": ["rate", "count"]
        }
    },
    "required": ["id", "title", "price", "description", "category", "image", "rating"]
}

def test_listar_produtos():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert "title" in data[0]


def test_buscar_produto_por_id():
    product_id = 1
    response = requests.get(f"{BASE_URL}/{product_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == product_id


def test_filtrar_produtos_por_categoria():
    categoria = "electronics"
    response = requests.get(f"{BASE_URL}/category/{categoria}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    # Verifica se todos os produtos retornados pertencem à categoria
    for product in data:
        assert product["category"] == categoria


def test_validar_schema_resposta():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    data = response.json()
    # Valida o primeiro produto do retorno contra o schema
    validate(instance=data[0], schema=product_schema)


def test_limite_de_produtos_retornados():
    limit = 5
    response = requests.get(f"{BASE_URL}?limit={limit}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == limit
