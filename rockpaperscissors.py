import random
import _pydecimal

user_wins = 0

computer_wins = 0

options = ["rock","paper","scissors"]



while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
       
       print ("You won", user_wins, "times.")
       print ("The computer won", computer_wins, "times.")

       print("Well played see ya!")

       break


    if user_input not in options:
       continue          
       
        


    random_number = random.randint(0,2)   
            #  rock: 0, paper:1, scissors: 2
    computer_decision = options[random_number]

    print("Computer picked", computer_decision + ".")
 
    if user_input == "rock" and computer_decision == "scissors":
                print ("You won!")
                user_wins += 1

    elif user_input == "paper" and computer_decision == "rock":
                 print ("You won!")
                 user_wins += 1
                

    elif user_input == "scissors" and computer_decision == "paper":
            print ("You won!")
            user_wins += 1
        
         
    else:



        print("You lost!")
        computer_wins += 1

        print ("You won", user_wins, "times.")
        print ("The computer won", computer_wins, "times.")





