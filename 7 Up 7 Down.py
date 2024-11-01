import time
from random import randint

print("Hey, Buddy!")
time.sleep(2)
print("🎲 Welcome to the 7 Up 7 Down Game! 🎲")
time.sleep(2)
print("------------------------------------------------")
time.sleep(3)
print("Get ready to test your luck and intuition!")
time.sleep(3)
print("Here's how it works:")
print("------------------------------------------------")
time.sleep(3)
print("1️⃣ You’ll roll a pair of dice.")
time.sleep(3)
print("2️⃣ Guess whether the sum will be above 7 (7 Up), below 7 (7 Down), or exactly 7!")
time.sleep(3)
print("3️⃣ Win if your guess is right!")
time.sleep(2)
print("------------------------------------------------")
time.sleep(3)
print("Are you feeling lucky? Let’s get started! 🎉")
time.sleep(3)
play = input("Do you want to play the game, 7Up 7Down!! (Y/N): ").lower()
time.sleep(3)

money = int(input("How much money would you like to bring to the table to start your adventure? "))
time.sleep(3)

if money < 1:
    print("Looks like you're out of cash! Time to head to the ATM.")
    money = int(input("Enter the amount you want to withdraw from your ATM: "))

while play == 'y':
    number = randint(2, 12)  # Dice sum should be between 2 and 12
    bet = int(input(f"Place your bet! How many rupees do you want to wager? You currently have {money} rupees: "))

    if bet > money:
        print(f"Oops! You don’t have enough money for that bet. You need {bet - money} more rupees.")
        break

    if bet == 0:
        print("A minimum bet of 1 rupee is required. Please place a bet of at least 1 rupee.")
        bet = int(input(f"How much do you want to bet? You have {money} rupees: "))

    # Check if the user ran out of money
    if money < 1:
        print("You ain't got no money, try looting a bank!💰.")
        money = int(input("How much money do you wanna withdraw? "))

    print("\nChoose your guess:")
    time.sleep(2)
    print("1. High Roller (above 7)")
    time.sleep(2)
    print("2. Low Blow (below 7)")
    time.sleep(2)
    print("3. Lucky 7 (exactly 7)")
    time.sleep(2)
    guess = input("Enter your choice (1 for High Roller, 2 for Low Blow, 3 for Lucky 7): ")

    time.sleep(1)
    print(".....")
    time.sleep(3)
    print("The dice are rolling...")
    time.sleep(1)
    print(".....")
    time.sleep(3)

    if guess == '1':
        if number > 7:
            print(f"Holly Molly!,You guessed correctly! The number was {number}.")
            money += bet
        else:
            print(f"Ooh Sad,You guessed wrong! The number was {number}.")
            money -= bet

    elif guess == '2':
        if number < 7:
            print(f"Holly Cow!,You guessed correctly! The number was {number}.")
            money += bet
        else:
            print(f"Oh Noo😢,You guessed wrong! The number was {number}.")
            money -= bet

    elif guess == '3':
        if number == 7:
            print(f"Yeeh!!You guessed correctly! The number was {number}. You win double your bet!")
            money += bet * 2
        else:
            print(f"Damn sorry,You guessed wrong! The number was {number}. You lose double your bet!")
            money -= bet * 2
    else:
        print("Invalid choice! Please choose 1, 2, or 3.")

    print(f"\nCurrent balance: {money} rupees.")

    # Ask if the player wants to continue or withdraw
    play = input("Do you want to continue playing (Y) or withdraw and exit (W)?: ").lower()

    if play == 'w':
        if money > 0:
            print(f"\nYou chose to withdraw! You are leaving with {money} rupees.")
        else:
            print("\nYou don't have any money left to withdraw.")
        print("Thank you for playing 7 Up 7 Down! Best of luck and see you next time! 🎉")
        break
