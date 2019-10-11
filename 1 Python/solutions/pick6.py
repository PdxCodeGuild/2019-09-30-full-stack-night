from random import randint

payouts = [0, 4, 7, 50000, 1000000, 250000000]

def pick_six():
    return [randint(1, 99) for i in range(6)]
  
def compare_matches(winner, ticket):
    matches = 0
    for i in range(len(ticket)):
        if ticket[i] == winner[i]:
            matches += 1
    return matches
        
def main():
    MAX_ITER = 100000
    balance = 0
    expenses = 0
    winner = pick_six()

    for i in range(MAX_ITER):
        expenses += 2
        ticket = pick_six()
        matches = compare_matches(winner, ticket)
        balance += payouts[matches]

    print(f'\n Balance: {balance}\n Expenses: {expenses} \n ROI: {(balance - expenses) / expenses}')

main()
