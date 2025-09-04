import time
import json
import random
# loading Texts from json file
with open("texts.json",'r') as f:
    typing_texts = json.load(f)

# Menu
print("\n-----------Welcome to Typing Speed Tester-------------\n Enter 'Q' to Exit")

# selects (easy,medium,hard) and randomly choose one from it. 
def get_text(level):
    if level == '1':
        text = random.choice(typing_texts['easy'])
    elif level == '2':
        text = random.choice(typing_texts['medium'])
    else:
        text = random.choice(typing_texts['hard'])
    
    return text

# Take test input and calculates words per miniute
def wpm_tester(text):
    words = text.split()
    print(f"\n{text}\n")
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
    return test,wpm

# Calculates Accuracy by matching each character.
def accuracy(text,test):
    total = len(text)
    correct = 0
    for i,j in zip(text,test):
        if i == j:
            correct += 1

    accuracy_percentage = (correct/total)*100
    print(f"Accuracy : {accuracy_percentage:2f}")



# Driver
while True:
    print("\nChoose Difficulty Level - \n 1 - Easy\n 2 - Medium\n 3 - Hard")
    level = input("Enter (1,2,3): ")
    if str(level).lower() == 'q':
        quit()
    if int(level) in [1,2,3]:
         text=get_text(level)
         test,wpm = wpm_tester(text)
         accuracy(text,test) 
         

    else :
        print("Invalid Input")
        continue
