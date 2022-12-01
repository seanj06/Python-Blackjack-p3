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
| play_again() | Played through main game loops to make sure user  inpput validation was working correctly, if user pressed yes a new deck was created and the user kept current chip stack. If user selected no chip stack was reset. | Fail (see fixed bugs section.) |
| clear() | Checked that screen was being cleared anytime function was called | Pass |

