import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 10000000

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 7,
    "B": 5,
    "C": 2,
    "D": 2
}

def check_wins(columns, lines, bet, values):
    wins = 0
    victory_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            wins += values[symbol] * bet
            victory_lines.append(line + 1)

    return wins, victory_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
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
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end="")

        print()

def deposite():
    while True:
        amount = input("How much would you like to deposite? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print("Thanks for your deposite")
                break
            else:
                print("Come on. Insert some cash")
        else:
            print("Please insert proper money.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the amount of lines to bet on (1-" + str(MAX_LINES) + ") ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid amount of lines.")
        else:
            print("please insert a number.")
    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                print("Thanks for betting")
                break
            else:
                print(f"Amount must be between ${MIN_BET} - {MAX_BET}.")
        else:
            print("Please bet with only money.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"you do not have enough balance. Your total balance is = {balance}.")
        
        else:
            break

    print(f"Your balance is {balance}.You are betting {bet} on each of the {lines} lines. Total bet is equal to {total_bet}")

    slot_machine = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slot_machine)
    wins, victory_lines = check_wins(slot_machine, lines, bet, symbol_value)  
    print(f"You won ${wins} .")
    print(f"The lines you won on are:", * victory_lines)
    return wins - total_bet

def engine():
    balance = deposite()
    while True:
        print(f"Your current balance is ${balance}")
        game = input("press enter to spin(press 'q' to quit)")
        if game == "q":
            break
        balance += spin(balance)

    print(f"You have ${balance} left.")

engine()