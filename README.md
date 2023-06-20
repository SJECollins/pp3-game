# Python Terminal Game

## Battleship

Based on [gbrough's battleship repo](https://github.com/gbrough/battleship)

### Printing the boards:
Based on this [Stack Overflow thread](https://stackoverflow.com/questions/41869481/print-two-or-more-outputs-from-functions-side-by-side-in-python)
- Using:
    - The ["end"](https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/) parameter in the print statements to prevent a default new line
    - ["Yield"](https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/) to halt printing while each function executes its respective lines
    - The ["next()"](https://www.geeksforgeeks.org/python-next-method/) function in our while loop to execute both board printing functions in our while loop

### Adding ships to boards:
Using randint to pick a starting point on the board (between 1 and 10, minus the ship length) and which direction the ship is facing on the board (x or y).
- We create lists of row or column cells in a range from the "start" to the end of the ship
- For our columns we also need to convert the random numbers we created to characters using the [chr()](https://www.w3schools.com/python/ref_func_chr.asp) function on the column number plus 96.
- We'll then create a list (using the [zip()](https://www.w3schools.com/python/ref_func_zip.asp) function to convert our rows & cols to tuples) of our coordinates that we'll pass on to our check_overlap() function

Our check_overlap() function loops through our coordinates and checks whether [any()](https://www.geeksforgeeks.org/python-any-function/) of the coordinates are already present in the given ship list. If so, we'll send that ship back through the add_ships() function to create new coordinates. If not, we'll append the coordinates to the ship lists and print the ships to the board. We'll be using our ship list to check our inputs against, rather than reading the board itself.

### User & comp moves, updating board:
get_user_move() function prompts user for row number and column letter inputs with simple while loops to check whether input is "not in" the accepted answers. get_comp_move() generates random row and column numbers, and converts column number to character.

Both functions create tuples from the inputs/generated coordinates and pass those, plus the enemy's ship list, board, and the player variable (set to True in the user's function) to check_hit().

The check_hit() function then loops through each of the ships in given ship list, checks if the move is within that ship (which is itself a list of tuples), and then checks the length of the ship. If there's only one coordinate left in the ship, you sunk a battleship! Otherwise, we'll remove the matching coordinates, so shortening the ship.

After that, it prints the moves and updates the boards accordingly, with an "X" for a hit and an "O" for a miss.

We also update the main() function to include a while loop to get our inputs and print our boards as they're updated.

Could probably make the computer function a little smarter. What if the last move hit a ship? Should the computer then look in neighbouring cells for further hits?? Otherwise human is always at a massive advantage.

### Prevent user and computer inputting same coordinates multiple times
So, one thing about checking the ship list vs reading the board, is that there's no way to tell from the ship list if you've already missed on one spot. Obviously the user could read the board, but what's to prevent them entering the same coordinates anyway? And the computer could randomly hit the same spot twice because it's not smart.

Added a parent while loop for inputs and an if statement to check whether the move is within a list of the player/computer's previous moves.

### Endgame
End game conditions are simple, updated while loop in main() to only run while user AND computer ships are above 0. Once one or the other reaches 0, the loop breaks and we go to our end_game() function.

### Coloured board
Updated the board to print in colour using simple [ANSI colour codes](https://en.wikipedia.org/wiki/ANSI_escape_code). Created a basic class with the colour codes, may build on that...

### Computer moves
Updated the get_comp_move() function to first check the player's board for hit_icons indicating that it's already hit a boat (also now the hit_icons change to sunk_icons when a boat is sunk on either board, so the computer can differentiate - it can't read the "You sunk a battleship!" message after all (also, have changed from simple characters to [object]_icons on the boards due to the colours (alot of alsos))). So, if a hit_icon exists on the board, the computer will check if a hit_icon also exists below or to the right and if so will see if it can it above or to the left (because it will have passed those on its way to the hit_icon), that way it can also work backwards from a hit in a semi-intelligent way following the right direction. Otherwise, it'll try whatever cell is available to hit around a long hit_icon.

There's probably a smarter way to do it, but it's my day off. Also, should probably think about what is the smartest pattern to follow when the computer doesn't have a hit_icon to focus on because right now it just shoots randomly.

### Placing ships
So just a quick thing, but added an option for user to place their own ships. A frankenstein of while loops for input, with copies of pieces of existing code to check if the boat fits or overlaps and then print it to the board. Nothing fancy. Could be refactored.


## Hangman
Not really based on anything. Nothing too complicated, almost half the file is made of the strings for the man.

### Getting the word
Using [Random word API](https://random-word-api.herokuapp.com/home), a handy Heroku app, we get a random word. The get_word() function also checks if the word is more than ten letters - to avoid anything too ridiculous - and calls itself (RECURSION OH NO!) if so.

## Checking for a win
The only other new thing here is the use of the [all()](https://www.w3schools.com/python/ref_func_all.asp) function in our check_win(). all() returns True if all the elements in an iterable are True, so here we're setting the "won" variable to true if all the letters in the word are in our guesses.

