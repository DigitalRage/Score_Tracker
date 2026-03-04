import csv
import os

SCORES_FILE = 'high_scores.csv'

def update_score(username, new_score):
    scores = get_scores()
    current_score = next((s[1] for s in scores if s[0] == username), 0)
    if new_score > current_score:
        scores = [s for s in scores if s[0] != username] 
        scores.append([username, new_score])
        with open(SCORES_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['username', 'score'])  
            writer.writerows(scores)
        print("High score updated!")
    else:
        print("Score not higher than current high.")

def get_scores():
    if not os.path.exists(SCORES_FILE):
        return []
    with open(SCORES_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)  
        return [[row[0], int(row[1])] for row in reader if len(row) == 2]

def display_scores(scores):
    if not scores:
        print("No high scores yet.")
        return
    scores.sort(key=lambda x: x[1], reverse=True)  
    print("High Scores:")
    for i, (user, score) in enumerate(scores[:5], 1):  
        print(f"{i}. {user}: {score}")