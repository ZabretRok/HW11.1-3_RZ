import datetime
import json
import random


player = input("Hi, what is your name? ")


secret = random.randint(1, 30)
attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

top_3 = sorted(score_list, key=lambda x: x['attempts'])[:3]

for score_dict in top_3:
    print("Player: " + score_dict.get("player_name") + ", attempts: " + str(score_dict.get("attempts")) + ", date: " + score_dict.get("date") + ", number was " + str(score_dict.get("secret_number"))
          + ". These were the wrong guesses: " + str(score_dict.get("wrong_guesses")))

wrong_guesses = []

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"player_name": player, "attempts": attempts, "date": str(datetime.datetime.now()), "secret_number": secret, "wrong_guesses": wrong_guesses})


        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    wrong_guesses.append(guess)