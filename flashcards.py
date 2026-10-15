#What it does: Asks the user quiz questions from a file or list, keeps track of score, and uses a set to
# store unique incorrect questions so the user can re-test themselves.   Concepts practiced: Functions with
# default parameters, set operations (unique tracking), conditional logic (if/elif/else), and error handling 
# for user inputs (TypeError / ValueError). 
import json
import random

with open("flashcards.json") as f:
    cards = json.load(f)
points = 0
while True:

    card = cards[random.randint(0,95)]
    print(f'TOPIC: {card["topic"]}')
    print(card["question"])
    answer = input("> ").lower().strip()
    #Keep track of score, set for incorrect questions so user can re-test themselves
    score = 0
    incorrect = {}
    for group in card["keywords"]:
        for word in group:
            if word in answer:
                score += 1
                break
    if score > 0:
        points += 1
    print(score, "of", len(card["keywords"]), "ideas found")
    print("Answer:", card["answer"])
    print(f"{points} correct so far")


#UPDATE SO THAT IT COUNTS WEAK TOPIC BY ADDING ELIF 

