
#from api import app

#@pytest.fixture
#def client():
    #app.config["TESTING"] = True
    #app.config["JWT_SECRET_KEY"] = "test-secret"
    #with app.test_client() as client:
        #yield client

import pytest
from api import app
from flask_jwt_extended import create_access_token

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["WT_SECRET_KEY"] = "test-secret"
    with app.app_context():

        with app.test_client() as client:
            yield client

@pytest.fixture
def user_token():
    return create_access_token(identity="testuser")

@pytest.fixture
def admin_token():
    return create_access_token(identity="admin_user", additional_claims={"role": "admin"})