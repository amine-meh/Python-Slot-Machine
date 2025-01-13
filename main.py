MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
  while True:
    amount = input("Enter the amount you want to add to your balance: $")
    if amount.isdigit():
      amount = int(amount)
      if amount <= 0 :
        print("The amount should be greater than 0!")
      else :
        break
    else :
      print("Please enter a valid number!")
  return amount

def number_lines():
  while True:
    lines = input(f"Enter the number of lines you want to bet on (1- {MAX_LINES}): ")
    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else :
        print("Enter a valid number of lines!")
        
    else :
      print("Please enter a valid number!")
  return lines

def bet_amout():
  while True:
    amount = input(f"Enter the amount you want to bet ({MIN_BET} - {MAX_BET}): $")
    if amount.isdigit():
      amount = int(amount)
      if MIN_BET <= amount <= MAX_BET :
        break
      else :
        print("Enter a valid amount!")
        
    else :
      print("Please enter a valid number!")
  return amount





def main() :
  balance = deposit()
  lines = number_lines()
  while True:
    bet = bet_amout()
    total_bet = bet * lines
    if balance < total_bet :
      print(f"Your balance is not enough to make this bet. Your balance is ${balance}")
    else :
      print(f"You have bet ${bet} on {lines} number of lines, your total bet is ${total_bet}")
      break




main()