#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 16:29:20 2022

@author: gunnarfranko
"""

import pandas as pd
import numpy as np


class Die:
    '''
    A die has N sides, or “faces”, and W weights, and can be rolled to select a face. 
    W defaults to 1.0 for each face but can be changed after the object is created.
    The die has one behavior, which is to be rolled one or more times.
    '''
    def __init__(self, N):
        '''
        Takes an array of faces as an argument. The array's data type (dtype) may be strings or numbers.
        Internally iInitializes the weights to 1.0 for each face.
        Saves both faces and weights into a private dataframe that is to be shared by the other methods.

        '''
        self.faces = N
        self.weights = np.ones(len(N))
        self._diedf = pd.DataFrame({'faces':self.faces, 'weights':self.weights})
        
    def change_weight(self, face, weight):
        '''
        Takes two arguments: the face value to be changed and the new weight.
        Checks to see if the face passed is valid; is it in the array of weights?
        Checks to see if the weight is valid; is it a float? Can it be converted to one?

        '''
        if type(weight) != float:
            print('Weight is not a float')
        elif any(face == self._diedf['faces']):
            self._diedf.loc[self._diedf['faces']==face, 'weights']= weight
        else:
            print('Face does not exist')
    
    def roll(self, times=1):
        '''
        Takes a parameter of how many times the die is to be rolled; defaults to 1. 
        This is essentially a random sample from the vector of faces according to the weights.
        Returns a list of outcomes.
        Does not store internally these results. 

        '''
        return(self._diedf['faces'].sample(times,replace=True,
                                           weights=self._diedf['weights']/sum(self._diedf['weights'])))
    
    def show(self):
        '''
        Returns the dataframe created in the initializer.

        '''
        return(self._diedf)
        
            


class Game(Die):
    '''
    A game consists of rolling of one or more dice of the same kind one or more times. 
    Each game is initialized with one or more of similarly defined dice (Die objects).
    By “same kind” and “similarly defined” we mean that each die in a given game has 
    the same number of sides and associated faces, but each die object may have its own weights.
    The class has a behavior to play a game, i.e. to rolls all of the dice a given number of times.
    The class keeps the results of its most recent play. 
    '''
    def __init__(self, dies):
        '''
        Takes a single parameter, a list of already instantiated similar Die objects.

        '''
        self.dies = dies
     
    def play(self, nrolls):
        '''
        Takes a parameter to specify how many times the dice should be rolled.
        Saves the result of the play to a private dataframe of shape N rolls by M dice.
        The private dataframe should have the roll number is a named index.

        '''
        self._playdf= pd.DataFrame()
        counter = 0
        for i in self.dies:
            counter += 1
            self._playdf['Die '+str(counter)]=(i.roll(nrolls)).tolist()
        dexcount = 0
        self.playdex = []
        for i in range(nrolls):
            dexcount +=1
            self.playdex.append('Roll '+str(dexcount).zfill(len(str(nrolls))))
        self._playdf.index = (self.playdex)
    
    def Gshow(self, form = 'wide'):
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
        form = form
        if form == 'wide':
            return(np.transpose(self._playdf))
        elif form =='narrow':
            return( self._playdf.stack())
        else:
            print('Invalid Form')



class Analyzer(Game):
    '''
    An analyzer takes the results of a single game and computes various descriptive 
    statistical properties about it. These properties results are available as attributes 
    of an Analyzer object. 

    '''
    
    def __init__(self, game):
        '''
        Takes a game object as its input parameter. 
        At initialization time, it also infers the data type of the die faces used.

        '''
        self.game = game
        self.ftype = type(self.game.dies[0]._diedf['faces'][0])
        
    def jackpot(self):
        '''
        Returns an integer for the number times to the user.
        Stores the results as a dataframe of jackpot results in a public attribute.
        The dataframe should have the roll number as a named index.

        '''
        self.jpotdf = self.game._playdf
        for row in self.game._playdf.index:
            if len(np.unique(self.game._playdf.loc[row,:])) >1 :
                self.jpotdf = self.jpotdf.drop(row)
        self.numjpot = len(self.jpotdf)
        return(int(self.numjpot))
        
    def combo(self):
        '''
        Combinations should be sorted and saved as a multi-columned index.
        Stores the results as a dataframe in a public attribute.
        '''
        self.combo = self.game._playdf.apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('n')
        return(self.combo)
    
    def face_counts_per_roll(self):
        '''
        Stores the results as a dataframe in a public attribute.
        The dataframe has an index of the roll number and face values as columns (i.e. it is in wide format).
        '''
        self.fcpr = self.game._playdf.stack().groupby(level=0).value_counts().unstack(fill_value=0)
        return(self.fcpr)










