#BB 1st Main interperter
#Main program runner for Score Tracker, used as function in other files
#Import libraries
#import files
import snake_game, user_management, score_management, sys, random, csv
USERS_FILE = 'high_scores.csv'

#liamfile.find_user(name, score_type, game)
def main():
    try:
        user = None
        #get user input for player names and scores
        while not user:
            choice = input("Enter 'r' to register, 'l' to login, 'q' to quit or 'v' to view scores").lower()
            if choice == 'r':
                #name = input("Enter player name: ")
                user = user_management.register()
            elif choice == 'l':
                #use find user function to find player names and scores
                user = user_management.login()
            elif choice == 'q':
                sys.exit(0)
            elif choice == 'v':
                #display scores in csv file
                with open(USERS_FILE, 'r', newline='') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        print(", ".join(row))
            else:
                print("Invalid choice. Try again.")
        #Display user information
        print(f"Welcome, {user}!")

        while True:
            #Get user input for game
            try:
                #scores = masonfile.get_scores()
                score = snake_game.play_game()
            except Exception as e:
                #Handle game errors
                print(f"Game failed to run: {e}")
                backup = input("Run backup game? (y/n): ").lower()
                if backup == 'y':
                    sys.exit(0)
                else:
                    score = 0

            #if player dies, save score and display score
            score_management.update_score(user, score)
            scores = score_management.get_scores()
            score_management.display_scores(scores)

            #ask user if they want to play again, if yes, run game, else if no, quit program, else ask again
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
    #Handle unexpected errors
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

#Run the main function
if __name__ == "__main__":
    main()