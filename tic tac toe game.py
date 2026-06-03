import tkinter as tk
import random

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.resizable(False, False)

win_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

buttons = []
game_over = False


def check_winner():
    global game_over

    for combo in win_combinations:
        a, b, c = combo

        if buttons[a]["text"] != "" and \
           buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"]:

            winner = buttons[a]["text"]
            status_label.config(text=f"🎉 Player {winner} Wins!")

            for btn in buttons:
                btn.config(state="disabled")

            game_over = True
            return True

    # Draw Check
    if all(btn["text"] != "" for btn in buttons):
        status_label.config(text="🤝 Match Draw!")

        for btn in buttons:
            btn.config(state="disabled")

        game_over = True
        return True

    return False


def computer_move():
    if game_over:
        return

    empty_cells = [i for i in range(9) if buttons[i]["text"] == ""]

    if empty_cells:
        move = random.choice(empty_cells)
        buttons[move].config(text="O")

        check_winner()

        if not game_over:
            status_label.config(text="Player X's Turn")


def button_click(index):
    global game_over

    if game_over:
        return

    if buttons[index]["text"] == "":
        buttons[index].config(text="X")

        if not check_winner():
            status_label.config(text="Computer's Turn")
            root.after(500, computer_move)


def reset_game():
    global game_over

    game_over = False

    for btn in buttons:
        btn.config(text="", state="normal")

    status_label.config(text="Player X's Turn")


# Create Board
for i in range(9):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 25, "bold"),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )

    btn.grid(row=i // 3, column=i % 3)
    buttons.append(btn)

# Status Label
status_label = tk.Label(
    root,
    text="Player X's Turn",
    font=("Arial", 16)
)
status_label.grid(row=3, column=0, columnspan=3, pady=10)

# New Game Button
reset_btn = tk.Button(
    root,
    text="New Game",
    font=("Arial", 14),
    command=reset_game
)
reset_btn.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()