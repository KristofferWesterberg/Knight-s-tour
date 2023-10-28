from engine import Chessboard
from tkinter import *
from tkinter import messagebox
import time

#Display game GUI
class Window:
    def __init__(self, root, rule):
        self.root = root
        self.chessboard = Chessboard(root)
        self.rule = rule
        self.count = 1
        self.root.resizable(False,False)
        self.chessboard.create_board(self)
    
    # Update GUI for knights move
    def display_knights_move(self, position):
        self.chessboard.disable_board()
        self.chessboard.get_knights_move(position)
        self.count += 1
        if not self.chessboard.valid_moves(position):
            steps = self.count - 1    #Correct count for display
            messagebox.showinfo("Congratulations", f"You completed {steps} steps!") #Display game over

    #Update GUI for longest route
    def display_longest_route(self, position):
        longest_route = self.chessboard.get_longest_route(position, [])
        self.chessboard.disable_board()
        for move in longest_route:
            self.chessboard.board[move[0]][move[1]].button.configure(text=str(self.count), bg="#8CFF53")
            self.count += 1
            self.root.update()
            time.sleep(0.3)

    # Display the choosen game when a square is clicked
    def handle_click_event(self, position):    
        if self.rule == "Create Route":
            self.display_knights_move(position)
        else:
            self.display_longest_route(position)



#GUI game menu
class Menu: 

    def __init__(self): 

        self.root = Tk()
        self.root.title("Knight's Tour")
        self.root.geometry("600x600")
        self.root.configure(bg="white")
        self.root.resizable(False,False)
        self.root.iconphoto(True, PhotoImage(file="icon.png")) 

        self.main_label = Label(self.root, text = "Welcome", font = ("Arial", 20, "bold"), bg="white")
        self.main_label.pack(pady=30)

        self.create_button("Create Route", 70 ,120)
        self.create_button("Longest Route", 370, 120)
        
        self.image = PhotoImage(file="picture.gif")
        self.image_label = Label(self.root, image=self.image)
        self.image_label.pack(padx=150, pady=140)

    # Create menu buttons to choose a game
    def create_button(self, game_name, x, y):
        button_label = Label(self.root, text=game_name, font = ("Arial", 16), bg="white")
        button_label.place(x=x, y=y)

        button = Button(self.root, text = "Click me", font = ("Arial", 12), bg="#D1D1D1", command=lambda game=game_name: self.open_window(game))
        button.place(x= x+25, y=y+40)

    #Create window with choosen game rule
    def open_window(self, game):
        child = Toplevel(self.root)
        if game == "Create Route":
            rule = game
        else:
            rule = game
        return Window(child, rule)
        

    def run(self):
        return self.root.mainloop()

#Run the GUI
menu = Menu()
menu.run()
