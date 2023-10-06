#importing time module for time of registration
import time

#list of users and their registration inforation

registration_information=[]

def register_user(username,current_time):
    """
    function that allows users to be registered on the software
    return: None
    """

    #text to append to list of usernames
    registration_information.append(f"User's username: {username} was registered at {current_time}")


def main():
    """
    function that calls upom register_user
    allows the user to register 
    """
    #welcomes user to codeventure
    print("Welcome to CodeVenture")
    username= str(input("Enter your username:"))

    #using strftime function we can get the exact time users register
    present_time= time.strftime("%H:%M:%S")

    #user is now registered into the system
    register_user(username,present_time)

    #confirms registration
    print("Your Registration is now complete\n")
    print("Time to embark on your coding journey!\n")


if __name__ == "__main__":
    main()
