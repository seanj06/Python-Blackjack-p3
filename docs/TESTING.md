## Unit Testing

 Below is a table of every function unit test, the method of testing and pass or fail.
 If result was fail more info can be found in the fixed bugs section.

 |Function tested | Method of testing  | Result  |   
|---|---|---|
| new_deck()   | Created test decks to make sure cards were being added accordingly and shuffled.  | Pass  |   
| deal_card()  | Created test hand variable to make sure cards were beng taken from deck accordingly. Checked length of deck was getting smaller as cards were being taken  | Pass  |   
| hand_value()  | Created test list variables to make sure hand values matched up accordingly.  | Fail (see fixed bugs section.)  | 
|check_winner()| Created test player and dealer hands and passed them as arguments into check winner function | Pass |
| start_screen() | Checked both inputs are validated correcty and worked accordingly | Pass |
| name_input() | Checked user could only type in letters for username. | Fail (see fixed bugs section.) |
| instructions() | Checked all printed text lined up correctly and was not distorted. | Fail (see fixed bugs section.) |
| main() | Went through start screen process and played through a few main game loops to make sure main game loop was functioning correctly. | Fail (see fixed bugs section.) |
| bet() using Chips class | Played through a few main game loops and made sure chips were being taken and added to player chip stack accordingly. | Fail (see fixed bugs section) |
| play_again() | Played through main game loops to make sure user  input validation was working correctly, if user pressed yes a new deck was created and the user kept current chip stack. If user selected no chip stack was reset. | Fail (see fixed bugs section.) |
| clear() | Checked that screen was being cleared anytime function was called | Pass |

## Fixed bugs

 Below is a description of fixed bugs from unit test fails.

 ### hand_value()

  - #### Reason for fail:

    - When testing hand values I noticed that the value of Aces were not changing accordingly to 1 instead of 11.

  - #### Fix:

    - After some testing I concluded the problem was because of the way I had written my hand value function. I originally had the function set up to check if the string value "A" was in hand and hand value was > 10 change the value to 1. I changed the function to keep track of aces then made a while loop to state while number of aces is > 0 and value is < 21 take 10 away from hand total. See below code snippet for function solution.
    
  ![Hand Value Solution](README-images/hand_value.png) 

  ### name_input()

  - #### Reason for fail:

    - When testing the name input I noticed that the user could type in any character other than letters including directional buttons and the input would be validated, even though I had set up my code to prevent this.

  - #### Fix:

    - After some more testing and research I concluded that I need to add the .strip() method at the end of my name input to get rid of any whitespace, I also need to add the .isalpha() method to make sure any input was a letter. See below code snippet for function solution.

   ![Name Input Solution](README-images/name-input.png)   

  ### instructions()

  - #### Reason for fail:

    - When testing my instruction screen text I noticed that the text was not lining up correctly when deployed on Heroku.

  - #### Fix:

    - After some more testing and research I concluded that the new line method I was using was incorrect. I had been using \ (backslashes) to enter a new line of text but I found if i simply used inverted commas and lined up the text in a block along with \n, the text would line up as I wanted. See below code snippet for function solution.

   ![Instruction text solution](README-images/instruction-solution.png)   
