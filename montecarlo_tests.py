#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 22:27:20 2022

@author: gunnarfranko
"""
import unittest
import montecarlo
import pandas


class montecarloTestSuite(unittest.TestCase):
    '''
    Includes unittests for each method in each class of the montecarlo.py
    '''
    
    def test_1_change_weight(self):
        '''
        Adds a Die, Changes weight then tests if weight is different
        '''
        d1 = montecarlo.Die(['H','T'])
        d1.change_weight('H',3.0)
        self.assertFalse(d1._diedf['weights'][0]==1.0)
        
    def test_2_roll(self):
        '''
        Sets a number of rolls for the game and makes sure that it rolls that many times
        '''
        d1 = montecarlo.Die(['H','T'])
        d2 = montecarlo.Game([d1,d1])
        d2.play(43)
        test2 = len(d2._playdf)
        self.assertEqual(test2, 43)
        
    def test_3_show(self):
        '''
        Runs the game then sees if the wide function works for dataframe of rolls
        '''
        d1 = montecarlo.Die(['H','T'])
        test3 = type(d1._diedf)
        self.assertEqual(test3, pandas.core.frame.DataFrame)
    
    
    def test_4_play(self):
        '''
        Runs the play and tests that it returns dataframe
        '''
        d1 = montecarlo.Die(['H','T'])
        d2 = montecarlo.Game([d1,d1])
        d2.play(43)
        test4 = type(d2._playdf)
        self.assertEqual(test4, pandas.core.frame.DataFrame)
        
    def test_5_play(self):
        '''
        Runs same play as test 4 and tests to see if the length of data frame is same as number of rolls 
        '''
        d1 = montecarlo.Die(['H','T'])
        d2 = montecarlo.Game([d1,d1])
        d2.play(43)
        test5 = len(d2._playdf)
        self.assertEqual(test5, 43)
        
    def test_6_Gshow(self):
        '''
        Runs same game and tests to see if the wide works
        '''
        d1 = montecarlo.Die(['H','T'])
        d2 = montecarlo.Game([d1,d1])
        d2.play(43)
        test6 = len(d2.Gshow('wide'))
        self.assertEqual(test6, 2)
        
    def test_7_Gshow(self):
        '''
        Runs same game and tests to see if the narrow works 
        '''
        d1 = montecarlo.Die(['H','T'])
        d2 = montecarlo.Game([d1,d1])
        d2.play(43)
        test7 = len(d2.Gshow('narrow'))
        self.assertEqual(test7, 86)
        
    def test_8_jackpot(self):
        '''
        Runs same game and tests to see if jackpot returns an int 
        '''
        d1 = montecarlo.Die(['H','T'])
        d2 = montecarlo.Game([d1,d1])
        d2.play(43)
        d3 = montecarlo.Analyzer(d2)
        test8 = type(d3.jackpot())
        self.assertEqual(test8, int)
        
    def test_9_combo(self):
        '''
        Runs the game and tests to see if combo dataframe has right dimensions
        '''
        d1 = montecarlo.Die(['H','T'])
        d2 = montecarlo.Game([d1,d1])
        d2.play(43)
        d3 = montecarlo.Analyzer(d2)   
        test9 = d3.combo().shape
        self.assertEqual(test9, (3,1))

    def test_10_face_counts_per_roll(self):
        '''
        Runs the game and tests to see if facecount dataframe has right dimensions
        '''        
        d1 = montecarlo.Die(['H','T'])
        d2 = montecarlo.Game([d1,d1])
        d2.play(43)
        d3 = montecarlo.Analyzer(d2)   
        test10 = d3.face_counts_per_roll().shape  
        self.assertEqual(test10, (43,2))
        
    def test_11_init(self):
        '''
        Tests to see if the Die class initializes 

        '''
        try:
            d1 = montecarlo.Die(['1', '2', '3', '4'])
        except RuntimeError:
            print('The Die was not created')
        
    def test_12_init(self):
        '''
        Tests to see if the Game class initializes
        '''
        try:
            d1 = montecarlo.Die(['1', '2', '3', '4'])
            d2 = montecarlo.Game([d1,d1])
        except RuntimeError:
            print('The Game was not created')
        
    def test_13_init(self):
        '''
        Tests to see if the Analyzer class initializes 
        '''
        try:
            d1 = montecarlo.Die(['1', '2', '3', '4'])
            d2 = montecarlo.Game([d1,d1])
            d2.play(43)
            d3 = montecarlo.Analyzer(d2)
        except RuntimeError:
            print('The Game was not Analyzed')
        
        
    
    
if __name__ == '__main__':
    unittest.main(verbosity=3)
   

   

   
    
   
    
   
    