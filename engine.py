from tkinter import *


#Logic for chessboard square
class Square:
    
    def __init__(self, root, row, col, color, window, update_position):
        
        self.root = root
        self.window = window
        self.row = row
        self.col = col
        self.visited = False
        self.color = color 
        self.update_position = update_position
        self.button = Button(self.root, width=8, height=4, bg=self.color, bd = 1,
                            activebackground= "#8CFF53", command=self.click_event) 
        self.button.grid(row=self.row, column=self.col, sticky="nesw")

    #Update square when clicked
    def click_event(self):
        self.color =  "#8CFF53"
        self.visited = True
        self.button.configure(text=str(self.window.count), bg=self.color)
        self.update_position((self.row, self.col)) #Callback, passing coordinates when clicked


#Chessboard functions and game logic
class Chessboard:
    
    def __init__(self, root):

        self.root = root
        self.board = [[None for _ in range(8)]for _ in range(8)]
        self.moves = [(-1,-2),(-1,2),(1,2),(1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

    def create_board(self, window):
        for row in range(8):
            for col in range(8):
                if row % 2 == col % 2:
                    color = "white"
                else:
                    color = "#b4b4b4"
                self.board[row][col] = Square(self.root, row, col, color, window, window.handle_click_event)
        
    #Calulate valid moves. Returns a list of valid coordinates 
    def valid_moves(self, position):
        valid_moves = []
        for move in self.moves:
            new_move = (position[0] + move[0], position[1] + move[1])
            if 0 <= new_move[0] < 8 and 0 <= new_move[1] < 8 and not self.board[new_move[0]][new_move[1]].visited:
                valid_moves.append(new_move)

        return valid_moves

    #Enable squares in valid moves
    def get_knights_move(self, position):
        valid_moves = self.valid_moves(position)
        for (row, col) in valid_moves:
            self.board[row][col].button.configure(state = "normal")

    
    def disable_board(self):
        for row in range(8):
            for col in range(8):
                self.board[row][col].button.configure(state="disabled")


    #Calculate knights longest path. Returns a list of positions in order of the path
    def get_longest_route(self, position, route):

        route.append(position)
        self.board[position[0]][position[1]].visited = True

        if len(route) == 64:
            return route

        valid_moves = self.valid_moves(position)
        valid_moves.sort(key=lambda move: len(self.valid_moves(move))) #Sort valid moves based on Warnsdorff's rule 

        minimum_move = valid_moves[0]  #Warnsdorff's rule                        
        longest_route= self.get_longest_route(minimum_move, route)
        return longest_route