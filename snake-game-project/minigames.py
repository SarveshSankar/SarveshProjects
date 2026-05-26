import tkinter as tk
import random
import time

# =========================
# Main Arcade Application
# =========================

class ArcadeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MiniGames Arcade")
        self.geometry("800x600")
        self.resizable(True, True)

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        # Initialize all game screens
        for F in (MainMenu,
                  ReactionTimeGame,
                  DodgeBlocksGame,
                  WhackAMoleGame,
                  MemoryGame,
                  SnakeGame,
                  TypingGame):
            frame = F(parent=self.container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
        # Set focus to the frame so key bindings work
        frame.focus_set()
        if hasattr(frame, "on_show"):
            frame.on_show()


# =========================
# Main Menu
# =========================

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#222222")
        self.controller = controller

        title = tk.Label(self, text="MiniGames Arcade", font=("Arial", 32, "bold"), fg="white", bg="#222222")
        title.pack(pady=40)

        btn_cfg = {"font": ("Arial", 16), "width": 25, "bg": "#444444", "fg": "white", "bd": 0, "highlightthickness": 0}

        games = [
            ("Reaction Time Test", "ReactionTimeGame"),
            ("Dodge the Blocks", "DodgeBlocksGame"),
            ("Whack-A-Mole", "WhackAMoleGame"),
            ("Memory Flip Cards", "MemoryGame"),
            ("Snake Mini", "SnakeGame"),
            ("Typing Speed Challenge", "TypingGame"),
        ]

        for text, frame_name in games:
            b = tk.Button(self, text=text, command=lambda n=frame_name: controller.show_frame(n), **btn_cfg)
            b.pack(pady=5)

        quit_btn = tk.Button(self, text="Quit", command=controller.destroy, **btn_cfg)
        quit_btn.pack(pady=20)


# =========================
# Reaction Time Game
# =========================

class ReactionTimeGame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="black")
        self.controller = controller

        self.label = tk.Label(self, text="Click 'Start' and wait for GREEN", font=("Arial", 20), fg="white", bg="black")
        self.label.pack(pady=40)

        self.canvas = tk.Canvas(self, width=400, height=200, bg="red", highlightthickness=0)
        self.canvas.pack(pady=20)

        self.info = tk.Label(self, text="", font=("Arial", 16), fg="white", bg="black")
        self.info.pack(pady=10)

        btn_frame = tk.Frame(self, bg="black")
        btn_frame.pack(pady=20)

        self.start_btn = tk.Button(btn_frame, text="Start", font=("Arial", 14), command=self.start_game)
        self.start_btn.grid(row=0, column=0, padx=10)

        back_btn = tk.Button(btn_frame, text="Back to Menu", font=("Arial", 14),
                             command=lambda: controller.show_frame("MainMenu"))
        back_btn.grid(row=0, column=1, padx=10)

        self.canvas.bind("<Button-1>", self.on_click)

        self.waiting_for_green = False
        self.green_time = None

    def on_show(self):
        self.reset()

    def reset(self):
        self.canvas.config(bg="red")
        self.info.config(text="")
        self.label.config(text="Click 'Start' and wait for GREEN")
        self.waiting_for_green = False
        self.green_time = None

    def start_game(self):
        self.reset()
        delay = random.randint(2000, 5000)
        self.label.config(text="Wait for GREEN...")
        self.after(delay, self.turn_green)
        self.waiting_for_green = True

    def turn_green(self):
        if self.waiting_for_green:
            self.canvas.config(bg="green")
            self.green_time = time.time()

    def on_click(self, event):
        if not self.waiting_for_green:
            return
        if self.green_time is None:
            self.info.config(text="Too early! You clicked before GREEN.")
            self.waiting_for_green = False
        else:
            rt = (time.time() - self.green_time) * 1000
            self.info.config(text=f"Reaction Time: {rt:.0f} ms")
            self.waiting_for_green = False


# =========================
# Dodge the Blocks Game
# =========================

class DodgeBlocksGame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="black")
        self.controller = controller

        self.canvas = tk.Canvas(self, width=600, height=400, bg="black", highlightthickness=0)
        self.canvas.pack(pady=20)

        info_frame = tk.Frame(self, bg="black")
        info_frame.pack()

        self.score_label = tk.Label(info_frame, text="Score: 0", font=("Arial", 16), fg="white", bg="black")
        self.score_label.grid(row=0, column=0, padx=20)

        back_btn = tk.Button(info_frame, text="Back to Menu", font=("Arial", 14),
                             command=lambda: controller.show_frame("MainMenu"))
        back_btn.grid(row=0, column=1, padx=20)

        self.player = None
        self.blocks = []
        self.score = 0
        self.speed = 4
        self.running = False

        # Key bindings on the FRAME rather than ALL to avoid conflicts
        self.bind("<Left>", self.move_left)
        self.bind("<Right>", self.move_right)

    def on_show(self):
        self.focus_set()
        self.start_game()

    def start_game(self):
        self.canvas.delete("all")
        self.blocks.clear()
        self.score = 0
        self.speed = 4
        self.running = True
        self.score_label.config(text="Score: 0")
        self.player = self.canvas.create_rectangle(280, 360, 320, 390, fill="white")
        self.spawn_block()
        self.game_loop()

    def spawn_block(self):
        x = random.randint(0, 580)
        block = self.canvas.create_rectangle(x, 0, x + 20, 20, fill="red")
        self.blocks.append(block)

    def move_left(self, event):
        if self.running:
            self.canvas.move(self.player, -20, 0)

    def move_right(self, event):
        if self.running:
            self.canvas.move(self.player, 20, 0)

    def game_loop(self):
        if not self.running:
            return

        for block in list(self.blocks):
            self.canvas.move(block, 0, self.speed)
            coords = self.canvas.coords(block)
            if not coords: continue
            
            y1 = coords[1]
            if y1 > 400:
                self.canvas.delete(block)
                self.blocks.remove(block)
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                if self.score % 5 == 0:
                    self.speed += 1
                self.spawn_block()
            else:
                if self.check_collision(block, self.player):
                    self.game_over()
                    return

        if random.random() < 0.02:
            self.spawn_block()

        self.after(30, self.game_loop)

    def check_collision(self, a, b):
        ax1, ay1, ax2, ay2 = self.canvas.coords(a)
        bx1, by1, bx2, by2 = self.canvas.coords(b)
        return not (ax2 < bx1 or ax1 > bx2 or ay2 < by1 or ay1 > by2)

    def game_over(self):
        self.running = False
        self.canvas.create_text(300, 200, text=f"Game Over!\nScore: {self.score}",
                                fill="yellow", font=("Arial", 24, "bold"))


# =========================
# Whack-A-Mole Game
# =========================

class WhackAMoleGame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#225522")
        self.controller = controller

        title = tk.Label(self, text="Whack-A-Mole", font=("Arial", 24, "bold"), bg="#225522", fg="white")
        title.pack(pady=20)

        self.grid_frame = tk.Frame(self, bg="#225522")
        self.grid_frame.pack()

        self.buttons = []
        for r in range(3):
            row = []
            for c in range(3):
                b = tk.Button(self.grid_frame, text="", width=10, height=4,
                              command=lambda pos=(r, c): self.hit(pos))
                b.grid(row=r, column=c, padx=10, pady=10)
                row.append(b)
            self.buttons.append(row)

        info_frame = tk.Frame(self, bg="#225522")
        info_frame.pack(pady=10)

        self.score_label = tk.Label(info_frame, text="Score: 0", font=("Arial", 16), bg="#225522", fg="white")
        self.score_label.grid(row=0, column=0, padx=20)

        back_btn = tk.Button(info_frame, text="Back to Menu", font=("Arial", 14),
                             command=self.back_to_menu)
        back_btn.grid(row=0, column=1, padx=20)

        self.score = 0
        self.current_mole = None
        self.running = False

    def on_show(self):
        self.start_game()

    def start_game(self):
        self.score = 0
        self.score_label.config(text="Score: 0")
        self.running = True
        self.spawn_mole()

    def spawn_mole(self):
        if not self.running:
            return
        if self.current_mole:
            r, c = self.current_mole
            self.buttons[r][c].config(text="")
        
        r = random.randint(0, 2)
        c = random.randint(0, 2)
        self.current_mole = (r, c)
        self.buttons[r][c].config(text="M", fg="brown", font=("Arial", 12, "bold"))
        self.after(800, self.spawn_mole)

    def hit(self, pos):
        if self.running and self.current_mole == pos:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            r, c = pos
            self.buttons[r][c].config(text="")
            self.current_mole = None

    def back_to_menu(self):
        self.running = False
        self.controller.show_frame("MainMenu")


# =========================
# Memory Flip Cards Game
# =========================

class MemoryGame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#333366")
        self.controller = controller

        title = tk.Label(self, text="Memory Flip Cards", font=("Arial", 24, "bold"), bg="#333366", fg="white")
        title.pack(pady=20)

        self.grid_frame = tk.Frame(self, bg="#333366")
        self.grid_frame.pack()

        info_frame = tk.Frame(self, bg="#333366")
        info_frame.pack(pady=10)

        self.moves_label = tk.Label(info_frame, text="Moves: 0", font=("Arial", 16), bg="#333366", fg="white")
        self.moves_label.grid(row=0, column=0, padx=20)

        back_btn = tk.Button(info_frame, text="Back to Menu", font=("Arial", 14),
                             command=lambda: controller.show_frame("MainMenu"))
        back_btn.grid(row=0, column=1, padx=20)

        self.buttons = []
        self.values = []
        self.flipped = []
        self.moves = 0
        self.matched = 0

    def on_show(self):
        self.start_game()

    def start_game(self):
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        self.buttons.clear()
        self.flipped.clear()
        self.moves = 0
        self.matched = 0
        self.moves_label.config(text="Moves: 0")

        vals = list("AABBCCDDEEFFGGHH")
        random.shuffle(vals)
        self.values = [vals[i*4:(i+1)*4] for i in range(4)]

        for r in range(4):
            row = []
            for c in range(4):
                b = tk.Button(self.grid_frame, text="?", width=6, height=3,
                              command=lambda pos=(r, c): self.flip(pos))
                b.grid(row=r, column=c, padx=5, pady=5)
                row.append(b)
            self.buttons.append(row)

    def flip(self, pos):
        r, c = pos
        if len(self.flipped) == 2 or pos in self.flipped:
            return
        self.buttons[r][c].config(text=self.values[r][c])
        self.flipped.append(pos)
        if len(self.flipped) == 2:
            self.after(700, self.check_match)

    def check_match(self):
        (r1, c1), (r2, c2) = self.flipped
        self.moves += 1
        self.moves_label.config(text=f"Moves: {self.moves}")
        
        if self.values[r1][c1] == self.values[r2][c2]:
            self.buttons[r1][c1].config(state="disabled")
            self.buttons[r2][c2].config(state="disabled")
            self.matched += 1
            if self.matched == 8:
                self.game_won()
        else:
            self.buttons[r1][c1].config(text="?")
            self.buttons[r2][c2].config(text="?")
        self.flipped.clear()

    def game_won(self):
        win_label = tk.Label(self, text=f"You Won in {self.moves} moves!", font=("Arial", 20, "bold"),
                             bg="#333366", fg="yellow")
        win_label.pack(pady=10)


# =========================
# Snake Mini Game
# =========================

class SnakeGame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="black")
        self.controller = controller

        self.canvas = tk.Canvas(self, width=400, height=400, bg="black", highlightthickness=0)
        self.canvas.pack(pady=20)

        info_frame = tk.Frame(self, bg="black")
        info_frame.pack()

        self.score_label = tk.Label(info_frame, text="Score: 0", font=("Arial", 16), fg="white", bg="black")
        self.score_label.grid(row=0, column=0, padx=20)

        back_btn = tk.Button(info_frame, text="Back to Menu", font=("Arial", 14),
                             command=self.stop_game)
        back_btn.grid(row=0, column=1, padx=20)

        self.cell_size = 20
        self.direction = "Right"
        self.snake = []
        self.food_pos = None
        self.food = None
        self.score = 0
        self.running = False

        self.bind("<Up>", lambda e: self.set_dir("Up"))
        self.bind("<Down>", lambda e: self.set_dir("Down"))
        self.bind("<Left>", lambda e: self.set_dir("Left"))
        self.bind("<Right>", lambda e: self.set_dir("Right"))

    def on_show(self):
        self.focus_set()
        self.start_game()

    def start_game(self):
        self.canvas.delete("all")
        self.direction = "Right"
        self.snake = [(5, 10), (4, 10), (3, 10)]
        self.score = 0
        self.score_label.config(text="Score: 0")
        self.running = True
        self.draw_snake()
        self.spawn_food()
        self.game_loop()

    def stop_game(self):
        self.running = False
        self.controller.show_frame("MainMenu")

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            x1, y1 = x * self.cell_size, y * self.cell_size
            self.canvas.create_rectangle(x1, y1, x1+self.cell_size, y1+self.cell_size, fill="green", tags="snake")

    def spawn_food(self):
        if self.food: self.canvas.delete(self.food)
        while True:
            fx, fy = random.randint(0, 19), random.randint(0, 19)
            if (fx, fy) not in self.snake: break
        x1, y1 = fx * self.cell_size, fy * self.cell_size
        self.food_pos = (fx, fy)
        self.food = self.canvas.create_oval(x1, y1, x1+self.cell_size, y1+self.cell_size, fill="red")

    def set_dir(self, d):
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if opposites.get(d) != self.direction:
            self.direction = d

    def game_loop(self):
        if not self.running: return
        head_x, head_y = self.snake[0]
        if self.direction == "Up": head_y -= 1
        elif self.direction == "Down": head_y += 1
        elif self.direction == "Left": head_x -= 1
        elif self.direction == "Right": head_x += 1

        if head_x < 0 or head_x > 19 or head_y < 0 or head_y > 19 or (head_x, head_y) in self.snake:
            self.game_over()
            return

        self.snake.insert(0, (head_x, head_y))
        if (head_x, head_y) == self.food_pos:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.spawn_food()
        else:
            self.snake.pop()

        self.draw_snake()
        speed = max(80, 200 - self.score * 5)
        self.after(speed, self.game_loop)

    def game_over(self):
        self.running = False
        self.canvas.create_text(200, 200, text=f"Game Over!\nScore: {self.score}", fill="yellow", font=("Arial", 20, "bold"))


# =========================
# Typing Speed Challenge
# =========================

class TypingGame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#222244")
        self.controller = controller

        title = tk.Label(self, text="Typing Speed Challenge", font=("Arial", 24, "bold"), bg="#222244", fg="white")
        title.pack(pady=20)

        self.word_label = tk.Label(self, text="", font=("Arial", 28), bg="#222244", fg="yellow")
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(self, font=("Arial", 20))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_word)

        info_frame = tk.Frame(self, bg="#222244")
        info_frame.pack(pady=10)

        self.score_label = tk.Label(info_frame, text="Score: 0", font=("Arial", 16), bg="#222244", fg="white")
        self.score_label.grid(row=0, column=0, padx=20)

        self.time_label = tk.Label(info_frame, text="Time: 30", font=("Arial", 16), bg="#222244", fg="white")
        self.time_label.grid(row=0, column=1, padx=20)

        back_btn = tk.Button(info_frame, text="Back to Menu", font=("Arial", 14),
                             command=self.stop_game)
        back_btn.grid(row=0, column=2, padx=20)

        self.words = ["python", "arcade", "snake", "memory", "whack", "dodge", "speed", "typing",
                      "reaction", "blocks", "game", "score", "window", "canvas", "button"]
        self.running = False

    def on_show(self):
        self.start_game()

    def start_game(self):
        self.score = 0
        self.time_left = 30
        self.running = True
        self.next_word()
        self.entry.delete(0, tk.END)
        self.entry.focus_set()
        self.countdown()

    def stop_game(self):
        self.running = False
        self.controller.show_frame("MainMenu")

    def next_word(self):
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word)

    def check_word(self, event=None):
        if self.running and self.entry.get().strip().lower() == self.current_word:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.entry.delete(0, tk.END)
            self.next_word()

    def countdown(self):
        if not self.running: return
        if self.time_left <= 0:
            self.game_over()
            return
        self.time_left -= 1
        self.time_label.config(text=f"Time: {self.time_left}")
        self.after(1000, self.countdown)

    def game_over(self):
        self.running = False
        self.word_label.config(text=f"Time's up! Score: {self.score}")


if __name__ == "__main__":
    app = ArcadeApp()
    app.mainloop()