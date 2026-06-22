from src.app import activities


def test_get_activities_returns_expected_shape(client):
    # Arrange
    expected_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert len(payload) == len(activities)

    for details in payload.values():
        assert expected_keys.issubset(details.keys())
        assert isinstance(details["participants"], list)
