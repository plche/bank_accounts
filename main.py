from BankAccount import BankAccount

cuenta1 = BankAccount(1, 200)
cuenta2 = BankAccount(2, 300)

cuenta1.deposit(100).deposit(100).deposit(100).withdrawal(100).generate_interest().show_account_info()

cuenta2.deposit(200).deposit(200).withdrawal(100).withdrawal(100).withdrawal(100).withdrawal(100).generate_interest().show_account_info()

BankAccount.print_all_instances()