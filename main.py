# Importing necessary modules
import tkinter as tk
from tkinter.ttk import Button
import time

# Initializing variables
button_list = [[0,0,0],
               [0,0,0],
               [0,0,0]]
button_data = [[0,0,0],
               [0,0,0],
               [0,0,0]]
player_turn = 0            

# Creating the main Tkinter window
root = tk.Tk()
canvas = tk.Canvas(root, bg = 'white',height = 900, width= 1400)
canvas.pack()
player1_score = 0
player2_score = 0


# Function to check the game logic for a winner or draw
def game_logic():
    global player1_score , player2_score
    winner = None
    winner_string = None
    
    # Checking rows and columns for a winner
    for rc in range(3):
        if button_data[rc][0] == button_data[rc][1] == button_data[rc][2] != 0:
            winner = button_data[rc][0]
            break
        elif button_data[0][rc] == button_data[1][rc] == button_data[2][rc] != 0:
            winner = button_data[0][rc]
            break
    
    # Checking diagonals for a winner
    if button_data[0][0] == button_data[1][1] == button_data[2][2] != 0:
        winner = button_data[0][0]
    elif button_data[0][2] == button_data[1][1] == button_data[2][0]:
        winner = button_data[0][2]
    
    # Determining the winner or draw
    if winner == 'O':
        winner_string = player1_name + ' is the winner'
        player1_score += 1
    elif winner == 'X':
        winner_string = player2_name + ' is the winner'
        player2_score += 1
    elif player_turn == 9:
        winner_string = "It's a draw."
    
    # Displaying the winner or draw message
    if winner_string:
        score_board(winner_string)

# Function to quit the game
def quit_game():
    if player1_score > player2_score:
        winner_string = player1_name + ' is the winner'
    elif player1_score < player2_score:
        winner_string = player2_name + ' is the winner'
    else:
        winner_string = 'It is a draw.'
    
    # Displaying final winner or draw message
    label = tk.Label(root, bg='light blue', fg='black', text=winner_string, font=('brown sugar', 30, 'bold'))
    label.place(relx=0, rely=0, relheight=1, relwidth=1)
    score_frame.destroy()
    canvas.destroy()
    time.sleep(3)

# Function to replay the game
def replay_game():
    global player_turn
    score_frame.destroy()
    for i in range(3):
        for j in range(3):
            button_data[i][j] = 0
            button_list[i][j] = 0 
    player_turn = 0
    setup()

# Function to display the score board
def score_board(winner_string):
    global score_frame
    score_frame = tk.Toplevel(root, height=200, width=400)

    label = tk.Label(score_frame, bg='light blue', fg='black', text=winner_string, font=('brown sugar', 30, 'bold'))
    label.place(relx=0, rely=0, relheight=0.6, relwidth=1)

    replay_btn = tk.Button(score_frame, fg='black', text='Replay', font=('chalkboard', 20), command=replay_game)
    replay_btn.place(relheight=0.4, relwidth=0.5, relx=0, rely=0.6)

    quit_btn = tk.Button(score_frame, fg='black', text='Quit', font=('chalkboard', 20), command=quit_game)
    quit_btn.place(relheight=0.4, relwidth=0.5, relx=0.5, rely=0.6)

    win1.config(text= player1_name + ' score: ' + str(player1_score))
    win2.config(text= player2_name + ' score: ' + str(player2_score))

# Function to handle button click and change text on button
def change_text(row, col):
    global player_turn
    if player_turn % 2 == 0:
        textt = 'O'
    else:
        textt = 'X'
    if button_data[row][col] == 0:
        button_data[row][col] = textt
        button_list[row][col].config(text=textt)
        player_turn += 1
    if player_turn >= 5:
        game_logic()

# Function to set up the game interface
def setup():
    global button_frame, win1, win2, player1_score
    frame = tk.Frame(canvas, bg='#303030')
    frame.place(relx=0, rely=0, relheight=1, relwidth=1)
    welcome_text = tk.Label(canvas, bg='white', fg='black', font=('brown sugar', 40), text='Tic-Tac-Toe')
    welcome_text.place(relx=0.3, rely=0.1, relwidth=0.4)
    button_frame = tk.Frame(canvas, bg='white')
    button_frame.place(relx=(1 - 500 / 1400) / 2, rely=(1 - 500 / 900) / 2, relheight=500 / 900, relwidth=500 / 1400)

    for r in range(3):
        for c in range(3):
            button = tk.Button(button_frame, bg='blue', fg='black', font=('comic', 30),
                               command=lambda row=r, col=c: change_text(row, col))
            button.place(relwidth=1 / 3, relheight=1 / 3, relx=c / 3, rely=r / 3)
            button_list[r][c] = button
    
    win1 = tk.Label(canvas, bg='light blue', fg='black', text=player1_name + ' score: ' + str(player1_score),
                    font=('chalkboard', 30))
    win1.place(relx=0.05, rely=0.4, relheight=1 / 3 - 0.25, relwidth=0.2)

    win2 = tk.Label(canvas, bg='light blue', fg='black', text=player2_name + ' score: ' + str(player2_score),
                    font=('chalkboard', 30))
    win2.place(relx=0.8, rely=0.4, relheight=1 / 3 - 0.25, relwidth=0.2)

# Function to set up player names and start the game
def presetup():
    global player1_name, player2_name
    player1_name = entry_1.get()
    player2_name = entry_2.get()
    setup()

# Function to display welcome screen and get player names
def welcome():
    global entry_1, entry_2
    welcome_text = tk.Label(canvas, bg='white', fg='black', font=('brown sugar', 40), text='Tic-Tac-Toe')
    welcome_text.place(relx=0.3, rely=0.1, relwidth=0.4)
    label_1 = tk.Label(canvas, bg='white', fg='black', font=('chalkboard', 24), text='Player 1:')
    label_2 = tk.Label(canvas, bg='white', fg='black', font=('chalkboard', 24), text='Player 2:')

    entry_1 = tk.Entry(canvas, bg='white', fg='black', font=('chalkboard', 20), bd=2)
    entry_2 = tk.Entry(canvas, bg='white', fg='black', font=('chalkboard', 20), bd=2)

    label_1.place(relx=0.2, rely=0.25, relwidth=0.25)
    label_2.place(relx=0.2, rely=0.5, relwidth=0.25)

    entry_1.place(relx=0.5, rely=0.25, relwidth=0.4)
    entry_2.place(relx=0.5, rely=0.5, relwidth=0.4)
    start_button = tk.Button(canvas, bg='white', fg='black', text='Start the game', font=('chalkboard', 16),
                             command=presetup)
    start_button.place(relx=0.45, rely=0.65, relheight=0.06, relwidth=0.1)

# Starting the welcome screen
welcome()
root.mainloop()
