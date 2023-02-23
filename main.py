import json


if __name__ == "__main__":
    user_dict = '{"username": "user123", "password": "pass123", "name": {"forename": "ben", "surname": "clough"}}'
    user_json = json.loads(user_dict)

    print(type(user_json))
    print(type(user_json['name']))

