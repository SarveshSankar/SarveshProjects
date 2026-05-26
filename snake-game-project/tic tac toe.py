import tkinter as tk

root = tk.Tk()
root.title('Tic Tac Toe')

buttons = [[None for _ in range(3)] for _ in range(3)]
current_player = 'X'
game_over = False

def check_winner():
    global game_over
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            game_over = True
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            game_over = True
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        game_over = True
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        game_over = True
        return True
    return False

def button_click(row, col):
    global current_player, game_over
    if not game_over and buttons[row][col]['text'] == '':
        buttons[row][col].config(text=current_player)
        if check_winner():
            print(f"Player {current_player} wins!")
        else:
            current_player = 'O' if current_player == 'X' else 'X'

for i in range(3):
    for j in range(3):
        button = tk.Button(root, text='', width=5, height=2,
                          command=lambda r=i, c=j: button_click(r, c))
        button.grid(row=i, column=j)
        buttons[i][j] = button

root.mainloop()