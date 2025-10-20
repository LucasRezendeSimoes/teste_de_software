import requests
import pytest
BASE_URL = "https://jsonplaceholder.typicode.com"
def test_create():
    """Teste CREATE - valida que POST retorna 201"""
    novo_post = {
    "title": "Novo Post",
    "body": "Conteudo do post",
    "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=novo_post)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == novo_post["title"]
    print(f"Post criado com ID: {data["id"]}")
def test_read():
    """Teste READ - buscar post existente"""
    response = requests.get(f"{BASE_URL}/posts/1")  
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data

    print(f"Post encontrado - Titulo: {data["title"]}")
def test_read_inexistente():
    """Teste READ - buscar post que nao existe"""
    response = requests.get(f"{BASE_URL}/posts/999999") 
    assert response.status_code == 404
    print("Status 404 correto para post inexistente")
def test_update():
    """Teste UPDATE - atualizar post existente"""
    dados_atualizados = {
    "title": "Titulo Modificado"
    }

    response = requests.patch(f"{BASE_URL}/posts/1",
    json=dados_atualizados)

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == dados_atualizados["title"]

    print(f"Post atualizado - Novo titulo: {data["title"]}")
def test_delete():
    """Teste DELETE - deletar post"""
    response = requests.delete(f"{BASE_URL}/posts/1")   
    assert response.status_code == 200
    print("Post deletado com sucesso (status 200)")
def test_listar_posts():
    """Teste adicional - listar todos os posts"""
    response = requests.get(f"{BASE_URL}/posts")    
    assert response.status_code == 200
    posts = response.json()
    assert len(posts) > 0

    print(f"Total de posts: {len(posts)}")
    print(f"Primeiro post: {posts[0]["title"]}")
