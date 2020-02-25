# withdrawl
def withdrawl(x):
  while True:  
    y = int(input("How much would you like to withdrawl: "))
    if y <= x:
      return (x - y)
    print ("Not enough money in account, please enter a valid number.")

# deposit
def deposit(x):
  y = int(input("How much would you like to deposit: "))
  return (x + y)

# cancel function
def finish():
  return input("Would you like to do something else, yes(y) or no(n): ")  

# quick exit
def exit_now():
  return input("Are you sure you would like to exit, yes(y) or no(n): ")

# transfer
def transfer(x):
   while True:  
    y = int(input("How much would you like to transfer: "))
    if y <= x:
      return (y)
    print ("Not enough money in account, please enter a valid number.")

# actual system 
def bank_system():

  # account numbers and balances
  acc_num1 = 1234
  acc_num1_bal = 2000

  acc_num2 = 4321
  acc_num2_bal = 2500

  wrong_tries = 0
  
  # enter account number
  while True:
    try:
      account_number = int(input("Welcome to Chase Banking, please enter your account number: "))

      if account_number == acc_num1 or account_number == acc_num2:
        print("Welcome account " + str(account_number) + ".")

        # action options
        while True:
          options = int(input("Would you like to withdrawl(1), deposit(2), review balance(3), transfer money(4), or exit(5): "))
          if account_number == acc_num1:
            while True:
              if options == 1:
                print("Your balance is " + str(acc_num1_bal) +" dollars.")
                acc_num1_bal = withdrawl(acc_num1_bal)
                fin = finish()
                if fin == "n":
                  break
                elif fin == "y":
                  break
                elif fin != "y" and fin != "n":
                  print ("Invalid answer, you have timed out.")
                  break
              elif options == 2:
                print("Your balance is " + str(acc_num1_bal) +" dollars.")
                acc_num1_bal = deposit(acc_num1_bal)
                fin = finish()
                if fin == "n":
                  break
                elif fin == "y":
                  break
                elif fin != "y" and fin != "n":
                  print ("Invalid answer, you have timed out.")
                  break
              elif options == 3:
                print("Your balance is " + str(acc_num1_bal) +" dollars.")
                fin = finish()
                if fin == "n":
                  break
                elif fin == "y":
                  break
                elif fin != "y" and fin != "n":
                  print ("Invalid answer, you have timed out.")
                  break
              elif options == 4:
                print("Your balance is " + str(acc_num1_bal) +" dollars.")
                trans = transfer(acc_num1_bal)
                acc_num1_bal -=  trans
                acc_num2_bal += trans
                fin = finish()
                if fin == "n":
                  break
                elif fin == "y":
                  break
                elif fin != "y" and fin != "n":
                  print ("Invalid answer, you have timed out.")
                  break
              elif options == 5:
                fin = "n"
                break
              elif options != 1 and options != 2 and options != 3 and options != 4 and options != 5:
                options = int(input("Invalid option, please select withdrawl(1), deposit(2), review balance(3), transfer money(4), or exit(5): "))
            
          elif account_number == acc_num2:
            while True:
              if options == 1:
                print("Your balance is " + str(acc_num2_bal) +" dollars.")
                acc_num2_bal = withdrawl(acc_num2_bal)
                fin = finish()
                if fin == "n":
                  break
                elif fin == "y":
                  break
                elif fin != "y" and fin != "n":
                  print ("Invalid answer, you have timed out.")
                  break
              elif options == 2:
                print("Your balance is " + str(acc_num2_bal) +" dollars.")
                acc_num2_bal = deposit(acc_num2_bal)
                fin = finish()
                if fin == "n":
                  break
                elif fin == "y":
                  break
                elif fin != "y" and fin != "n":
                  print ("Invalid answer, you have timed out.")
                  break
              elif options == 3:
                print("Your balance is " + str(acc_num2_bal) +" dollars.")
                fin = finish()
                if fin == "n":
                  break
                elif fin == "y":
                  break
                elif fin != "y" and fin != "n":
                  print ("Invalid answer, you have timed out.")
                  break
              elif options == 4:
                print("Your balance is " + str(acc_num2_bal) +" dollars.")
                trans = transfer(acc_num2_bal)
                acc_num2_bal -=  trans
                acc_num1_bal += trans
                fin = finish()
                if fin == "n":
                  break
                elif fin == "y":
                  break
                elif fin != "y" and fin != "n":
                  print ("Invalid answer, you have timed out.")
                  break
              elif options == 5:
                fin = "n"
                break
              elif options != 1 and options != 2 and options != 3 and options != 4 and options != 5:
                options = int(input("Invalid option, please select withdrawl(1), deposit(2), review balance(3), transfer money(4), or exit(5): "))
          elif account_number == 987654321:
            print("Please stop trying random numbers.")
          # log out
          if fin == "n":
            print("You have been logged out of Chase Banking, have a good day.")
            break
      
      #spam protection
      else:
        print ("That is not a valid banking number, please try again.")
        wrong_tries += 1
    #spam protection part 2
    except ValueError:
      print ("That was not a valid input, and you have been signed out for our safety. Please try again later.")
      wrong_tries += 1
    if wrong_tries > 10:
        print("There have been too many false inputs, we are shutting down to secure our servers. Please try agian later.")
        break
bank_system()