from app.app import app


def test_create_ticket_redirects_to_index():
    client = app.test_client()

    response = client.post(
        "/tickets",
        data={
            "author": "Alice",
            "title": "Unable to sign in",
            "content": "The login page returns an error."
        }
    )

    assert response.status_code == 303
    assert response.headers["Location"] == "/"


def test_create_ticket_rejects_missing_fields():
    client = app.test_client()

    response = client.post(
        "/tickets",
        data={
            "author": "Alice",
            "title": "",
            "content": "The login page returns an error."
        }
    )

    assert response.status_code == 400