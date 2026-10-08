# ===========================================
# OOP Encapsulation Examples
# ===========================================


# 1. Bank Account — Basic Encapsulation
# Create a BankAccount class where the balance is private.
# Allow the user to deposit money and check the balance,
# but don't allow direct modification of the balance.
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    def get_balance(self):
        return self.__balance


# 2. Student Marks — Validation
# Create a Student class with private marks.
# Create a method to set marks, but accept only values between 0 and 100.
class Student:
    def __init__(self):
        self.__mark = 0

    def set_mark(self, mark):
        if 0 <= mark <= 100:
            self.__mark = mark
        else:
            print("Marks must be between 0 and 100")

    def get_marks(self):
        return self.__mark


# 3. Employee Salary — Getter and Setter
# Create an Employee class with private salary.
# The salary should not be negative.
# Create methods to set and get the salary.
class Employee:
    def __init__(self, salary=0):
        self.__salary = salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative")

    def get_salary(self):
        return self.__salary


# 4. ATM — Real-World Encapsulation
# Create an ATM class with a private balance. Implement:
#   deposit()
#   withdraw()
#   get_balance()
# Withdrawal should be allowed only when sufficient balance is available.
class ATM:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


# ===========================================
# Test Run
# ===========================================
if __name__ == "__main__":
    print("--- Bank Account ---")
    account = BankAccount(1000)
    account.deposit(500)
    print("Balance:", account.get_balance())

    print("\n--- Student Marks ---")
    s = Student()
    s.set_mark(85)
    print("Marks:", s.get_marks())
    s.set_mark(150)  # invalid

    print("\n--- Employee Salary ---")
    emp = Employee(20000)
    emp.set_salary(25000)
    print("Salary:", emp.get_salary())
    emp.set_salary(-5000)  # invalid

    print("\n--- ATM ---")
    atm = ATM(5000)
    atm.deposit(2000)
    atm.withdraw(3000)
    print("Balance:", atm.get_balance())
    atm.withdraw(10000)  # insufficient
    atm.withdraw(-500)   # invalid
