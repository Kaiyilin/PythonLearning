
import json

class User(object):
    def __init__(self, name: str, age: int) -> None:
        super().__init__()
        self.name = name
        self.age = age

user = User("Kai", 50)

# write a custom encoding
# function for json encoding

"""isinstance
'Return whether an object is an instance of a class or of a subclass

e.g.
x = (1, 2)
isinstance(x, tuple) --> True
isinstance(x, object) --> True
isinstance(x, list) --> False
"""

def encode_user(x):
    if isinstance(x, User):
        return {
            "name" : x.name,
            "age" : x.age, 
            x.__class__.__name__: True
        }
    else:
        raise TypeError("object is not json serializable")

user_json = json.dumps(user, default=encode_user) # set the encoder to self defined one
print(user_json)

# another way to built json encoder 
class userEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {
                "name" : o.name,
                "age" : o.age, 
                o.__class__.__name__: True
            }
        return super().default(o)

user_json = json.dumps(user, cls=userEncoder) # set the encoder to self defined one
print(user_json)

# also work
user_json = userEncoder().encode(user)
print(user_json)

# if you want to decode the json the the object
# you need to build a decoder

def decode_user(dct: dict):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct

user = json.loads(user_json, object_hook=decode_user)
print(user) # now it's an user obj
