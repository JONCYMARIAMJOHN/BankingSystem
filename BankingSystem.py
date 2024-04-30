import maskpass

class Banking :
    def __init__(self, cust_id, cust_name, username, password, account_number, account_balance): 
        self.cust_id = cust_id    
        self.cust_name = cust_name
        self.username = username
        self.password = password
        self.account_number = account_number
        self.account_balance = account_balance

    def account_login(self) :
        global is_login
        if(is_login) :
            print("You are already logged in")
        else :
            try :
                username_input = input("Enter Username : ")
                password_input = maskpass.askpass(mask="*")

                if (username_input == self.username and password_input == self.password) :
                    is_login = True
                    print("Login Successful, Welcome!")
                else :
                    print("Incorrect Username or Password")

            except :
                print("Something went wrong")
        

    def amount_deposit(self) :
        if (is_login) :
            try :
                cust_id_input = input("Enter Customer Id : ")
                if(cust_id_input == self.cust_id) :
                    amount = float(input("Enter amount to deposit : "))
                    self.account_balance += amount
                    print("Rs. {} deposited successfully and your current balance is {}".format(amount, self.account_balance))
                else :
                    print("Incorrect CustomerId")
            except :
                print("Something went wrong")
        else :
            print("Please Login to continue")
            self.account_login()
        
    def amount_withdrawal(self) :
        if(is_login) :
            try :
                cust_id_input = input("Enter Customer Id : ")
                if(cust_id_input == self.cust_id) :
                    amount = float(input("Enter amount to withdraw : "))
                    if(amount > self.account_balance) :
                        print("Insufficient balance")
                    else :
                        self.account_balance -= amount
                        print("Rs. {} withdrew successfully and your current balance is {}".format(amount, self.account_balance))
                else :
                    print("Incorrect CustomerId")
            except :
                print("Something went wrong")
        else :
            print("Please Login to continue")
            self.account_login()
        

    def balance_check(self) :
        if(is_login) :
            try :
                cust_id_input = input("Enter Customer Id : ")
                if(cust_id_input == self.cust_id) :
                    print("Your account balance is Rs. ",self.account_balance)
                else :
                    print("Incorrect CustomerId")
            except :
                print("Something went wrong")
        else :
            print("Please Login to continue")
            self.account_login()

    def view_account_details(self) :
        if(is_login) :
            try :
                cust_id_input = input("Enter Customer Id : ")
                if(cust_id_input == self.cust_id) :
                    print("Your account details :\nCustomer Name : {}\nUsername : {}\nPassword : {}\nAccount Number : {}\nAccount Balance : Rs. {}"
                        .format(self.cust_name, self.username, self.password, self.account_number, self.account_balance))
                else :
                    print("Incorrect CustomerId")
            except :
                print("Something went wrong")
        else :
            print("Please Login to continue")
            self.account_login()

    def logout(self) :
        global is_login
        is_login = False
        print("Logout Successfully, Thank you!")


cust1 = Banking('CUST0001', "Sandeep", "sandeep@gmail.com", "Sandeep@123", "BANK123456789", 100000)
is_login = False

while True :
    try :
        print("\nOptions : \n1. Login \n2. Deposit Amount \n3. Withdraw Amount \n4. Check Balance \n5. View Account Details \n6. Logout \n7. Exit")
        option = int(input("Choose an option : "))
        if(option == 1) :
            cust1.account_login()
        elif(option == 2) :
            cust1.amount_deposit()
        elif(option == 3) :
            cust1.amount_withdrawal()
        elif(option == 4) :
            cust1.balance_check()
        elif(option == 5) :
            cust1.view_account_details()
        elif(option == 6) :
            cust1.logout()
        elif(option == 7) :
            print("Exiting.....")
            break
        else :
            print("Invalid option chose")
    except ValueError :
        print("Please enter an integer as option")
