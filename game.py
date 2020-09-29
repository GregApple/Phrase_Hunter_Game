import random

from phrase import Phrase

# Create your Game class logic in here.
class Game:
  
    def __init__(self):
      # used to track the number of incorrect guesses by the user. The initial value is 0 since no guesses have been made at the start of the game.
      self.missed  = 0
      # a list of five Phrase objects to use with the game. A phrase should only include letters and spaces -- no numbers, puntuation or other special characters.
      self.phrases = [Phrase('cut to the chase'), Phrase('the final countdown'), Phrase('right on the nose'), Phrase('possibly the worst'), Phrase('could be better')]
      # This is the Phrase object that's currently in play. The initial value will be None. Within the start_game() method, this property will be set to the Phrase object returned from a call to the get_random_phrase() method
      self.phrase = None
      # This is a list that contains the letters guessed by the user.
      self.guesses = []
      
      
    def start(self):
      # Calls the welcome method, creates the game loop, calls the get_guess method, adds the user's guess to guesses, increments the number of missed by one if the guess is incorrect, calls the game_over method.
      self.welcome()
      phrase = self.get_random_phrase()
      guess = ""
      complete = False
      missed = self.missed
      while complete == False and missed <5:
        new_phrase = Phrase(phrase).display(self.guesses)
        print(new_phrase)
        guess = self.get_guess()
        response = (Phrase(phrase).check_letter(guess))
        self.guesses.append(guess)
        if response == False:
          missed = missed +1
          print("Only {} lives remain.".format(5-missed))
          print(self.guesses)
        else:
          new_phrase = Phrase(phrase).display(self.guesses)
          complete = (Phrase(phrase).check_complete(new_phrase))
          print(self.guesses)
      self.game_over(phrase, missed)
        
        
    def welcome(self):
      # this method prints a friendly welcome message to the user at the start of the game
      print("Welcome to Phrase Hunter.") 


    def get_random_phrase(self):
      # this method randomly retrieves one of the phrases stored in the phrases list and returns it.
      self.phrase = random.choice(self.phrases)
      phrase = self.phrase

      return phrase
    
    def get_guess(self):
      # this method gets the guess from a user and records it in the guesses attribute 
        guess = input("Which letter would you like to guess? \n")
        guess = guess.lower()
        
        return guess

      
    def game_over(self, phrase, missed):
      # this method displays a friendly win or loss message and ends the game.
      if missed == 5:
        print("Game over. The phrase was '{}'. Better luck next time. ".format(phrase))
        start_over = input("Would you like to play again? [Yn]")
        if start_over == 'Y':
            new_game = Game()
            Game.start(new_game)
        else:
            print("Thanks for playing!")
        
      else:
        print("{}".format(phrase))
        print("Congratulations! You win.")
        start_over = input("Would you like to play again? [Yn]")
        if start_over == 'Y':
            new_game = Game()
            Game.start(new_game)
        else:
            print("Thanks for playing!")
