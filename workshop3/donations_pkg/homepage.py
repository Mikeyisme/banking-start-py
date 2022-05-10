def show_homepage():
    print("")
    print("          === Donateme Homepage ===          ")
    print("User: ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations |")
    print("               5. Exit                    ")
    print("------------------------------------------")

def donate(username):
    donation_amt = input("Enter amount to donate: ")
    donation_string = print("You donated $", donation_amt)
    print("Thank you for the donation")
    return donation_string
def show_donations(donations):
    print("\n--- All Donations ---")
    if len(donations) == 0:
        print("Currently there are no donations.")
    else:
        total = 0
        for donation_string in donations:
            print(donation_string)
            idx = donation_string.find('$') + 1
            total += float(donation_string[idx:])
        print("Total = $" + str(total))