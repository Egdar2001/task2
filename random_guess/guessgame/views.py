from django.shortcuts import render,redirect
import random
from django.http import HttpRequest

# Create your views here.

random_number = random.randint(1, 10)
tries = 0

def index(request: HttpRequest):
    global tries
    if request.method == "GET":
        tries = 0  # Reset tries when starting a new game
    return render(request, 'guessgame/index.html')

def result(request: HttpRequest):
    global random_number, tries
    feedback = ""
    play_again = False

    if request.method == "POST":
        try:
            guess = int(request.POST.get("guess"))
            tries += 1

            if guess == random_number:
                feedback = f"Congratulations! You guessed the correct number in {tries} tries."
                play_again = True
            else:
                feedback = "Wrong guess! Try again."

        except ValueError:
            feedback = "Please enter a valid number."

    # If game is won, reset the random number for a new game
    if play_again:
        random_number = random.randint(1, 10)
        tries = 0

    return render(request, 'guessgame/result.html', {"feedback": feedback, "play_again": play_again})
