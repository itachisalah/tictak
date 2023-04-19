import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class TicTacToeApp(App):
    def build(self):
        self.board = GridLayout(cols=3, rows=3)
        self.board.bind(minimum_height=self.board.setter('height'))
        self.board.bind(minimum_width=self.board.setter('width'))

        # create buttons and add to board
        self.buttons = []
        for i in range(9):
            btn = Button(text="")
            btn.bind(on_release=self.on_button_release)
            self.board.add_widget(btn)
            self.buttons.append(btn)

        return self.board

    def on_button_release(self, btn):
        self.player_move(btn)
        self.computer_move()

    def player_move(self, btn):
        # player makes a move
        btn.text = "X"
        btn.disabled = True
        self.check_for_winner()

    def computer_move(self):
        # computer makes a move
        btn = self.get_available_button()
        if btn:
            btn.text = "O"
            btn.disabled = True
            self.check_for_winner()

    def get_available_button(self):
        # get a list of available buttons
        available = [btn for btn in self.buttons if btn.text == ""]
        if available:
            return random.choice(available)
        return None
    def check_for_winner(self):
        # check rows
        for row in range(3):
            if (
                self.buttons[row*3].text == self.buttons[row*3+1].text == self.buttons[row*3+2].text
                and self.buttons[row*3].text != ""
            ):
                self.show_winner(self.buttons[row*3].text)

        # check columns
        for col in range(3):
            if (
                self.buttons[col].text == self.buttons[col+3].text == self.buttons[col+6].text
                and self.buttons[col].text != ""
            ):
                self.show_winner(self.buttons[col].text)

        # check diagonals
        if (
            self.buttons[0].text == self.buttons[4].text == self.buttons[8].text
            and self.buttons[0].text != ""
        ):
            self.show_winner(self.buttons[0].text)
        if (
            self.buttons[2].text == self.buttons[4].text == self.buttons[6].text
            and self.buttons[2].text != ""
        ):
            self.show_winner(self.buttons[2].text)

        if all(btn.text != "" for btn in self.buttons):
            self.show_winner("T")
            
    def show_winner(self, winner):
        if winner == "X":
            msg = "You won!"
        elif winner == "O":
            msg = "You lost."
        else:
            msg = "It's a tie."

        popup = Popup(title=msg, content=Label(text=msg), size_hint=(None, None), size=(200, 200))
        popup.open()


if __name__ == "__main__":
    TicTacToeApp().run()