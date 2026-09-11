from app.app import app


def test_index_returns_support_desk_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Support Desk" in response.data