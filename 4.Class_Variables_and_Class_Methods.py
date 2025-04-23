class Bank:
    # Class variable shared by all instances
    bank_name = "Old Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    def show_details(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name


# Creating objects
user1 = Bank("Ali")
user2 = Bank("Ayesha")

# Showing details before bank name change
print("Before changing bank name:")
user1.show_details()
user2.show_details()

# Changing the bank name using class method
Bank.change_bank_name("New Future Bank")

# Showing details after bank name change
print("\nAfter changing bank name:")
user1.show_details()
user2.show_details()
