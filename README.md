# simter
Python/Tkinter item calculator for SimCity BuildIt.

This GUI application is a utility with which to keep track of items necessary for building upgrades.

## Dependencies

simter runs via the `python-tk` library.
On Ubuntu systems: `sudo apt install python-tk`

All items produced in commercial buildings are displayed as buttons.
Each time a button is clicked, a dictionary is modified containing keys for items needed, and printed to the screen.

The "smart" part is that it automatically calculates for ITEMS NEEDED TO PRODUCE OTHER ITEMS.
For example, 2 boards are needed to produce 1 ladder.
When the ladder is clicked,
the integer value for "ladders" is increased by 1,
while "boards" is increased by 2.

Sweet!

At that point you are presented with a "shopping list", as it were.
The next version will include a separate button or toggle to subtract items as they are bought or placed into production.
In the meantime I wrote another app which is the exact same thing only subtracts values.

Enjoy!
