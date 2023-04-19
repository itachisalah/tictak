# tic-tac-toe-python

This is a simple implementation of the classic game Tic-Tac-Toe, written in Python using the Kivy library for the user interface. The game board is represented by a 3x3 grid of buttons, and two players take turns placing their respective symbols (either an "X" or an "O") on the board by clicking the corresponding buttons.

## Getting Started

To get started with the game, you will need to have Python and the Kivy library installed on your computer. You can install Kivy by running the following command:
```
pip install kivy
```
After that, you can run the game by running the TicTacToe.py file
```
python main.py
```

## Features

- The TicTacToeApp class is the main class that represents the game and it's derived from kivy's App class, which provides the basic structure for a Kivy application.
- The `build` method of this class is responsible for creating the 3x3 grid of buttons and setting up the event handler to handle button clicks.
- The `button_pressed` method is the event handler that's called when a button is clicked. It takes the button that was clicked as an argument, and it's responsible for updating the button text to display the current player's symbol and for disabling the button so that it cannot be clicked again.

## Tips

- The game is still missing some features like checking for win or draw, restarting the game, showing message when one wins, etc. So feel free to add them and make this game better.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
