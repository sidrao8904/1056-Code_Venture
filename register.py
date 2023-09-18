import time

def register_user(username):
    # Get the current timestamp
    current_time = str(input("Enter time (HH:MM:SS):"))

    # Create or open a registration file (append mode)
    with open('registration.txt', 'a') as file:
        # Write the registration information (username and timestamp) to the file
        file.write(f'Username: {username}, Registered at: {current_time}\n')

def main():
    print("Welcome to the registration system.")
    username = input("Enter your username: ")

    # Register the user
    register_user(username)

    print("Registration completed!")

if __name__ == "__main__":
    main()
