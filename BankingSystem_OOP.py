
#---------------  structure - OOP -----------------

class UserInputValidation:

    def __init__(self, user, mail, passwd):
 
    def username_validation(self, user):
    def email_validation(self, mail):
    def password_validation(self, passwd):

class PasswdEncryption(UserInputValidation):
    def __init__(self, passwd, user, mail):

    def make_salt(self):
    def make_pass_hash(self, pass_hash):

class DbLogin(PasswdEncryption):
    def __init__(self, username, email, password):

    def login(self, username, email, password):
    def write_to_db(self, json_file):

class Banker:
    def __init__(self, init_balance, amount_int, min_balance):

    def banking(self, init_balance, min_balance=100):
    def withdraw(self, init_balance, amount_int, min_balance):
    def deposit(self, init_balance, amount_int):                                    

# ------------ main - user input, login to account, banking below --------------------

class BankingSystem:

    def main(self):
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

            # 1. instance of the class
            userinputvalidation = UserInputValidation(username, email, password)

            # pass validation
            if not userinputvalidation.password_validation(password):
                print(f"\n Wrong password [ex. Username123]")
                continue
            else:

                # 2. instance of the class and fn call
                passwdencryption = PasswdEncryption(username, email, password)
                passwdencryption.make_pass_hash(password)

            # username and mail validation
            if not userinputvalidation.username_validation(username) \
                    and not userinputvalidation.email_validation(email):
                print("\n Wrong username [ex. username]\n" " or email [ex. username@abv.bg]")
                continue

            # 3. instance of the class and fn call
            dblogin = DbLogin(username, email, password)
            dblogin.login(username, email, password)

            if dblogin.login(username, email, password) == True:
                dblogin.write_to_db(json_file="db_user_entry_json.json")

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

                # 4. instance of the class and fn call
                banker = Banker(user_input, user_choice_2, min_balance=100)
                banker.banking(user_input)