# Create your Phrase class logic here.
class Phrase:
  
    def display(active_phrase, guesses):
      # this prints out the phrase to the console with guessed letters visibile and unguessed letters as underscores.
      new_phrase = "" 
      
      for letter in active_phrase:
        if letter.isalpha():
          if letter in guesses:
            new_phrase = new_phrase + letter
          else:
            new_phrase = new_phrase + letter.replace(letter, "_")
        else:
          new_phrase = new_phrase + " "
              
      return new_phrase
        
        
    def check_letter(active_phrase, guess):
      # checks to see if the letter selected by the user matches a letter in the phrase.
      response = active_phrase.count(guess) > 0
        
      return response  
    
  
    def check_complete(active_phrase, new_phrase):
        # checks to see if the whole phrase has been guessed.
        complete = active_phrase.upper() == new_phrase.upper()
          
        return complete
