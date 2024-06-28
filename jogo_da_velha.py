import tkinter # import GUI (Graphical User Interface)


def set_tile(row, column):
    global current_player

    if board[row][column]["text"] != "":
        return

    board[row][column]["text"] = current_player #mark the board

    if current_player == playerO: #switch player
        current_player = playerX
    else:
        current_player = playerO

    label["text"] = "Vez do " + current_player

def new_game():
    pass

# Game Setup
playerX = "X"
playerO = "O"
current_player = playerX
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# Color of the python logo
color_blue = "#4584b6"
color_yellow = "ffde57"
color_gray = "#808080"
color_light_gray = "646464"

# window setup
window = tkinter.Tk() #create de game window
window.title("Jogo da Velha")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="Rodada do "+current_player,
                      font=("Consolas", 20),
                      background=color_gray, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

#Set the grip and the buttons
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=color_gray, foreground=color_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

#Create the restart button
restart_button = tkinter.Button(frame, text="Reiniciar", background=color_gray, font=("Consolas", 20, "bold"),
                                foreground="white", command=new_game)
restart_button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

#Center the window
window.update()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window.winfo_reqwidth()) // 2
y = (screen_height - window.winfo_reqheight()) // 2
window.geometry(f"+{x}+{y}")

window.mainloop()
