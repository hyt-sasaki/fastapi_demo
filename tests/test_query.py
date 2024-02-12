from demo.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_query() -> None:
    query: str = """
        query {
          hello
        }
    """
    response = client.post("/graphql", json={"query": query})
    result = response.json()
    assert response.status_code == 200
    assert result["data"]["hello"] == "Hello World"
