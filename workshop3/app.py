from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register
import sys

database = {"admin": "password123"}
donations = []
authorized_user = ""

while True:
    print()
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as: ", authorized_user)

    option = input("Choose an option: ")

    if option == "1":                       
        username = input("\nEnter username: ") 
        password = input("Enter password: ")
        authorized_user = login(database, username, password)

    elif option ==  "2":                          
        username = input("\nEnter username: ") 
        password = input("Enter password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[authorized_user] = password
        
    elif option ==  "3":                            
        if authorized_user == "":
            print ("You are not logged in")
        else: 
            donation_string = donate(authorized_user)

    elif option ==  "4":                               
        show_donations(donations)
        
    elif option ==  "5":                          
        print("Leaving DonateMe...")
        sys.exit()
    else:
        print("Invalid entry. Please choose another option.")