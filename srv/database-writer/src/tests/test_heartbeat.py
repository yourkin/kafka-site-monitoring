def test_ping(test_app_without_db):
    # Given
    # test_app

    # When
    response = test_app_without_db.get("/heartbeat")

    # Then
    assert response.status_code == 200
    assert response.json() == {"heartbeat": "OK"}
