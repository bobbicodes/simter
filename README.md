# simter
Python/Tkinter Inventory and Production Management Tool

![](https://github.com/porkostomus/simter/blob/master/2018-05-09-204120_1366x768_scrot.png)

## Dependencies

simter runs via the `python-tk` library.
On Ubuntu systems: `sudo apt install python-tk`

## Usage

    python -m simter

This GUI application tracks your inventory and items needed for upgrades.
Items are organized by store where they're produced.
Performs appropriate calculations in regard to other items - 
For example, it takes into account that producing 1 pizza in turn requires 2 cheeses.

Sweet!
