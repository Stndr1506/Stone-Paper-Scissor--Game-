import random

User_action = input("Enter your choice: (stone, paper and scissor): ")
possible_actions = ["stone","paper","scissor"]
computer_action = random.choice(possible_actions)

print(f"\n You chose {User_action},computer chose {computer_action}.\n")

if User_action == computer_action:
    print("Both selected same! It's a tie")
elif(User_action == "scissor"):
    if(computer_action == "stone"):
        print("stone smashes scissor! You lose")
    else:
        print("paper covers stone! you lose")
elif(User_action == "stone"):
    if(computer_action == "scissor"):
        print("stone smashes scissor! You won")
    else:
        print("paper covers stone! You lose")
elif(User_action == "paper"):
    if(computer_action == "stone"):
        print("paper covers stone! You won")
    else:
        print("scissor cuts paper! You lose")


