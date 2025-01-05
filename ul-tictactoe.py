
class TicTacToe:
    def __init__(self):
        self.smaller_grids = []
        for _ in range(9):
            self.smaller_grids.append([0,0,0,0,0,0,0,0,0])
        self.larger_grid = [0, 1, 1, 0, 0, 0, 0, 0, 0]
        
        self.playable_larger_cell = 0
        self.last_played_larger_cell = 0
        self.moves = 1
        self.freewill = False

        self.played_larger_cell = 0
        self.played_smaller_cell = 0
    
    def check_win(self, grid):
        for i in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [3, 4, 6]]:
            if grid[i[0]] == grid[i[1]] == grid[i[2]] == 1:
                return 1
            elif grid[i[0]] == grid[i[1]] == grid[i[2]] == 2:
                return 2
        return 0
    
    def win_mgmt(self):
        win = self.check_win(self.smaller_grids[self.last_played_larger_cell])

        if win:
            self.larger_grid[self.last_played_larger_cell] = win
            overall_win = self.check_win(self.larger_grid)
            if overall_win:
                print(f"Player {overall_win} won the match!")
                return True

        self.last_played_larger_cell = self.playable_larger_cell
    
    def move(self, larger_cell, smaller_cell):
        if self.moves % 2 == 0:
            self.smaller_grids[larger_cell][smaller_cell] = 2
        else:
            self.smaller_grids[larger_cell][smaller_cell] = 1

        self.played_larger_cell = larger_cell
        self.played_smaller_cell = smaller_cell
        self.moves += 1
        self.playable_larger_cell = smaller_cell
        if self.larger_grid[self.playable_larger_cell] != 0:
            self.freewill = True
        else:
            self.freewill = False
    
    def turn(self):
        while True:
            larger_cell = self.playable_larger_cell
            if self.moves == 1:
                larger_cell = int(input("Which larger cell?: "))
            elif self.freewill:
                print("In this turn you can choose the larger cell.")
                larger_cell = int(input("Which larger cell?: "))
            
            if self.larger_grid[larger_cell] == 0:
                print(f"You will be playing in larger cell {larger_cell}")
                smaller_cell = int(input("Which smaller cell?: "))
            
                if self.smaller_grids[larger_cell][smaller_cell] == 0:
                    self.move(larger_cell, smaller_cell)
                    break
                else:
                    print("Unplayable cell. Try Again.")
            else:
                print("Unplayable cell. Try Again.")
    
    def print_game(self):
        symbols = (" ", "◯", "x")
        for i in range(0, 7, 3):
            #I know its huge, just like my big brain who did this.
            print(f"{symbols[self.smaller_grids[i][0]]}|{symbols[self.smaller_grids[i][1]]}|{symbols[self.smaller_grids[i][2]]} ", end="")
            print(f"{symbols[self.smaller_grids[i+1][0]]}|{symbols[self.smaller_grids[i+1][1]]}|{symbols[self.smaller_grids[i+1][2]]} ", end="")
            print(f"{symbols[self.smaller_grids[i+2][0]]}|{symbols[self.smaller_grids[i+2][1]]}|{symbols[self.smaller_grids[i+2][2]]} ")
            
            print(f"{symbols[self.smaller_grids[i][3]]}|{symbols[self.smaller_grids[i][4]]}|{symbols[self.smaller_grids[i][5]]} ", end="")
            print(f"{symbols[self.smaller_grids[i+1][3]]}|{symbols[self.smaller_grids[i+1][4]]}|{symbols[self.smaller_grids[i+1][5]]} ", end="")
            print(f"{symbols[self.smaller_grids[i+2][3]]}|{symbols[self.smaller_grids[i+2][4]]}|{symbols[self.smaller_grids[i+2][5]]} ")

            print(f"{symbols[self.smaller_grids[i][6]]}|{symbols[self.smaller_grids[i][7]]}|{symbols[self.smaller_grids[i][8]]} ", end="")
            print(f"{symbols[self.smaller_grids[i+1][6]]}|{symbols[self.smaller_grids[i+1][7]]}|{symbols[self.smaller_grids[i+1][8]]} ", end="")
            print(f"{symbols[self.smaller_grids[i+2][6]]}|{symbols[self.smaller_grids[i+2][7]]}|{symbols[self.smaller_grids[i+2][8]]} ")

            print("-----------------")
    
    def start(self):
        while True:
            self.print_game()
            self.turn()
            win = self.win_mgmt()
            if win:
                break

            if self.moves > 81:
                print("Draw!")
                break

if __name__ == "__main__":
    t = TicTacToe()
    t.start()
