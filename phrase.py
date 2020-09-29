
# Create your Phrase class logic here.
class Phrase:

    # The class should include an initializer or def __init__ that receives a phrase parameter and holds this phrase in an instance attribute on the Phrase object.
    def __init__(self, phrase):
        # phrase: this is the actual phrase the Phrase object is representing. This attribute should be set to the phrase parameter but converted to all lower case.
        self.my_phrase = phrase

        
    def __str__(self):
        return self.my_phrase

        
    def display(self, guesses):
      # this prints out the phrase to the console with guessed letters visibile and unguessed letters as underscores.
      new_phrase = ""
      my_phrase = str(self.my_phrase)
      for letter in my_phrase:
        if letter.isalpha():
          if letter in guesses:
            new_phrase = new_phrase + letter
          else:
            new_phrase = new_phrase + letter.replace(letter, "_")
        else:
          new_phrase = new_phrase + " "
              
      return new_phrase
        
        
    def check_letter(self, guess):
      # checks to see if the letter selected by the user matches a letter in the phrase.
      my_phrase = str(self.my_phrase)
      response = my_phrase.count(guess) > 0
        
      return response  
    
  
    def check_complete(self, new_phrase):
        # checks to see if the whole phrase has been guessed.
        my_phrase = str(self.my_phrase)
        complete = my_phrase.upper() == new_phrase.upper()
          
        return complete
