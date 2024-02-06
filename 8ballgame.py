import colorama
from colorama import Fore
colorama.init()
import random


def fortune_teller():
    return input("What is your question? ")

good_fortune = ["Good things are coming your way.",
    "Fortune favors the bold.",
    "You will find happiness in unexpected places.",
    "Success is just around the corner.",
    "Your hard work will pay off soon.",
    "Opportunities are on the horizon.",
    "Believe in yourself and good fortune will follow.",
    "You are destined for greatness.",
    "Positive vibes are heading your way.",
    "The universe has big plans for you.",
    "Your future is bright.",
    "Luck is on your side today.",
    "Embrace change and good fortune will find you.",
    "Your dreams will become reality.",
    "You have the power to create your own luck.",
    "Keep a positive outlook and good things will happen.",
    "Trust in the journey, good things take time.",
    "Stay optimistic and the universe will align in your favor."]

bad_fortune = ["Trouble lies ahead, be cautious.",
    "Challenges will test your resilience.",
    "Beware of deceitful people around you.",
    "Hard times are coming, but you will overcome them.",
    "Expect setbacks, but don't lose hope.",
    "Mistakes may lead to valuable lessons.",
    "Prepare for disappointment, but stay strong.",
    "Obstacles may block your path, but you can find a way around them.",
    "Be wary of unexpected problems in the near future.",
    "Difficulties may arise, but you have the strength to face them.",
    "Negative energy surrounds you, stay grounded.",
    "Misfortune may strike, but it's temporary.",
    "Take precautions to avoid potential pitfalls.",
    "Disappointments are part of life, learn to accept them.",
    "Not everything will go according to plan, adaptability is key.",
    "Stay vigilant, as danger may lurk in unexpected places.",
    "Prepare for the worst, but hope for the best.",
    "Hardships may test your resolve, but they will pass."]

while True:
    user_question = fortune_teller()
    rand_num = random.randint(1,10)

    if rand_num % 2:
        random_index = random.randint(0, len(good_fortune)-1)
        random_good_fortune = good_fortune[random_index]
        print(Fore.GREEN + random_good_fortune)
    else:
        random_index = random.randint(0, len(bad_fortune)-1)
        random_bad_fortune = bad_fortune[random_index]
        print(Fore.RED + random_bad_fortune)
    
    print(Fore.WHITE)
    
    continue_playing = input("Do you want to ask another question? (yes/no): ")
    if continue_playing.lower() != "yes":
        break