import os
import time
import random


def user_question():
    """Ask user to enter the question"""
    question = input("Please enter your question: ")
    return question

def thinking_screen(question_str):
    """Thinking process animation"""
    os.system('cls')
    print(question_str + "\n")
    print("|", end=" ", flush=True)
    for x in range(0, 11):
        print(f"{x * 10}%", end=" ", flush=True)
        time.sleep(0.2)
    print("|\n")

def pick_answer(answers_dict):
    """Pick a random answer from the dictionary"""
    answer = random.choice(answers_dict)
    return answer

if __name__ == '__main__':

    answers = {
        0 : "It is certain.",
        1 : "It is decidedly so.",
        2 : "Without a doubt.",
        3 : "Yes — definitely.",
        4 : "You may rely on it.",
        5 : "As I see it, yes.",
        6 : "Most likely.",
        7 : "Outlook good.",
        8 : "Signs point to yes.",
        9 : "Yes.",
        10 : "Reply hazy, try again.",
        11 : "Ask again later.",
        12 : "Better not tell you now.",
        13 : "Cannot predict now.",
        14 : "Concentrate and ask again.",
        15 : "Don’t count on it.",
        16 : "My reply is no.",
        17 : "My sources say no.",
        18 : "Outlook not so good.",
        19 : "Very doubtful."
        }

    os.system('cls')
    question = user_question()
    thinking_screen(question)
    print(pick_answer(answers))


