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


## Manifest
