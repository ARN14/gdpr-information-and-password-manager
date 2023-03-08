def create_new_user(username):
    password = input("Create a new password:  ")
    with open("./mock_new_user_database") as file:
        print(file.read())
