import snake_game
import user_management
import score_management
import sys
import random

def main():
    try:
        user = None
        while not user:
            choice = input("Enter 'r' to register, 'l' to login, or 'q' to quit: ").lower()
            if choice == 'r':
                user = user_management.register()
            elif choice == 'l':
                user = user_management.login()
            elif choice == 'q':
                sys.exit(0)
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