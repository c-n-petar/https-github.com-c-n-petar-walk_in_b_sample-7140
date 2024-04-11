
#-------------  structure - procedural   --------------------

# username validation
def username_validation(user):

# email validation
def email_validation(mail):

# password validation
def password_validation(passwd):

# make salt to add to the pass hash
def make_salt():

# pass hash and the salt together
def make_pass_hash(pass_hash):

# login into user account
def login(username, email, password):

# write user input to database (json file)
def write_to_db(json_file):

def banking(init_balance, min_balance=100):

# withdrawing
def withdraw(init_balance, amount_int, min_balance):

# depositing
def deposit(init_balance, amount_int):                                

# ------------ main - user input, login to account, banking below --------------------

while True:

    print(f"\n{45 * '-'}\n\t\t Welcome to Walk-In Banking \t\t\n{45 * '-'}\n")

    user_choice_1 = input(
        "- Press {A} to log in your Account\n- Press {Q} to Quit\n- action: "
    )

    if not user_choice_1.lower() in ("a", "q"):
      print("Wrong input.")
      continue

    if user_choice_1 == "q":
        break

    print(f"\n{45 * '-'}\n\t\t\t\t Logging \t\t\t\n{45 * '-'}\n")
    print(f"{14 * '-'} Enter your data {14 * '-'}\n")

    # User input - username, email, password
    print(f"[Lowercase letters, digits, 6-20]")
    username = input("- Username: ")
    print(f"[Lowercase letters, 6-35]")
    email = input("- Email: ")
    print(f"[Letters & digits, begin with Uppercase, 6-20]")
    password = input("- Password: ")

    # pass validation
    if not password_validation(password):
        print(f"\n Wrong password [ex. Username123]")
        continue
    else:
        make_pass_hash(password)

    # username, email validation
    if not username_validation(username) and not email_validation(email):
        print("\n Wrong username [ex. username]\n" " or email [ex. username@abv.bg]")
        continue

    login(username, email, password)

    if login(username, email, password) == True:
        write_to_db(json_file="db_user_entry_json.json")

    user_choice_2 = input(
        "\n- Press {B} to enter Banking\n- Press {R} to Return\n- action: "
    )

    if not user_choice_2.lower() in ("b", "r"):
      print("Wrong input.")
      continue

    if user_choice_2 == "r":
        print(f"\n{14 * '-'} Exiting Logging {14 * '-'}")
        continue

    if user_choice_2 == "b":

        try:
          user_input = int(input("\nEnter Initial Balance amount( > 100.00): "))
        except ValueError:
          print("Wrong input.")
          continue

        if not user_input >= 100:
            print(f"\n{11 * '-'} Wrong initial balance {11 * '-'}")
            continue

        banking(user_input)

