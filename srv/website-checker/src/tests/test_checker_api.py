def test_checker_api(test_app):
    # Given
    # test_app

    # When
    response = test_app.get(
        "/website-checker", json={"url": "https://google.com", "pattern": "sometext"}
    )

    # Then
    assert response.status_code == 200
    json_resp = response.json()
    assert type(json_resp["response_time"]) is float
    assert type(json_resp["status_code"]) is int
    assert type(json_resp["is_pattern_found"]) is int or type(None)
