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



