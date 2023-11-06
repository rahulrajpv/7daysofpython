
#define class
class BankAccount:
   #instance is created
   def __init__(self, account_number, account_holder_name,account_balance):
      self.account_number =account_number
      self.account_holder_name = account_holder_name
      self.account_balance = account_balance
   #deposit definition   
   def deposit(self,amount):
      self.account_balance += amount
      return self.account_balance
  #withdraw definition 
   def withdraw(self,amount):
       
      if amount > self.account_balance:
         print("Insufficient funds")
         
      else:
         self.account_balance -= amount
         return self.account_balance
   #self definition   
   def display(self):
      print("Account Number: ",self.account_number)
      print("Account Holder Name: ",self.account_holder_name)
      print("Account Balance: ",self.account_balance)

#trying
account1 = BankAccount("123456789","John","1000")

account1.display()

acc = BankAccount("123456789", "Jane Doe", 1000)

# Deposit money
acc.deposit(500)

# withdraw money
acc.withdraw(200)

# Display the account details
acc.display()
