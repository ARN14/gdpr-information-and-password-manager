from mock_database import data
from gdpr_mask import mask
from create_new_user import create_new_user

attempts = 1


def sign_in():
    username = input("Username:  ")
    for index, user in enumerate(data):
        if username == user['username']:
            password = hash(user['password'])
            result = check_password(password)

            if result:
                info_to_censor = input("What would you like to censor? (space separated for multiple fields)  ")
                print("Retrieving user information...")

                @mask(*info_to_censor.split())
                def get_client_details():
                    return data[index]

                print(get_client_details())
        else:
            new_user = input("A user with that username does not exist, would you like to create a new user with that username? (Yes/No)  ")
            if new_user.lower() == "yes":
                create_new_user(username)
                return
            else:
                print("Please try again.")
                return


def check_password(password_hash):
    global attempts
    password = hash(input("Password:  "))

    if password == password_hash:
        return True

    if attempts >= 3:
        print("Too many attempts, try again later")
        return False

    print("Incorrect Password")
    attempts += 1
    return check_password(password_hash)


sign_in()
