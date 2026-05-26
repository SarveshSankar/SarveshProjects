import tkinter as tk
import random

# --- Window setup ---
WIDTH = 500
HEIGHT = 600

root = tk.Tk()
root.title("Fruit Catcher")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="lightblue")
canvas.pack()

# --- Basket (fruit catching device) ---
basket_width = 100
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - 60
basket_speed = 20

basket = canvas.create_rectangle(
    basket_x, basket_y,
    basket_x + basket_width, basket_y + basket_height,
    fill="navy"
)

# --- Fruit settings ---
fruit_radius = 15
fruit_speed = 5
fruits = []

score = 0
lives = 5

score_text = canvas.create_text(10, 10, anchor="nw", text=f"Score: {score}", font=("Arial", 16))
lives_text = canvas.create_text(10, 40, anchor="nw", text=f"Lives: {lives}", font=("Arial", 16))

game_over = False

def spawn_fruit():
    x = random.randint(fruit_radius, WIDTH - fruit_radius)
    y = -fruit_radius
    fruit = canvas.create_oval(
        x - fruit_radius, y - fruit_radius,
        x + fruit_radius, y + fruit_radius,
        fill="red"
    )
    fruits.append(fruit)

def move_fruits():
    global score, lives, game_over

    if game_over:
        return

    to_remove = []

    for fruit in fruits:
        canvas.move(fruit, 0, fruit_speed)
        x1, y1, x2, y2 = canvas.coords(fruit)

        # Check if caught
        bx1, by1, bx2, by2 = canvas.coords(basket)
        if y2 >= by1 and x2 >= bx1 and x1 <= bx2:
            score += 1
            canvas.itemconfig(score_text, text=f"Score: {score}")
            to_remove.append(fruit)
            continue

        # Missed fruit
        if y2 > HEIGHT:
            lives -= 1
            canvas.itemconfig(lives_text, text=f"Lives: {lives}")
            to_remove.append(fruit)

            if lives <= 0:
                game_over = True
                canvas.create_text(
                    WIDTH // 2, HEIGHT // 2,
                    text="GAME OVER",
                    font=("Arial", 40),
                    fill="darkred"
                )

    # Remove fruits
    for fruit in to_remove:
        canvas.delete(fruit)
        fruits.remove(fruit)

    # Spawn new fruits occasionally
    if random.random() < 0.03:
        spawn_fruit()

    root.after(30, move_fruits)

def move_left(event):
    if not game_over:
        canvas.move(basket, -basket_speed, 0)

def move_right(event):
    if not game_over:
        canvas.move(basket, basket_speed, 0)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

spawn_fruit()
move_fruits()

root.mainloop()