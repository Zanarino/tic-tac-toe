import tkinter # import GUI (Graphical User Interface)


def set_tile(row, column):
    global current_player

    if (game_over):
        return

    if board[row][column]["text"] != "":
        return

    board[row][column]["text"] = current_player #mark the board

    if current_player == playerO: #switch player
        current_player = playerX
    else:
        current_player = playerO

    label["text"] = current_player+" 's turn =D"

    #Function to check the winner
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    #horizontally, check 3 rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return

    #vertically, check 3 colmuns
    for column in range (3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return

    #diagonally check
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return

    #anti-diagonally
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_gray)
        board[1][1].config(foreground=color_yellow, background=color_light_gray)
        board[2][0].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return

    #tie
    if (turns == 9):
        game_over = True
        label.config(text="Tie!! =/", foreground=color_yellow)

def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label.config(text=current_player+"'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)


# Game Setup
playerX = "X"
playerO = "O"
current_player = playerX
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# Color of the python logo
color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#808080"
color_light_gray = "#646464"

turns = 0
game_over = False

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
