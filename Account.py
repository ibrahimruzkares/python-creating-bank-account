import random
import time


class Account:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.bank_name = ""
        self.account_number = 0
        self.user_name = ""
        self.temp_password = 0
        self.log_user = ""
        self.log_pass = 0
        self.password = 0
        

    def welcome_msg(self):
        print("""
                    Welcome to account creator page.
              Available banks will be listed within seconds...
              """)
        time.sleep(2)

    def create_new_account(self):
        self.bank_list()
        selection = int(input("\n Which bank would you like to proceed with:\n"))
        match selection:
            case 1:
                self.bank_name = "Isbank"
            case 2:
                self.bank_name = "ING bank"
            case 3:
                self.bank_name = "Akbank"

        self.name = input("Name: ")
        self.surname = input("Surname: ")
        self.account_number = "TR" + "%0.16d" % random.randint(0, 999999999999)
        self.user_name = self.name + self.surname
        self.temp_password = "%0.6d" % random.randint(0, 999999)

    @staticmethod
    def bank_list():
        bank_list = ["Isbank", "ING bank", "Akbank"]
        codes = [1, 2, 3]
        for index, name in zip(codes, bank_list):
            print(f"{index}.{name}")

    def first_log_in(self):
        print("\n You are required to set a new password by using your username and temporary password...")
        time.sleep(2)
        self.log_user = input("Enter your user name: ")
        self.log_pass = input("Enter your temporary password: ")
        if self.log_user == self.user_name and self.log_pass == self.temp_password:
            print("Access granted!")
            self.password = input("Please create your new Password: ")
            self.log_pass = self.password
            print(f"You may now use your new password '{self.password}' to log in.")

    def log_in(self):
        log_in_attempts = 0
        account_blocked = False
        while not log_in_attempts >= 3:
            self.log_user = input("Enter your user name: ")
            self.log_pass = input("Enter your password: ")
            log_in_attempts += 1
            if log_in_attempts >= 3:
                print("Your account has been blocked and will be redirected to security question...")
                time.sleep(1)
                account_blocked = True
                if account_blocked:
                    answer = input("What was the name of your first dog?\n")
                    if answer == "lumi":
                        print("Verification succeeded!")
                        self.password = input("Create your new password: ")
                        log_in_attempts = 0
                    else:
                        print("Your account has been suspended! Contact your customer services.")
                        break
            elif self.log_user == self.user_name and self.log_pass == self.password:
                print(f"Welcome to {self.bank_name} mobile!")
                break
            elif self.log_user != self.user_name and self.log_pass != self.password:
                print("Wrong user ID and password!")
            elif self.log_user != self.user_name:
                print("Wrong user ID!")
            elif self.log_pass != self.password:
                print("Wrong password!")

    def show_account_details(self):
        print("\n Your account details are confidential. Do not share with others!")
        print("****************************************")
        print(f"Name: {self.name}\n"
              f"Surname: {self.surname}\n"
              f"Bank Name: {self.bank_name}\n"
              f"Account Number: {self.account_number}\n"
              f"User name: {self.user_name}\n"
              f"Temporary password: {self.temp_password}\n")
        print("****************************************")


account1 = Account()
account1.welcome_msg()
account1.create_new_account()
account1.show_account_details()
account1.first_log_in()
account1.log_in()
