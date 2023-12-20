import json
import os

DATA = None

class User:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        

class LoadData:
    def load_data():
        global DATA
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_folder_path = os.path.join(current_dir,'..','data')
        credential_file_path = os.path.join(data_folder_path,'credential.json')

        with open(credential_file_path, 'r') as file:
            data = json.load(file)

        DATA =  data


class UserAuthentication:
    def login_user(userName, password):
        print(userName, "Trying to login")
        if userName in DATA['UserName'] and password in DATA["Password"]:
            print('login success')
            return True
        else:
            print("Login Failed")
            return False


def auth_user(userName, password):
    LoadData.load_data()
    if UserAuthentication.login_user(userName, password):
        print("Move to Home page")

if __name__ == '__main__':
    LoadData.load_data()
    UserAuthentication.login_user('admin','admin')