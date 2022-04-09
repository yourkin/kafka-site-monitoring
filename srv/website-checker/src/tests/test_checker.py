def test_checker(test_app):
    # Given
    # test_app

    # When
    response = test_app.post("/website-checker")

    # Then
    assert response.status_code == 200
    assert response.json() == {"heartbeat": "OK"}
