import time
import json
import random
with open("texts.json",'r') as f:
    typing_texts = json.load(f)

print("\n-----------Welcome to Typing Speed Tester-------------\n Enter 'Q' to Exit")
def get_text(level):
    if level == 1:
        text = random.choice(typing_texts['easy'])
    elif level == 2:
        text = random.choice(typing_texts['medium'])
    else:
        text = random.choice(typing_texts['hard'])
    
    return text

def tester(text):
    words = text.split()
    print(text)
    check = input("Press 'S' to start : ")
    if check.lower() == 'q':
        quit()
    if check.lower() == 's':
        start =time.time()
    test = input("Start Typing\n")
    end = time.time()
    noOfWords = len(words)
    timetaken = (end-start)/60
    noOfWordsTyped = len(test.split())
    wpm = noOfWordsTyped/timetaken
    print(f"\nTyping Speed is : {wpm:.2f}")





while True:
    print("\nChoose Difficulty Level - \n 1 - Easy\n 2 - Medium\n 3 - Hard")
    level = input("Enter (1,2,3): ")
    if str(level).lower() == 'q':
        quit()
    if int(level) in [1,2,3]:
         text=get_text(level)
         tester(text)
    else :
        print("Invalid Input")
        continue
