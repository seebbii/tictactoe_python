import random
class TicTacToe:

    def __init__(self):
        self.field = [["_","_","_"], ["_","_","_"], ["_","_","_"]]
        self.player = self.choose_player()
        self.winning_row = ""

    # fill field with field_content
    def set_field(self, field_content):
        field_content_list = list(field_content)
        self.field[0] = [field_content_list[0], field_content_list[1], field_content_list[2]]
        self.field[1] = [field_content_list[3], field_content_list[4], field_content_list[5]]
        self.field[2] = [field_content_list[6], field_content_list[7], field_content_list[8]]

    def choose_player(self):
        players = ("X", "O")
        random.seed()
        return random.choice(players)


    # toggles player from X <-> O
    def toggle_player(self):
        if self.player == "X":
            self.player = "O"
        elif self.player == "O":
            self.player = "X"

    def get_player(self):
        return self.player

    # print formatted field to console
    def print_field(self):
        print("---------")
        print("| " + " ".join(self.field[0]) + " |")
        print("| " + " ".join(self.field[1]) + " |")
        print("| " + " ".join(self.field[2]) + " |")
        print("---------")

    def result(self):
        result = "The game ended in a draw"
        counter = 0
        x_count = 0
        o_count = 0
        # game not finished
        if any('_' in row for row in self.field):
            result = "The game is not finished"
        # across the top
        if self.field[0][0] == self.field[0][1] == self.field[0][2] != '_':
            result = self.field[0][0] + " has won"
            self.winning_row = "TOP"
            counter += 1
        # across the middle
        if self.field[1][0] == self.field[1][1] == self.field[1][2] != '_':
            result = self.field[1][0] + " has won"
            self.winning_row = "MIDDLE"
            counter += 1
        # across the bottom
        if self.field[2][0] == self.field[2][1] == self.field[2][2] != '_':
            result = self.field[2][0] + " has won"
            self.winning_row = "BOTTOM"
            counter += 1
        # down the left side
        if self.field[0][0] == self.field[1][0] == self.field[2][0] != '_':
            result = self.field[0][0] + " has won"
            self.winning_row = "DOWN_L"
            counter += 1
        # down the middle
        if self.field[0][1] == self.field[1][1] == self.field[2][1] != '_':
            result = self.field[0][1] + " has won"
            self.winning_row = "DOWN_M"
            counter += 1
        # down the right side
        if self.field[0][2] == self.field[1][2] == self.field[2][2] != '_':
            result = self.field[0][2] + " has won"
            self.winning_row = "DOWN_R"
            counter += 1
        # diagonal upper left to lower right
        if self.field[0][0] == self.field[1][1] == self.field[2][2] != '_':
            result = self.field[0][0] + " has won"
            self.winning_row = "DIAG_UL_LR"
            counter += 1
        # diagonal lower left to upper right
        if self.field[2][0] == self.field[1][1] == self.field[0][2] != '_':
            result = self.field[2][0] + " has won"
            self.winning_row = "DIAG_LL_UR"
            counter += 1
        # Error bei 2 vollen Reihen oder bei zu vielen Xs/Os
        for row in self.field:
            for item in row:
                if item == "X":
                    x_count += 1
                elif item == "O":
                    o_count += 1
        if counter > 1 or abs(x_count - o_count) > 1:  # or x_count - o_count < -1:
            result = "Error"
        return result

    def is_coordinate(self, coordinate):
        coord_list = list(coordinate)
        if len(coord_list) != 3 or coord_list[1] != " " or not coord_list[0].isnumeric() or not coord_list[2].isnumeric():
            return False, "Please input a number"
        elif int(coord_list[0]) > 3 or int(coord_list[2]) > 3:
            return False, "Please input coordinates between 1 and 3"
        elif self.field[int(coord_list[0]) - 1][int(coord_list[2]) - 1] != "_":
            return False, "This is not an empty cell - please choose another one"
        else:
            return True

    def move(self, coordinates, player):
        y_coords = int(coordinates.split(" ")[0]) - 1
        x_coords = int(coordinates.split(" ")[1]) - 1
        self.field[y_coords][x_coords] = player

    def play(self):
        self.print_field()
        print("It's your turn player",self.get_player(),": ", end="")
        coordinates = input()
        if self.is_coordinate(coordinates) == True:
            self.move(coordinates, self.get_player())
            self.toggle_player()
            if self.result() == "The game is not finished":
                self.play()
            else:
                print(self.result())
        else:
            print(self.is_coordinate(coordinates)[1])
            self.play()

if __name__ == '__main__':
    t = TicTacToe()
    t.play()