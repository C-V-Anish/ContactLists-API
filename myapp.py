import requests
import json

URL = 'http://127.0.0.1:8000/api/auth/register/'

def register_user():
    data={
        'username' : 'AnishCV',
        'first_name' : 'Chivukula',
        'last_name' : 'Venkata' ,
        'password' : 'abcdefgh',
        'email' : 'abcde@gmail.com',
        }
    json_data=json.dumps(data)
    print(json_data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)
    

register_user()

# def login_user():
#     data={
#         'username' : 'AnishCV',
#         'first_name' : 'Chivukula',
#         'last_name' : 'Venkata' ,
#         'password' : 'abcdefgh',
#         'email' : 'abcde@gmail.com',
#         }
#     json_data=json.dumps(data)
#     print(json_data)
#     r=requests.post(url=URL+'login/',data=json_data)
#     data=r.json()
#     print(data)

# login_user()