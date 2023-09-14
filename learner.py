'''
The definition for the Learner class is below.
'''
# Import statements
from user import User

# Learner class definition
class Learner():
    """
    Definition for the Learner class.

    This class accepts the following arguments:

    - User: a User object
    - display_name: a string, which will be pulle from the User object
    - age: an integer, which will be pulled from the User object
    - progressLevel: and integer whose initial value will be 0 and whose setting i have to figure out.
    """

    def __init__(self, 
                 User, 
                 age,
                 progressLevel):
        self.User = User
        self.display_name = User.getUsername()
        self.age = age
        self.progressLevel = progressLevel

    def addAge(self, age):
        self.age = age

    def addProgressLevel(self):
        self.progressLevel += 1

    def getAge(self):
        return self.age


if __name__ == "__main__":
    # Test cases
    # Create a User object
    user1 = User("Jane", "Doe", "something@gmail.com", "password", "jdoe", "student", 1)

    print( user1.getUsername())

    check = user1.__str__()
    # Create a Learner object
    learner1 = Learner(user1, 25, 0)


