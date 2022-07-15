# MonteCarlo-Project
## Metadata
Name: Gunnar Franko  
ID: gbf6qz  
Project Name: Monte Carlo Simulator 


## Synopsis
This repo has a package for a die game. When given faces it can roll any amount of similar die (meaning they have the same faces) any number of times. The weights of the die can be changed to give certain faces advantages in a roll. Using it you can return a few things such as the number for each face for a game, the number of each combonation of faces for a game, and number of jackpots for a game (number of rolls where all faces are the same). 
### Installing
To install the game you would execute: 
```
!cd Package/; pip install 
```
### Importing
To import the game you: 
```
from MC Package import montecarlo
```
### Creating Dice
To Create a Die, you have to call the Die class and specify the faces: 
```
Die1 = montecarlo.Die(['Heads', 'Tails']
```
### Playing Games
To Initialize a game you have to call the Game class using Die objects that have been created. Then you use the .play() function within the Game class, specifying the number of times the die is rolled. 
```
Die1 = montecarlo.Die(['Heads', 'Tails'])
#creates a Die object with Heads and Tails as faces
Game1 = Die1.Game([Die1, Die1])
#creates a Game object with 2 of the H/T die
Game1.play(43)
#This creates the game with 2 H/T die that is rolled 43 times. 
```

### Analyzing Games
To Analzye the Game you call the Analyze Class using a Game that has been run. Then you can choose from the .combo(), .jackpot(), and .face_counts_per_roll() methods to get the type of analyzation you want 

```
Die1 = montecarlo.Die(['Heads', 'Tails'])
#creates a Die object with Heads and Tails as faces
Game1 = Die1.Game([Die1, Die1])
#creates a Game object with 2 of the H/T die
Game1.play(43)
#This creates the game with 2 H/T die that is rolled 43 times. 
#All of this is the same as before
An1 = Game1.Analyzer(Game1)
#This creates the An1 object using Game 1
```

## API Description

### class Die
'''
    A die has N sides, or “faces”, and W weights, and can be rolled to select a face. 
    W defaults to 1.0 for each face but can be changed after the object is created.
    The die has one behavior, which is to be rolled one or more times.
'''  
#### change_weight()
'''
        Takes two arguments: the face value to be changed and the new weight.
        Checks to see if the face passed is valid; is it in the array of weights?
        Checks to see if the weight is valid; is it a float? Can it be converted to one?
'''  
Inputs:  
Faces - The Face of the die that you want to change the weight (type str)  
Weights - The value of the new weight (type float)  
Outputs:  
The updated dataframe with new weights 
#### roll()
'''
        Takes a parameter of how many times the die is to be rolled; defaults to 1. 
        This is essentially a random sample from the vector of faces according to the weights.
        Returns a list of outcomes.
        Does not store internally these results. 
'''  
Inputs:  
times - The number of times that you want to roll the dice. Default value is 1.  
Outputs:  
A list of the results for each roll
#### show
'''
        Returns the dataframe created in the initializer.
'''  
Outputs:   
The dataframe of the dies and their weights 


#### class Game
'''
    A game consists of rolling of one or more dice of the same kind one or more times. 
    Each game is initialized with one or more of similarly defined dice (Die objects).
    By “same kind” and “similarly defined” we mean that each die in a given game has 
    the same number of sides and associated faces, but each die object may have its own weights.
    The class has a behavior to play a game, i.e. to rolls all of the dice a given number of times.
    The class keeps the results of its most recent play. 
'''
#### play()
'''
        Takes a parameter to specify how many times the dice should be rolled.
        Saves the result of the play to a private dataframe of shape N rolls by M dice.
        The private dataframe should have the roll number is a named index.
'''
#### Gshow()
'''
        This method just passes the private dataframe to the user.
        Takes a parameter to return the dataframe in narrow or wide form.
        This parameter defaults to wide form.
        This parameter should raise an exception of the user passes an invalid option.
        The narrow form of the dataframe will have a two-column index with the roll number 
        and the die number, and a column for the face rolled.
        The wide form of the dataframe will a single column index with the roll number, 
        and each die number as a column.
'''


### class Analyzer
'''
    An analyzer takes the results of a single game and computes various descriptive 
    statistical properties about it. These properties results are available as attributes 
    of an Analyzer object. 
'''
#### jackpot()
'''
        Returns an integer for the number times to the user.
        Stores the results as a dataframe of jackpot results in a public attribute.
        The dataframe should have the roll number as a named index.
'''
#### combo()
'''
        Combinations should be sorted and saved as a multi-columned index.
        Stores the results as a dataframe in a public attribute.
'''
#### face_counts_per_roll()
 '''
        Stores the results as a dataframe in a public attribute.
        The dataframe has an index of the roll number and face values as columns (i.e. it is in wide format).
'''



## Manifest
