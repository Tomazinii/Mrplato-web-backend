import requests
import pytest

@pytest.fixture
def api_url():
    return "http://localhost:8000"  # URL do endpoint da API

def test_get_problem(api_url):

    url = api_url + "/api/v1/problems/get_problem837513c3-6683-408f-a3c3-fa13b97fc747"
    response = requests.get(url)
    assert response.status_code == 200  # Verifica se a requisição foi bem-sucedida
    user_data = response.json()  # Converte a resposta JSON em um dicionário Python

    # assert user_data["id"] == 1  # Verifica se o ID do usuário retornado é 1
    # assert "name" in user_data  # Verifica se há um campo "name" nos dados do usuário
