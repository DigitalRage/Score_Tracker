#BB 1st Main interperter
#Main program runner for Score Tracker, used as function in other files
#Import libraries
#import files
#Get user input for game
#get user input for player names and scores
#name = input("Enter player name: ")
#scores = masonfile.get_scores()
#use find user function to find player names and scores
#liamfile.find_user(name, score_type, game)

#run game except for if the game doesn't run, then ask user if they want to run backup game, if yes, run backup game, else quit program

#if player dies, save score and display score

#ask user if they want to play again, if yes, run game, else if no, quit program, else ask again

import snake_game
import user_management
import score_management
import sys
import random
import csv
USERS_FILE = 'high_scores.csv'

def main():
    try:
        user = None
        while not user:
            choice = input("Enter 'r' to register, 'l' to login, 'q' to quit or 'v' to view scores").lower()
            if choice == 'r':
                user = user_management.register()
            elif choice == 'l':
                user = user_management.login()
            elif choice == 'q':
                sys.exit(0)
            elif choice == 'v':
                with open(USERS_FILE, 'r', newline='') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        print(", ".join(row))
            else:
                print("Invalid choice. Try again.")

        print(f"Welcome, {user}!")

        while True:
            
            try:
                score = snake_game.play_game()
            except Exception as e:
                print(f"Game failed to run: {e}")
                backup = input("Run backup game? (y/n): ").lower()
                if backup == 'y':
                    sys.exit(0)
                else:
                    score = 0

            
            score_management.update_score(user, score)
            scores = score_management.get_scores()
            score_management.display_scores(scores)

            
            again = input("Play again (y), logout (l), or quit (q)? ").lower()
            if again == 'y':
                continue
            elif again == 'l':
                user_management.logout()
                main()  
            elif again == 'q':
                sys.exit(0)
            else:
                print("Invalid input.")

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()