from random import randint

def pick_six():
    ticket = []
    for i in range(6):
        ticket.append(randint(1, 99))
    return ticket
  
def compare_matches(winner, ticket):
    matches = 0
    for i in range(len(ticket)):
        if ticket[i] == winner[i]:
            matches += 1
    return matches

def calculate_payout(matches):
    if matches == 0:
        return 0
    elif matches == 1:
        return 4
    elif matches == 2:
        return 7
    elif matches == 3:
        return 5E4
    elif matches == 4:
        return 1E6
    elif matches == 5:
        return 25E7

def main():
    MAX_ITER = int(1E5)
    balance = 0
    expenses = 0
    winner = pick_six()

    for i in range(MAX_ITER):
        expenses += 2
        matches = compare_matches(winner, pick_six())
        balance += calculate_payout(matches)

    print(f'\n Balance: {balance}\n Expenses: {expenses} \n ROI: {(balance - expenses) / expenses}\n')

main()