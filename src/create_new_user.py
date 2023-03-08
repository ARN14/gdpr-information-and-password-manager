import json


def create_new_user(username):
    password = input("Create a new password:  ")
    about_me = input("About me:  ")

    with open("mock_new_users_database.json", "r") as file:
        current_users = json.loads(file.read())
        new_user = {
            "username": username,
            "passsword": password,
            "about_me": about_me
        }

        print(f"User is being created... {new_user}")

        current_users.append(new_user)

        with open("mock_new_users_database.json", "w") as file:
            json.dump(current_users, file, indent=2)

        print("User created successfully")
