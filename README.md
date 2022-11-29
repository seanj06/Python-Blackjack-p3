# Python Blackjack

## Overview
A Python terminal game based on the popular card game Blackjack.

Game developed by Sean Johnston for Code Institute Project Portfolio 3 using Python.

[Live Game Link](https://python-blackjack.herokuapp.com/)

![Home Screen](docs/README-images/Home-screen.png)

## How to play 
This game was designed to be very simple to play and user friendly.
Instructions are given along the way of what key to press to continue the game and the first letter of the input corresponds to the target word(for example S to start game).

The aim of the game is to get as close to 21 as you can without going over it. If you do you will bust and lose the hand. If the dealer gets closer to 21 than you do you will also lose.

At the start of each hand you will be dealt 2 cards. You will then be given the choice whether to hit or stand. If you choose hit you will be dealt another card, if you choose stand it is the dealers turn. The dealer has to hit until they reach 17.

Each card number is worth its value, Jacks, Queens and Kings are worth 10 and Aces are worth both 11 and 1(If you get an Ace and will be over 21 it changes to a 1).

There is also a very simple chip betting system in the game. You will start the game with 500 chips and at the beginning of every hand will be given the choice of how many chips you want to bet. If you win the hand you double the amount of chips you bet and if you lose the hand you lose all the chips you bet. If you run out of chips its game over and the game restarts.


## Project Goals

 - This project was created for project 3 of Code Institutes Diploma in full stack web development.

 - ### Main goals of this project include
  
   - Creating a fully functional blackjack terminal game using python.

   - Making the game as realistic as possible for the user

   - Making the game easy to understand for the user while also including game instructions.

 - ### Target audience of the project include 

   - Users that have an interest in card games

   - Users that have an interest in playing simple terminal games for fun.

## User stories

 - As a user I want

   - Clear instructions on how to start the game.
   
   - Instructions on how to play the game

   - An option to play the game again when finished

   - To be able to enter a username

   - Game feedback if I have an incorrect input

## Features

 ### Start screen

 ![Start Screen](docs/README-images/start-screen.png)

 The start screen features a "Welcome To Blackjack" ascii text message and a message prompting the user to either press S to start the game or I for the instruction screen.

  - If the user presses the S key they are shown a prompt to enter their username.
  If the username is valid the user is shown a welcome message and the game starts.
 ![Username](docs/README-images/Home-screen.png)

  - If the user presses the I key they are brought to the instructions page where text is typed out in a typewrite effect and user is given a prompt to enter any key to return to the main menu
  ![Instruction Page](docs/README-images/ins-page.png)

  ### Bet Input

  ![Bet Input](docs/README-images/Chip-input.png)

  After the user enters a valid username, they are brought to the bet input screen which asks them how many chips they would like to bet

   - If the user tries to bet more chips than they currently have they are shown an error message telling them they dont have enough chips to place the bet.
   ![Invalid Bet](docs/README-images/invalid-bet.png)

   - If the user tries to type in a bet amount that is not a number or zero they are shown an error message that asks them to type in a valid bet amount.
   ![Invalid Bet 2](docs/README-images/nan.png)

   - If the user enters a valid bet amount they are shown and ascii message telling them the cards are being dealt before moving on to the next screen.
   ![Dealing Cards](docs/README-images/deal-cards.png)
 

