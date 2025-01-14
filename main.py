import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
  'A': 2,
  'B': 3,
  'C': 4,
  'D': 5,
}

symbol_value = {
  'A': 5,
  'B': 4,
  'C': 3,
  'D': 2,
}

def check_winnings(columns, lines, bet, values):
  winnings = 0
  winnings_lines = []
  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbol_to_check = column[line]
      if symbol != symbol_to_check:
        break
    else :
      winnings += values[symbol] * bet
      winnings_lines.append(line+1)
  return winnings, winnings_lines

def get_slot_machine_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)
    
  columns = []

  for _ in range(cols):
    column = []
    current_symbols = all_symbols[:]
    for _ in range(rows):
      value = random.choice(current_symbols)
      current_symbols.remove(value)
      column.append(value)
    
    columns.append(column)

  return columns

def print_slot_machine(columns):
  for row in range(len(columns[0])):
    for i, column in enumerate(columns) :
      if i != len(columns) -1:
        print(column[row], end=" | ")
      else :
        print(column[row], end="")

    print()

  

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


def spin(balance):
  lines = number_lines()
  while True:
    bet = bet_amout()
    total_bet = bet * lines
    if balance < total_bet :
      print(f"Your balance is not enough to make this bet. Your balance is ${balance}")
    else :
      break

  print(f"You have bet ${bet} on {lines} number of lines, your total bet is ${total_bet}")

  slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)

  winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
  print(f"You won ${winnings}!")
  print(f"You won on lines :", *winning_lines)
  return winnings - total_bet





def main() :
  balance = deposit()
  while True :
    print(f"Your current balance is : ${balance}")
    play = input("Press a key to start spining or (q) to quit. ")
    if play == "q" :
      print("Game over!")
      break
    
    balance += spin(balance)
  print(f"You left with ${balance}.")




main()