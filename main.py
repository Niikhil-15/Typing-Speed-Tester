import time
text = '''The entire competition is conducted online. All learning materials and resources tailored to your chosen theme will be provided. Teams will complete tasks and submit their work through the competition portal. Interactive online sessions and a dedicated discussion forum will help you resolve queries and connect with mentors throughout the event.'''
words = text.split()
print(text)
check = input("Press 'S' to start : ")
if check.lower() == 's':
    start =time.time()
test = input("Start Typing\n")
end = time.time()
noOfWords = len(words)
timetaken = (end-start)/60
noOfWordsTyped = len(test.split())
wpm = noOfWordsTyped/timetaken
print(f"Typing Speed is : {wpm:.2f}")