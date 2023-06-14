# Python Terminal Game

## Battleship

Based on [gbrough's battleship repo](https://github.com/gbrough/battleship)

### Printing the boards:
Based on this [Stack Overflow thread](https://stackoverflow.com/questions/41869481/print-two-or-more-outputs-from-functions-side-by-side-in-python)
- Using:
    - The ["end"](https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/) parameter in the print statements to prevent a default new line
    - ["Yield"](https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/) to halt printing while each function executes its respective lines
    - The ["next()"](https://www.geeksforgeeks.org/python-next-method/) function in our while loop to execute both board printing functions in our while loop