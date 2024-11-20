import random, time

class GuessNumber:
  def __init__(self):
    self._number_range = random.randint(1, 101)
    
    self._difficults = {
      1 : [10, "Easy"],
      2 : [5, "Medium"], 
      3 : [3, "Hard"], 
    }
    
    self._menu = {
      1: 1, #Play
      2: 2, #Exit
    }
  def game(self):
    
    print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")
    
    try:
      select_difficult = int(input("Please select the difficulty level:\n 1. Easy (10 chances)\n 2. Medium (5 chances)\n 3. Hard (3 chances) \n"))  
      
      if select_difficult not in self._difficults:
        print('Invalid selection. Please choose a valid difficult level')
        return
        
      chances = self._difficults[select_difficult][0]
      level_name = self._difficults[select_difficult][1]
      print(f'Great! You have selected the {level_name} difficulty level.\n You have {chances} attemps!')
      
      while chances > 0:
        try:
          guess = int(input("Enter your choice: "))
          if guess < 0 or guess > 100:
              print('The number you chose is out of range!')
              continue
          
          if guess == self._number_range:
            print('Congratulations! You guessed the correct number')
            break
          elif guess > self._number_range:
            print(f"The number is less than {guess}")
          elif guess < self._number_range:
            print(f"The number is greater than {guess}")
            
          chances -= 1
          print(f'You have {chances} chances!')
        except ValueError:
          print("Invalid input! Please enter a valid number.")
        
        if chances == 0:
          print(f"Sorry, you've run out of chances. The number was {self._number_range}.\nGAME OVER!")
      
    except ValueError:
      print("Invalid input! Please enter a valid option (1, 2, 3) .")
      
  def game_handler(self):
    
    while True:
      try:
        option = int(input('Welcome to guessing number!\nChoose an option:\n1)Play\n2)Exit\n'))
        
        if option == 1:
          while True:
            self.game()
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
              print('Thanks for playing! Goodbye!')
              time.sleep(1)
              return
        elif option == 2:
          print("Closing the game...")
          time.sleep(1)
          break
        else:
          print('Select a valid option!')
        
      except ValueError:
        print('Invalid input. Please enter 1 or 2.')
    
    
guess_number = GuessNumber()
guess_number.game_handler()
