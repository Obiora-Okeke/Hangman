import random


#use the random module to pick a random word in dictionary text   
word = open("dictionary.txt").readlines()
RandomWord = random.choice(word).lower()
    
#Make the random word a list
RandomWordList = list(RandomWord)
RandomWordList.remove("\n")
 

def main ():

    #create the number of lines needed based off the length of the Random Word List
    NumberOfLetters = list("_" * (len(RandomWord)-1))
    
    ListGuessLetters = []
    
    PlayerAttempts = 0
    
    print("".join(NumberOfLetters))
    
    #Create a loop that runs until the player has guessed incorrectly 5 times and the word is not guessed
    while PlayerAttempts < 5 and RandomWordList != NumberOfLetters:
      #take the user input 
      user_guess = input("Please guess a letter! ").lower()
      #make sure the user input is a letter
      if user_guess.isalpha():
            
        #if the user guesses a letter for the first time add that letter to the list of Guesses 
        if user_guess not in ListGuessLetters:
          ListGuessLetters.append(user_guess)
          z = 0   

          #run through the list and see at what index/indices the letter occurs at 
          if user_guess in RandomWordList:
            for i in RandomWordList:
              
              if i == user_guess:
                NumberOfLetters[z] = i

              z += 1

          #if the letter does not occur at any index then increase the count for the number of incorrect guesses  
          else:
            PlayerAttempts += 1
        
        # if the user guesses the same letter twice then increase the count for the number of incorrect guesses
        elif user_guess in ListGuessLetters:
          print("you have already guessed this letter")
          PlayerAttempts += 1
          
      #prints the combined string of _ and letters guessed
      print("".join(NumberOfLetters))


         
            
    # if the user finds all the letters before guessing incorrectly 5 times then they win     
    if RandomWordList == NumberOfLetters:
        print("Congrats, you guessed the word! You win!")
    
    #if the user guesses incorrectly 5 times then the user looses 
    else:
        print("Sorry, you ran out of tries. The word was " + "".join(RandomWordList) + ". Maybe next time!")

    
    

if __name__ == "__main__":
    main() 
