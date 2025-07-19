import random
from math import*
# Configure the Roulette Wheel
list = [i for i in range (0,37)]
# Manage the Player's Budget

Budget_Initial=int(input("Your budget: "))
print("Your budget is: ",Budget_Initial )
print("Your goal is to maximize your winnings before deciding to stop!!!!")

while Budget_Initial>0:
    # Accept Bets
    num = int(input("Choose a number between 0 and 36 you wish to bet on: "))
    while num not in list:
        print("The number must be between 0 and 36.")
        num = int(input("Choose a number between 0 and 36 you wish to bet on: "))

    argent = int(input("How much money do you want to bet on this number? "))
    # Check the condition
    if argent <= Budget_Initial:
        print("The budget is sufficient!")
    else:
        argent = int(input("Again, how much money do you want to bet on this number? It must be less than or equal to your budget."))

    # Spin the Roulette Wheel
    numé = random.choice(list)  # random.choice(list)
    print("The drawn number is: ", numé)
    # Win and Loss Logic
    if numé == num:
        Budget_Initial = argent * 35
        print("A win!! Your new budget is: ", Budget_Initial)
    else:
        Budget_Initial = Budget_Initial - argent
        print("You lose!! Your new budget is: ", Budget_Initial)
    # End the game
    reponse=input("Do you want to continue playing? Enter yes or no: ")
    if reponse =='oui':
        continue
    if reponse=='non':
        print(f"Thank you for playing! Your final budget is {Budget_Initial}. See you soon!")
        break
else:
    print("You no longer have money to continue.")
print("Nice game. See you soon!")
