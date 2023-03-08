from src.create_new_user import create_new_user
from unittest.mock import Mock, patch
import json


def mock_input(*args):
    return "Password"


@patch("src.create_new_user.input", side_effect=mock_input)
def test_adds_username_and_password_from_input(patch):
    with open("mock_new_users_database.json", "w") as file:
        json.dump([], file)

    create_new_user("ABC")

    with open("mock_new_users_database.json", "r") as file:
        read_file = json.loads(file.read())

    assert read_file == [{
    "username": "ABC",
    "passsword": "Password",
    "about_me": "Password"
    }]
