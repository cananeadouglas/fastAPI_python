from fastapi.testclient import TestClient
from tests.utils.items import create_item_valido

def test_cria_item(client: TestClient) -> None:
    body = create_item_valido()
    response = client.post("/items/", json=body)
    content = response.json()
    assert response.status_code == 200
    assert content["nome"] == body["nome"]

