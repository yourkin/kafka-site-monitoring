import pytest
from fastapi.testclient import TestClient

from ..app.main import create_application


@pytest.fixture(scope="module")
def test_app_without_db():
    # set up
    app = create_application()
    with TestClient(app) as test_client:

        # testing
        yield test_client

    # tear down
