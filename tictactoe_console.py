import os
import tictactoe_console as tc
import tkinter as tk

def button_clicked_restart():
    window.destroy()
    os.startfile("TicTacToe_GUI.pyw")
import random

class TicTacToe:

    def __init__(self):
        self.field = [["_"] * 3 for _ in range(3)]
        self.player = random.choice(("X", "O"))
        self.winning_row = ""

    def set_field(self, field_content):
        self.field = [list(field_content[i:i+3]) for i in range(0, 9, 3)]

    def toggle_player(self):
        self.player = "O" if self.player == "X" else "X"

    def print_field(self):
        print("---------")
        for row in self.field:
            print("| " + " ".join(row) + " |")
        print("---------")

    def result(self):
        lines = self.field + [list(col) for col in zip(*self.field)] + \
                [[self.field[i][i] for i in range(3)], [self.field[i][2-i] for i in range(3)]]
        if any(line == ["X"] * 3 for line in lines):
            return "X has won"
        if any(line == ["O"] * 3 for line in lines):
            return "O has won"
        if any("_" in row for row in self.field):
            return "The game is not finished"
        return "The game ended in a draw"

    def is_valid_move(self, coordinate):
        try:
            y, x = map(int, coordinate.split())
            if 1 <= y <= 3 and 1 <= x <= 3 and self.field[y-1][x-1] == "_":
                return True, ""
            return False, "Invalid move. Try again."
        except ValueError:
            return False, "Please input coordinates as two numbers separated by a space."

    def move(self, coordinates):
        y, x = map(int, coordinates.split())
        self.field[y-1][x-1] = self.player

    def play(self):
        self.print_field()
        while True:
            print(f"It's your turn player {self.player}: ", end="")
            coordinates = input()
            valid, message = self.is_valid_move(coordinates)
            if valid:
                self.move(coordinates)
                result = self.result()
                if result == "The game is not finished":
                    self.toggle_player()
                    self.print_field()
                else:
                    self.print_field()
                    print(result)
                    break
            else:
                print(message)

if __name__ == '__main__':
    TicTacToe().play()
class MainApplication(tk.Frame):
    def change_button_text(self, button, text):
        self.Buttons[button - 1].configure(text=text)

    def change_playerlabel_text(self, text):
        self.Label_Player.configure(text=text)

    def change_outlabel_text(self, text):
        self.Label_Out.configure(text=text)

    def freeze(self):
        for button in self.Buttons:
            button["state"] = tk.DISABLED

    def highlight_winning_row(self):
        winning_row = game.winning_row
        indices = {
            "TOP": [0, 1, 2],
            "MIDDLE": [3, 4, 5],
            "BOTTOM": [6, 7, 8],
            "DOWN_L": [0, 3, 6],
            "DOWN_M": [1, 4, 7],
            "DOWN_R": [2, 5, 8],
            "DIAG_LL_UR": [6, 4, 2],
            "DIAG_UL_LR": [0, 4, 8]
        }
        for index in indices.get(winning_row, []):
            self.Buttons[index].configure(background="gold")

    def update_label_player(self):
        self.Label_Player.configure(text=("It's your turn player " + game.player + "!"))

    def button_clicked(self, button):
        coords = {
            1: "1 1", 2: "1 2", 3: "1 3",
            4: "2 1", 5: "2 2", 6: "2 3",
            7: "3 1", 8: "3 2", 9: "3 3"
        }
        coord = coords[button]
        if game.is_coordinate(coord):
            game.move(coord, game.player)
            self.change_button_text(button, game.player)
            self.Buttons[button - 1]["state"] = tk.DISABLED
            game.toggle_player()
            self.update_label_player()
            if game.result() != "The game is not finished":
                self.freeze()
                self.highlight_winning_row()
                self.change_outlabel_text(game.result())
        else:
            self.change_outlabel_text(game.is_coordinate(coord)[1])

    # Aufbau der Gui, ab hier nichts verändern
    def __init__(self, root, *args, **kwargs):
        # main Frame
        tk.Frame.__init__(self, root, *args, **kwargs)

        # configure main window
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#ececec'

        window.geometry("638x512+688+286")
        window.minsize(120, 1)
        window.maxsize(2052, 1133)
        window.resizable(0, 0)
        window.title("TicTacToe")
        window.configure(background="#004240")

        # configure widgets
        self.Buttons = []
        button_configs = [
            (0.235, 0.234, self.button_clicked, 1),
            (0.408, 0.234, self.button_clicked, 2),
            (0.581, 0.234, self.button_clicked, 3),  # Adjusted
            (0.235, 0.449, self.button_clicked, 4),
            (0.408, 0.449, self.button_clicked, 5),
            (0.581, 0.449, self.button_clicked, 6),  # Adjusted
            (0.235, 0.664, self.button_clicked, 7),
            (0.408, 0.664, self.button_clicked, 8),
            (0.581, 0.664, self.button_clicked, 9)   # Adjusted
        ]
        for relx, rely, command, button_number in button_configs:
            button = tk.Button(window)
            button.place(relx=relx, rely=rely, height=114, width=117)
            button.configure(activebackground="#ececec")
            button.configure(activeforeground="#000000")
            button.configure(background="#d9d9d9")
            button.configure(disabledforeground="#a3a3a3")
            button.configure(font="-family {Eras Light ITC} -size 18 -weight bold")
            button.configure(foreground="#000000")
            button.configure(highlightbackground="#d9d9d9")
            button.configure(highlightcolor="black")
            button.configure(pady="0")
            button.configure(cursor="hand2")
            button.configure(text="")
            button.configure(command=lambda bn=button_number: command(bn))
            self.Buttons.append(button)

        Button_Restart = tk.Button(window)
        Button_Restart.place(relx=0.768, rely=0.176, height=44, width=77)
        Button_Restart.configure(activebackground="#ececec")
        Button_Restart.configure(activeforeground="#000000")
        Button_Restart.configure(background="#d9d9d9")
        Button_Restart.configure(disabledforeground="#a3a3a3")
        Button_Restart.configure(font="-family {Fixedsys} -size 9")
        Button_Restart.configure(foreground="#000000")
        Button_Restart.configure(highlightbackground="#d9d9d9")
        Button_Restart.configure(highlightcolor="black")
        Button_Restart.configure(pady="0")
        Button_Restart.configure(text='''Restart''')
        Button_Restart.configure(command=button_clicked_restart)

        self.Label_Title = tk.Label(window)
        self.Label_Title.place(relx=0.0, rely=0.0, height=41, width=644)
        self.Label_Title.configure(background="#006a68")
        self.Label_Title.configure(disabledforeground="#a3a3a3")
        self.Label_Title.configure(font="-family {Fixedsys} -size 18 -weight bold")
        self.Label_Title.configure(foreground="#b3fffd")
        self.Label_Title.configure(relief="raised")
        self.Label_Title.configure(text='''TicTacToe''')

        self.Label_Out = tk.Label(window)
        self.Label_Out.place(relx=0.135, rely=0.898, height=31, width=500)
        self.Label_Out.configure(background="#004240")
        self.Label_Out.configure(disabledforeground="#a3a3a3")
        self.Label_Out.configure(font="-family {Fixedsys} -size 12 -weight bold")
        self.Label_Out.configure(foreground="#b3fffd")
        self.Label_Out.configure(text="")

        self.Label_Player = tk.Label(window)
        self.Label_Player.place(relx=0.235, rely=0.176, height=31, width=337)
        self.Label_Player.configure(background="#5d5d5d")
        self.Label_Player.configure(disabledforeground="#a3a3a3")
        self.Label_Player.configure(font="-family {Fixedsys} -size 9")
        self.Label_Player.configure(foreground="#ffffff")
        self.Label_Player.configure(relief="raised")
        self.Label_Player.configure(text=("It's your turn player "+game.player+"!"))

# main
if __name__ == '__main__':
    game = tc.TicTacToe()
    window = tk.Tk()
    MainApplication(window).place()
    window.mainloop()