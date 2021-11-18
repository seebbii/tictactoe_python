# Reihenfolge der Buttons
# Button1 Button2 Button3
# Button4 Button5 Button6
# Button7 Button8 Button9
import os
import tictactoe_console as tc
import tkinter as tk

def button_clicked_restart():
    window.destroy()
    os.startfile("TicTacToe_GUI.pyw")

class MainApplication(tk.Frame):
    def change_button_text(self, button, text):
        if button == 1:
            self.Button1.configure(text=text)
        elif button == 2:
            self.Button2.configure(text=text)
        elif button == 3:
            self.Button3.configure(text=text)
        elif button == 4:
            self.Button4.configure(text=text)
        elif button == 5:
            self.Button5.configure(text=text)
        elif button == 6:
            self.Button6.configure(text=text)
        elif button == 7:
            self.Button7.configure(text=text)
        elif button == 8:
            self.Button8.configure(text=text)
        elif button == 9:
            self.Button9.configure(text=text)

    def change_playerlabel_text(self, text):
        self.Label_Player.configure(text=text)

    def change_outlabel_text(self, text):
        self.Label_Out.configure(text=text)

    def freeze(self):
        self.Button1["state"] = tk.DISABLED
        self.Button2["state"] = tk.DISABLED
        self.Button3["state"] = tk.DISABLED
        self.Button4["state"] = tk.DISABLED
        self.Button5["state"] = tk.DISABLED
        self.Button6["state"] = tk.DISABLED
        self.Button7["state"] = tk.DISABLED
        self.Button8["state"] = tk.DISABLED
        self.Button9["state"] = tk.DISABLED

    def highlight_winning_row(self):
        if game.winning_row == "TOP":
            self.Button1["background"] = "gold"
            self.Button2["background"] = "gold"
            self.Button3["background"] = "gold"
        elif game.winning_row == "MIDDLE":
            self.Button4["background"] = "gold"
            self.Button5["background"] = "gold"
            self.Button6["background"] = "gold"
        elif game.winning_row == "BOTTOM":
            self.Button7["background"] = "gold"
            self.Button8["background"] = "gold"
            self.Button9["background"] = "gold"
        elif game.winning_row == "DOWN_L":
            self.Button1["background"] = "gold"
            self.Button4["background"] = "gold"
            self.Button7["background"] = "gold"
        elif game.winning_row == "DOWN_M":
            self.Button2["background"] = "gold"
            self.Button5["background"] = "gold"
            self.Button8["background"] = "gold"
        elif game.winning_row == "DOWN_R":
            self.Button3["background"] = "gold"
            self.Button6["background"] = "gold"
            self.Button9["background"] = "gold"
        elif game.winning_row == "DIAG_LL_UR":
            self.Button7["background"] = "gold"
            self.Button5["background"] = "gold"
            self.Button3["background"] = "gold"
        elif game.winning_row == "DIAG_UL_LR":
            self.Button1["background"] = "gold"
            self.Button5["background"] = "gold"
            self.Button9["background"] = "gold"

    def update_label_player(self):
        self.Label_Player.configure(text=("It's your turn player " + game.player + "!"))

    def button_clicked_1(self):
        self.button_clicked(1)

    # Feld 1 2
    def button_clicked_2(self):
        self.button_clicked(2)

    # Feld 1 3
    def button_clicked_3(self):
        self.button_clicked(3)

    # Feld 2 1
    def button_clicked_4(self):
        self.button_clicked(4)

    # Feld 2 2
    def button_clicked_5(self):
        self.button_clicked(5)

    # Feld 2 3
    def button_clicked_6(self):
        self.button_clicked(6)

    # Feld 3 1
    def button_clicked_7(self):
        self.button_clicked(7)

    # Feld 3 2
    def button_clicked_8(self):
        self.button_clicked(8)

    # Feld 3 3
    def button_clicked_9(self):
        self.button_clicked(9)

    def button_clicked(self, button):
        coords = ""
        if button == 1:
            coords = "1 1"
        elif button == 2:
            coords = "1 2"
        elif button == 3:
            coords = "1 3"
        elif button == 4:
            coords = "2 1"
        elif button == 5:
            coords = "2 2"
        elif button == 6:
            coords = "2 3"
        elif button == 7:
            coords = "3 1"
        elif button == 8:
            coords = "3 2"
        elif button == 9:
            coords = "3 3"
        if game.is_coordinate(coords):
            game.move(coords, game.player)
            self.change_button_text(button, game.player)
            game.toggle_player()
            self.update_label_player()
            if game.result() != "The game is not finished":
                self.freeze()
                self.highlight_winning_row()
                self.change_outlabel_text(game.result())
        else:
            self.change_outlabel_text(game.is_coordinate(coords)[1])

    # Restart Button

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
        window.resizable(1, 1)
        window.title("TicTacToe")
        window.configure(background="#004240")

        # configure widgets
        self.Button1 = tk.Button(window)
        self.Button1.place(relx=0.235, rely=0.234, height=114, width=117)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(cursor="fleur")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Eras Light ITC} -size 18 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(cursor="hand2")
        self.Button1.configure(text="")
        self.Button1.configure(command=self.button_clicked_1)

        self.Button2 = tk.Button(window)
        self.Button2.place(relx=0.408, rely=0.234, height=114, width=117)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Eras Light ITC} -size 18 -weight bold")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(cursor="hand2")
        self.Button2.configure(text="")
        self.Button2.configure(command=self.button_clicked_2)

        self.Button3 = tk.Button(window)
        self.Button3.place(relx=0.58, rely=0.234, height=114, width=117)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(cursor="fleur")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Eras Light ITC} -size 18 -weight bold")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(cursor="hand2")
        self.Button3.configure(text="")
        self.Button3.configure(command=self.button_clicked_3)

        self.Button4 = tk.Button(window)
        self.Button4.place(relx=0.235, rely=0.449, height=114, width=117)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font="-family {Eras Light ITC} -size 18 -weight bold")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(cursor="hand2")
        self.Button4.configure(text="")
        self.Button4.configure(command=self.button_clicked_4)

        self.Button5 = tk.Button(window)
        self.Button5.place(relx=0.408, rely=0.449, height=114, width=117)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(cursor="fleur")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font="-family {Eras Light ITC} -size 18 -weight bold")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(cursor="hand2")
        self.Button5.configure(text="")
        self.Button5.configure(command=self.button_clicked_5)

        self.Button6 = tk.Button(window)
        self.Button6.place(relx=0.58, rely=0.449, height=114, width=117)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(font="-family {Eras Light ITC} -size 18 -weight bold")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(cursor="hand2")
        self.Button6.configure(text="")
        self.Button6.configure(command=self.button_clicked_6)

        self.Button7 = tk.Button(window)
        self.Button7.place(relx=0.235, rely=0.664, height=114, width=117)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(cursor="fleur")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(font="-family {Eras Light ITC} -size 18 -weight bold")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(cursor="hand2")
        self.Button7.configure(text="")
        self.Button7.configure(command=self.button_clicked_7)

        self.Button8 = tk.Button(window)
        self.Button8.place(relx=0.408, rely=0.664, height=114, width=117)
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(cursor="fleur")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(font="-family {Eras Light ITC} -size 18 -weight bold")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(cursor="hand2")
        self.Button8.configure(text="")
        self.Button8.configure(command=self.button_clicked_8)

        self.Button9 = tk.Button(window)
        self.Button9.place(relx=0.58, rely=0.664, height=114, width=117)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(font="-family {Eras Light ITC} -size 18 -weight bold")
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(cursor="hand2")
        self.Button9.configure(text="")
        self.Button9.configure(command=self.button_clicked_9)

        self.Button_Restart = tk.Button(window)
        self.Button_Restart.place(relx=0.768, rely=0.176, height=44, width=77)
        self.Button_Restart.configure(activebackground="#ececec")
        self.Button_Restart.configure(activeforeground="#000000")
        self.Button_Restart.configure(background="#d9d9d9")
        self.Button_Restart.configure(disabledforeground="#a3a3a3")
        self.Button_Restart.configure(font="-family {Fixedsys} -size 9")
        self.Button_Restart.configure(foreground="#000000")
        self.Button_Restart.configure(highlightbackground="#d9d9d9")
        self.Button_Restart.configure(highlightcolor="black")
        self.Button_Restart.configure(pady="0")
        self.Button_Restart.configure(text='''Restart''')
        self.Button_Restart.configure(command=button_clicked_restart)

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
