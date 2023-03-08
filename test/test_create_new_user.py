from src.create_new_user import create_new_user
from unittest.mock import patch

@patch("create_new_user.input", return_value="Password")
def test_adds_username_and_password_from_input(patch):
    create_new_user("ABC")

    assert "new_users" == [{
    "username": "ABC",
    "passsword": "Password"
    }]

