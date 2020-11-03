guess = 1
while True:
    num = input("Please guess the number (betwenn 0-100):")
    try:
        num = int(num)
    except:
        print("Invalid number, please guess again")
        continue
    
    if num < 45:
        print("your guess is under")
    elif num > 45:
        print("your guess is above")
    else:
        break
    
    guess +=1
print(f"You guessed it in {guess} guesses")
