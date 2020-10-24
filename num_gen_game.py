import random

number = random.randint(1,25)
print("number is between 1 and 25")
x = 0
while True:
    
    score = 100
    print("what is your guess: ")
    guess = int(input())
    if guess > number:
        print("you are too high, guess lower")
        x = x + 1
    elif guess < number:
        print("you are too low, guess higher")
        x = x + 1
    else:
        print("you got it! Nice Job!")
        
        score = 100 - 5*x
        print(score)
        break
    
    
    
    
    
    
