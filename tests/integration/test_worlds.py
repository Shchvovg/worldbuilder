async def test_create_world(client):
    response = await client.post(
            "/worlds/",
            json={"name": "Eidhar", "description": "Magic vanished 200 years ago."},
            )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Eidhar"
    assert "id" in data

async def test_get_world(client):
    create_response = await client.post(
            "/worlds/",
            json={"name": "Eidhar", "description": "Magic vanished 200 years ago."},
            )
    world_id = create_response.json()["id"]

    response = await client.get(f"/worlds/{world_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Eidhar"

async def test_get_world_not_found(client):
    response = await client.get("/worlds/99999")
    assert response.status_code == 404
