##### Before 
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


##### After
# always think how can i make this as simple as possible ? readable ? easy to modify ?
class GuessNumber:
    def __init__(self, number, mn=0, mx=100):
        self.number = number
        self.guesses = 0
        self.min = mn
        self.max = mx
        
    def get_guess(self):
        guess = input(f"please guess a number between ({self.min} and {self.max}): ")
        if self.valid_number(guess):
            return int(guess)
        else:
            print("please enter a valid number")
            return self.get_guess()
   
            
    def valid_number(self,str_number):
        try:
            number = int(str_number)
        except:
            return False
        return self.min <= number <= self.max #this allows us to check if the number is between min and max
    
    def play(self):
        while True:
            self.guesses +=1
            guess = self.get_guess()
            if guess < self.number:
                print("your guess was under")
            elif guess > self.number:
                print("your guess was above")
            else: #they guessed it
                break
        print(f"you guessed it in {self.guesses} guesses.")

game = GuessNumber(56,0,100)
game.play()
                
        