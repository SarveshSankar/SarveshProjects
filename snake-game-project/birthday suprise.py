import tkinter as tk
import random
import time
import threading

# -----------------------------
# Balloon Animation
# -----------------------------
def float_balloons(canvas):
    colors = ["red", "blue", "yellow", "green", "purple", "orange", "pink"]
    balloons = []

    # Create balloons
    for _ in range(10):
        x = random.randint(20, 380)
        y = 350
        size = random.randint(25, 40)
        color = random.choice(colors)
        balloon = canvas.create_oval(x, y, x+size, y+size*1.2, fill=color, outline="")
        balloons.append((balloon, x, y, size))

    # Animate upward
    for _ in range(200):
        for i, (balloon, x, y, size) in enumerate(balloons):
            canvas.move(balloon, 0, -2)
        canvas.update()
        time.sleep(0.03)


# -----------------------------
# Confetti Animation
# -----------------------------
def confetti_burst(canvas):
    colors = ["red", "yellow", "blue", "green", "pink", "orange", "purple"]
    for _ in range(150):
        x = random.randint(0, 500)
        y = random.randint(0, 300)
        size = random.randint(5, 10)
        canvas.create_rectangle(x, y, x+size, y+size, fill=random.choice(colors), outline="")
        canvas.update()
        time.sleep(0.01)


# -----------------------------
# Surprise Window
# -----------------------------
def launch_surprise():
    surprise = tk.Toplevel()
    surprise.title("🎉 Surprise!")
    surprise.geometry("500x450")
    surprise.config(bg="black")

    title = tk.Label(
        surprise,
        text="🎉 HAPPY BIRTHDAY AMMA!!! 🎉",
        font=("Arial", 26, "bold"),
        fg="gold",
        bg="black"
    )
    title.pack(pady=10)

    canvas = tk.Canvas(surprise, width=500, height=350, bg="black", highlightthickness=0)
    canvas.pack()

    # Run animations in parallel
    threading.Thread(target=lambda: float_balloons(canvas)).start()
    threading.Thread(target=lambda: confetti_burst(canvas)).start()


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("Birthday Surprise")
root.geometry("400x350")

label = tk.Label(
    root,
    text="🎂 Happy Birthday! 🎂",
    font=("Arial", 24, "bold")
)
label.pack(pady=20)

cake = tk.Label(
    root,
    text="🎂🎂🎂",
    font=("Arial", 40)
)
cake.pack()

button = tk.Button(
    root,
    text="PRESS FOR SURPRISE",
    font=("Arial", 16, "bold"),
    bg="purple",
    fg="white",
    command=launch_surprise
)
button.pack(pady=30)

root.mainloop()