# GDPR Mask and Password Manager

This repo contains the following functionality:  
1. A GDPR mask that can obscure personal data, it simulates masking personally identifiable data which cannot be exposed to certain users under GDPR regulation. The implementation here is as a decorator, which takes input to allow the user to specify which fields they want masked.
1. A database with user information, and a function to create new users with a username and password, and add information about themselves. The information is stored locally in a mock database as JSON.
1. Password storage, and hashing functionality which can check password hashes against each other to confirm correct passwords. Uses python's built-in hash method, and uses hashes created at runtime to compare, such that each hash is unique to any user, and a new hash will be generated each time the application is terminated and restarted.
1. A script that combines the previous functionality. It contains logic to find existing users, check that the password is correct by comparing a hash, and only then: display user information, while simulating a GDPR mask by masking fields based on user input.  

Example of masking:  
```python
{
        'name': '**** *****',
        'email': '*****************',
        'telephones': {
            'mobile': '***** ******'
        },
        'status': 'excellent'
}
```  

Example of logging in using user input:
```
Username:  myUsername
Password:  wrongPassword123
Incorrect Password. Try again..
Password:  
```  

## Tools used in this repo:
1. Comparing data from a database, and checking passwords
1. Python input() method: Working with user-input and testing input functionality
1. Python hash() method: hashing passwords and comparing hashed data
1. Decorators, and Recursion
1. Test-Driven-Development
1. Mocking, Patching
1. JSON Files, reading, writing, and manipulating JSON data

## File structure:
1. The src folder contains the following functions:  
- create_new_user: Creates a user, using python input method, asks for a new username, password, and other information. Writes this information to the new_users_database, and provides feedback on each step via printing to the terminal.  
- gdpr_mask: A function to mask any field in a python dictionary, uses recursion to find any field at any level of nesting. It replaces characters with '*', and ignores spaces.  
- sign_in: A script to fetch data from the database, compare passwords, and create new users if they don't exist.  
1. The test folder contains tests for the create_new_user and gdpr_mask functions, using pytest. Functions were built using test-driven-development.  
1. Mock databases: one for existing data, and one for any data the user creates when running the sign-in script.

## Requirements:
- Python 3.11
- Pytest

## Setup:
After downloading the repo, and installing the correct python version, run the following commands.  
Make sure all commands are run with the working directory at the root of the repo.  
To check: run 'pwd', the path that is shown should end with the name of the repo.  
Input any commands between ' ' into the terminal, omitting the quotation marks:
- Create a virtual environment using 'python -m venv venv'. A folder should be created in the root.
- Activate the environment using 'source venv/bin/activate'.
- Install pytest 'pip install pytest'.
- Setup PYTOHONPATH using 'export PYTHONPATH=$(pwd)'.
- Run Pytest to check all functions were setup correctly: 'pytest'.
- Run the sign_in script: 'python src/sign_in'.

## Script Usage
- You can test getting data by using existing usernames and passwords by checking mock_users_database.json and inputting usernames and passwords from there (case sensitive).
- The user will have 3 attempts to input a correct password.
- When retieving data, fields can be specified to be masked, by typing the fields with a space between each required field. for example: 'username password name'
- Inputting an incorrect username will prompt the user to create a new user with that username.
- The user can then input a new password and about_me information. After this, a new user will be added to the mock_new_users_database.json file.
- Retrieving and inputting data are separated currently, but users can be added to mock_users_database manually and retrieved using the script.

