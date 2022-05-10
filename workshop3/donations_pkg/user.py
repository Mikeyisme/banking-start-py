def login(database, username, password):                        
    if username.lower() in database and database[username.lower()] == password:
            print("\nWelcome back", username+"!")
            return username
    if username.lower() in database and database[username.lower()] != password:
        print("\nIncorrect password for "+username+".")
        return ""
    else:
        username.lower() not in database
        print("\nUser not found. Please register.")
        return ""
def register(database, username, password):
    if username.lower() == database:
        print("Username already registered")
        return ""
    if len(username) > 10:
        print("Please enter a username that is 10 characters or less")
        return ""
    if len(password) <= 5:
        print("password must be more than 5 characters")
        return ""
    else:
        print("Username has been registered")
        return username.lower()