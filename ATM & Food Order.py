# ATM Mini project
# total balance
Balance = 2000

# list of material
print("ATM mini project")
print("1.Check balance:")
print("2.Deposit Money:")
print("3.Withdraw Money:")
print("4.Exit:")

# inputs
Choice = int(input("enter your num:  "))

# match choice
match Choice:
  case 1:
    print(f"your balance is : RS {Balance}")

  case 2:
    deposite_money = float(input("enter money:"))
    Balance = Balance + deposite_money
    print(f"deposite completed,New balance is:Rs{Balance}")

  case 3:
    withdraw_money = float(input("enter money:"))

    if withdraw_money > Balance:
      print("Insufficient Balance")
    else:
          Balance = Balance - withdraw_money
      print(f"withdraw completed , new balance is :Rs{Balance}")

  case 4:
    print("thanks")

  case _:
    print("plz enter avalible option")



# Hotel menu 

# food Menu
print("menu_List")
print("1. idly - Rs 30")
print("2. dosa - Rs 50")
print("3. pongal - Rs 60")
print("4. Rost - Rs 55")
print("5. finish_order & bill")

total_bill = 0

# order loop
while True:
  order = int(input("your_order : "))

  match order:
    case 1:
      qty = int(input("total idly: "))
      bill = qty * 30
      total_bill = total_bill + bill
      print(f"added {qty} idly(s) . current_total = {total_bill}")

    case 2:
      qty = int(input("total dosa : "))
      bill = qty * 50
      total_bill = total_bill + bill
      print(f"added {qty} dosa(s) . current_total = {total_bill}")

    case 3:
      qty = int(input("total_pongal: "))
      bill = qty * 60
      total_bill = total_bill + bill
      print(f"added {qty} pongal(s) . current_total = {total_bill}")

    case 4:
      qty = int(input("total_Rost: "))
      bill = qty * 55
      total_bill = total_bill + bill
      print(f"added {qty} Rost(s) . current_total = {total_bill}")

    case 5:
      print("\n ------------------")
      print(f"Final_bill = Rs {total_bill}")
      print("thanks")
      break

    case _:
      print("Invalid choice , plz select avalible order")