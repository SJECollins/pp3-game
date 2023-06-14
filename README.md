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

Our check_overlap() function loops through our coordinates and checks whether [any()](https://www.geeksforgeeks.org/python-any-function/) of the coordinates are already present in the given ship list. If so, we'll send that ship back through the add_ships() function to create new coordinates.



