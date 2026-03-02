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
import csv
import os

USERS_FILE = 'users.csv'

def register():
    while True:
        username = input("Enter username: ").strip()
        if not username:
            print("Username cannot be empty. Try again.")
            continue

        pin = input("Enter 4-8 digit PIN: ").strip()
        if not (4 <= len(pin) <= 8 and pin.isdigit()):
            print("PIN must be 4-8 digits and numeric only. Try again.")
            continue

        # Check for existing username
        users = load_users()
        if username in users:
            print("Username already exists. Try a different one.")
            continue

        # Save new user
        users[username] = pin
        save_users(users)
        print("Registered successfully.")
        return username

def login():
    while True:
        username = input("Enter username: ").strip()
        if not username:
            print("Username cannot be empty. Try again.")
            continue

        pin = input("Enter 4-8 digit PIN: ").strip()
        if not (4 <= len(pin) <= 8 and pin.isdigit()):
            print("Invalid PIN format. Try again.")
            continue

        users = load_users()
        if username in users and users[username] == pin:
            print("Login successful.")
            return username
        else:
            print("Invalid username or PIN. Try again.")

def logout():
    print("Logged out.")

def load_users():
    users = {}
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 2:
                        users[row[0]] = row[1]
        except Exception as e:
            print(f"Error loading users: {e}")
    return users

def save_users(users):
    try:
        with open(USERS_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            for username, pin in users.items():
                writer.writerow([username, pin])
    except Exception as e:
        print(f"Error saving users: {e}")