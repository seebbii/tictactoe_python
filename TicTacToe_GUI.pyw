import os
import tictactoe_console as tc
import tkinter as tk


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
            "DIAG_UL_LR": [0, 4, 8],
            "DIAG_LL_UR": [6, 4, 2]
        }
        for index in indices.get(winning_row, []):
            self.Buttons[index].configure(background="gold")

    def update_label_player(self):
        self.Label_Player.configure(text=f"It's your turn player {game.player}!")
        
    def button_clicked_restart(self):
        global game
        game = tc.TicTacToe()  # Reset the game instance
        self.change_outlabel_text("")  # Clear the output label
        self.update_label_player()  # Update the player label
        for button in self.Buttons:
            button.configure(text="", state=tk.NORMAL, background="#d9d9d9") 
            
    def button_clicked(self, button):
        coords = {
            1: "1 1", 2: "1 2", 3: "1 3",
            4: "2 1", 5: "2 2", 6: "2 3",
            7: "3 1", 8: "3 2", 9: "3 3"
        }
        coord = coords[button]
        valid, message = game.is_valid_move(coord)
        if valid:
            game.move(coord)
            self.change_button_text(button, game.player)
            self.Buttons[button - 1]["state"] = tk.DISABLED
            if game.result() != "The game is not finished":
                self.freeze()
                self.highlight_winning_row()
                self.change_outlabel_text(game.result())
            else:
                game.toggle_player()
                self.update_label_player()
        else:
            self.change_outlabel_text(message)

    # Aufbau der GUI, ab hier nichts verändern
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)

        # configure main window
        window.geometry("638x512+688+286")
        window.minsize(120, 1)
        window.maxsize(2052, 1133)
        window.resizable(0, 0)
        window.title("TicTacToe")
        window.configure(background="#004240")

        # configure buttons
        self.Buttons = []
        button_configs = [
            (0.235, 0.234, self.button_clicked, 1),
            (0.408, 0.234, self.button_clicked, 2),
            (0.581, 0.234, self.button_clicked, 3),
            (0.235, 0.449, self.button_clicked, 4),
            (0.408, 0.449, self.button_clicked, 5),
            (0.581, 0.449, self.button_clicked, 6),
            (0.235, 0.664, self.button_clicked, 7),
            (0.408, 0.664, self.button_clicked, 8),
            (0.581, 0.664, self.button_clicked, 9)
        ]
        for relx, rely, command, button_number in button_configs:
            button = tk.Button(window)
            button.place(relx=relx, rely=rely, height=114, width=117)
            button.configure(activebackground="#ececec", background="#d9d9d9", font="-family {Eras Light ITC} -size 18 -weight bold", text="", command=lambda bn=button_number: command(bn))
            self.Buttons.append(button)

        Button_Restart = tk.Button(window)
        Button_Restart.place(relx=0.768, rely=0.176, height=44, width=77)
        Button_Restart.configure(activebackground="#ececec", background="#d9d9d9", font="-family {Fixedsys} -size 9", text='''Restart''', command=self.button_clicked_restart)

        self.Label_Title = tk.Label(window)
        self.Label_Title.place(relx=0.0, rely=0.0, height=41, width=644)
        self.Label_Title.configure(background="#006a68", font="-family {Fixedsys} -size 18 -weight bold", foreground="#b3fffd", text='''TicTacToe''')

        self.Label_Out = tk.Label(window)
        self.Label_Out.place(relx=0.135, rely=0.898, height=31, width=500)
        self.Label_Out.configure(background="#004240", font="-family {Fixedsys} -size 12 -weight bold", foreground="#b3fffd", text="")

        self.Label_Player = tk.Label(window)
        self.Label_Player.place(relx=0.235, rely=0.176, height=31, width=337)
        self.Label_Player.configure(background="#5d5d5d", font="-family {Fixedsys} -size 9", foreground="#ffffff", text=f"It's your turn player {game.player}!")

# main
if __name__ == '__main__':
    game = tc.TicTacToe()
    window = tk.Tk()
    MainApplication(window).place()
    window.mainloop()