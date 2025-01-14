# Slot Machine Game

## Description
This project is a Python-based slot machine. Players can deposit money, place bets on specific lines, and spin the slot machine to win rewards. The game incorporates a user-friendly interface, randomization, and checks for winnings based on symbols displayed on the slot machine.

## Features
- Deposit an amount to start playing.
- Bet on up to 3 lines in the slot machine.
- Symbols with varying values and counts add variety to gameplay.
- Check for winnings and update the balance after each spin.
- Exit the game anytime, with your remaining balance displayed.

## Gameplay Mechanics
1. **Deposit Funds**: The player starts by depositing money.
2. **Choose Lines**: Bet on 1 to 3 lines.
3. **Place Bets**: Decide the amount to bet on each line.
4. **Spin the Slot Machine**: Random symbols appear, and winnings are calculated based on matching symbols across the chosen lines.
5. **Adjust Balance**: Winnings are added to or subtracted from the player's balance.
6. **Repeat or Exit**: Continue playing or quit the game to see the remaining balance.

## Code Structure
### Constants
- `MAX_LINES`: Maximum number of lines to bet on.
- `MAX_BET` and `MIN_BET`: Constraints for the betting amount.
- `ROWS` and `COLS`: Dimensions of the slot machine grid.
- `symbol_count`: Number of occurrences for each symbol.
- `symbol_value`: Winnings multiplier for each symbol.

### Functions
1. **`check_winnings(columns, lines, bet, values)`**: Calculates winnings based on matching symbols.
2. **`get_slot_machine_spin(rows, cols, symbols)`**: Generates a randomized slot machine spin.
3. **`print_slot_machine(columns)`**: Displays the slot machine grid.
4. **`deposit()`**: Handles depositing money.
5. **`number_lines()`**: Prompts the player to choose the number of lines to bet on.
6. **`bet_amout()`**: Prompts the player to input a valid bet amount.
7. **`spin(balance)`**: Executes a single spin and updates the balance.
8. **`main()`**: Main game loop managing the player's balance and gameplay flow.

## Requirements
- Python 3.x
- No external libraries are required.

## How to Run
1. Clone this repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd number-guessing-game
   ```
3. Run the game:
   ```bash
   python3 game.py
   ```

## Example Gameplay
```plaintext
Enter the amount you want to add to your balance: $100
Enter the number of lines you want to bet on (1-3): 2
Enter the amount you want to bet (1-100): $10
You have bet $10 on 2 number of lines, your total bet is $20.

A | B | C
A | A | A
B | D | D

You won $50!
You won on lines: 2
Your current balance is: $130
Press a key to start spinning or (q) to quit: q
Game over!
You left with $130.
```

## Contributing
Contributions are welcome! If you find a bug or have suggestions for improvements, please open an issue or create a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
