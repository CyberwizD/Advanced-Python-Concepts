import json
from json import JSONEncoder

person = {
  'name': 'Alice',
  'age': 20,
  'city': 'New York',
  'hasChildren': True,
  'titles': [
    'Engineer',
    'Programmer'
  ],
    'relative': {
        'firstName': 'John',
        'LastName': 'Doe',
        'Hobbies': ['running', 'singing', 'dancing'],
        'age': 28,
        'hasChildren': True,
        'children': [
            {
                'firstName': 'Alex',
                'age': 5
            },
            {
                'firstName': 'Bob',
                'age': 7
            }
        ]
    }
}


# Converting Python Dict to JSON
fp = json.dumps(person, indent=4, sort_keys=True)  # separators=('; ', '= ')

mp = json.dumps(person, indent=4, sort_keys=True)


# Converting JSON to Python Dict
f_person = json.loads(fp)
print(f_person)


# Writing to a json file
with open('data.json', 'w') as json_file:
    json_file.write(f"{fp}")


# Converting JSON File to Python Dict
with open('data.json', 'r') as j_file:
    f_person_file = json.load(j_file)
    print("Loading JSON File...", f_person_file)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_user(obj):
    if isinstance(obj, User):
        return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError('Object of type User in not JSON serializable!')


user = User('John', 'Doe')
userJSON = json.dumps(user, default=encode_user)
print(userJSON)


# Custom JSON encoder
class UserEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
        return JSONEncoder.default(self, obj)


userJS = json.dumps(user, cls=UserEncoder)
userJ = UserEncoder().encode(user)
print(userJS)
print(userJ)


# Custom JSON decoder
def decode_user(dict_):
    if User.__name__ in dict_:
        return User(name=dict_['name'], age=dict_['age'])
    return dict_


userD = json.loads(userJSON, object_hook=decode_user)
print(userD.name, userD.age)
print(userD)
