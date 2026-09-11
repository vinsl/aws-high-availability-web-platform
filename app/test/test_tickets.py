from app.app import app


def test_create_ticket_redirects_to_index():
    client = app.test_client()

    response = client.post(
        "/tickets",
        data={
            "author": "Alice",
            "title": "Unable to sign in",
            "content": "The login page returns an error.",
        },
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
            "content": "The login page returns an error.",
        },
    )

    assert response.status_code == 400


def test_created_ticket_is_displayed():
    client = app.test_client()

    response = client.post(
        "/tickets",
        data={
            "author": "Alice",
            "title": "VPN connection issue",
            "content": "The VPN client cannot establish a connection.",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"VPN connection issue" in response.data
    assert b"Alice" in response.data
    assert b"open" in response.data