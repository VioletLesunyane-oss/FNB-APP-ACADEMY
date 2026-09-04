# THE HIGH-SCORE TRACKER GAME

while True:

    score = input("Enter your game score next to the flashing cursor: ")

    if score.strip().lower() == "stop":
        print("Game session ended!")
        break

    score = int(score)

    if score > 100:
        print("Wow! That's a new high score!")
    else:
        print("Good try, keep playing!")