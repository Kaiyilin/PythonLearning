"""@property is a built in decorator

@property  in Python which is helpful in defining the properties effortlessly 
without manually calling the inbuilt function property(). 
Which is used to return the property attributes of a class from the stated getter, 
setter and deleter as parameters.

in short, property is used to fulfill the encapsulation in OOP
which makes code modularised

https://www.maxlist.xyz/2019/12/25/python-property/
"""

class Portal1(object):

    def __init__(self) -> None:
        self._name = ""

    # turn the name to the read-only attribute
    @property
    def name(self):
        return self._name
    
    # with setter, you can set the new variable to the name
    @name.setter
    def name(self, val):
        self._name = val
    
    @name.deleter
    def name(self):
        del self._name

p = Portal1()
p.name = "Kai-Yi"

print(p.name)

del p.name

# Real usage, encrypted the pwd befored in stored to database
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

# create the user, and set the pwd to "max"
user_max = User()
user_max.password = "max"

# If the pwd is like previous example, it's really dangerous!
# people can always access to your pwd immediately, in our case

# it'll return AttributeError: password is not readable attribute
print(user_max.password)

# we can only access t the encrypted pwd
print(user_max.password_hash)

# verify_password is used to check whether the input pwd correct or not

print(user_max.verify_password('max'))
print(user_max.verify_password('cat'))