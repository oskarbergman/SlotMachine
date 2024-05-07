import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "🍎": 2,
    "🍌": 4,
    "🍊": 6,
    "🍇": 8
}

symbol_value = {
    "🍎": 5,
    "🍌": 4,
    "🍊": 3,
    "🍇": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
                
    return winnings, winning_lines

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
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("Hur mycket vill du sätta in? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Beloppet måste vara större än 0.")
        else:
            print("Var vänlig och skriv in beloppet med siffror.")
            
    return amount

def get_number_of_lines():
    while True:
        lines = input("Ange antalet linjer att satsa på (1-" + str(MAX_LINES) +")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Ange ett giltigt antal linjer att satsa på.")
        else:
            print("Var vänlig och skriv in antalet linjer med siffror.")
    
    return lines

            
def get_bet():
    while True:
        amount = input("Hur mycket vill du betta? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <=  amount <= MAX_BET:
                break
            else:
                print(f"Ditt bett måste vara mellan {MIN_BET} - {MAX_BET}.")
        else:
            print("Var vänlig och skriv in ditt bett med siffror.")
            
    return amount
                
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"Du har inte tillräckligt med krediter. Just nu kan du betta {balance} kronor som mest.")
        else: 
            break
        
    print(f"Du bettar {bet} kronor på {lines} linjer. Du bettar totalt {total_bet} kronor.")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"Du vann {winnings} kronor.")
    print("På linje:", " och ".join(map(str, winning_lines)))
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Nuvaranda saldo är {balance} kronor.")
        answer = input("Tryck på enter för att spela (q för att avsluta)")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"Du lämnar spelet med {balance} kronor")    
    

main()
