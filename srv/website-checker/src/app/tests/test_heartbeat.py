def test_heartbeat(test_app):
    # Given
    # test_app

    # When
    response = test_app.get("/heartbeat")

    # Then
    assert response.status_code == 200
    assert response.json() == {"heartbeat": "OK"}
