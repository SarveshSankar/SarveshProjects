'''import time
import random
x = input("Do you want to play the number guessing game?").lower()
if x == "yes":
    print("okay")
    time.sleep(1)
    print("lets begin")
    time.sleep(1)
    attempts = 10
    y = random.randint(1,100)
    for i in range(attempts):
     z = int and float(input("What is your guess?"))

     if y > z:
         print("too low")
     if z > y:
         print("too high")
     if z == y:
         print("you win")
         break
else:
   print("okay then")'''


'''import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.title("Drawing board")
t = turtle.Turtle()
t.speed(0)
t.shape("circle")
rainbow_colors = [
    (255, 0, 0),       # Red
    (255, 127, 0),     # Orange
    (255, 255, 0),     # Yellow
    (0, 255, 0),       # Green
    (0, 0, 255),       # Blue
    (75, 0, 130),      # Indigo
    (148, 0, 211) ,     # Violet
]
turtle.colormode(255)
for i in range(10):
    color = rainbow_colors[i%len(rainbow_colors)]
    t.pencolor(color)
    t.pencolor(color)

for y in range(360):
        t.forward(100+random.random())
        t.left(90)
        t.right(90)




turtle.done()'''

'''import time
y = input("Want to play the geography quiz?").lower()
if y == "yes":
    print("okay")
    time.sleep(1)
    print("lets begin")
else:
    print("okay then")
score = 0
z = input("What it is the capital of denmark?")
if z == "copenhagen".lower():

    print("correct you have a score of",score + 1)

else:
    print("incorrect you have a score of",score)
a = input("What is the capital of Germany?").lower()
if a == 'berlin'.lower():
   
    print("correct you have a score of",score + 1)
else:
    print("incorrect you have a score of",score)
b = input("What is the capital of Ontario?").lower()
if b == 'Toronto'.lower():

    print("correct you have a score of",score + 3)
else:
    print("incorrect you have a score of",score)'''



'''import tkinter as tk
tk._test()''' # testing the tkinter module to see if it works

'''import tkinter as tk #importing the module
root = tk.Tk()    #root is the main window/parent window for any GUI(Graphical User Interface)
root.title('App')#Titiling root
def add_list(event= None):
    text = entry.get()
    if text:
       tst_list.insert(tk.END, text)
       entry.delete(0, tk.END)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = tk.Frame(root)# get the frame
frame.grid(row=0,column=0,sticky = 'nsew')#placing the frame in the app
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
entry = tk.Entry(frame)
entry.grid(row=0,column=0,sticky='nsew')
entry.bind('<Return>',add_list)
entry_btn = tk.Button(frame,text="Add",command=add_list)
entry_btn.grid(row=0,column=0)
tst_list = tk.Listbox(frame)
tst_list.grid(row=1,column=0,columnspan = 2,sticky='nsew')
root.mainloop() #loops the root


''''''def on_click():             # on click func defined
    print("Testing") #onclick func prints testing
def on_click2():
    lbl.config(text = "Button is clicked")# config changes the lbl text


lbl = tk.Label(root, text='Label 1') #creating a label
lbl.grid(row = 0, column = 0) #putting the label in place
#print(lbl.config().keys())#prints all the available keys

btn = tk.Button(root, text='Button 1',command=on_click2) #creating a button to the window root, parent window command = on click which is testing

btn.grid(row = 0,column = 1) #making it organized by rows with grid()
root.mainloop()  #loops the root
'''

'''class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
emp = Employee("James",20000)
print(emp.name)
print(emp.salary)'''


'''import time
import random
class Pet:
    def __init__(self,hunger,energy):
        self.hunger = hunger
        self.energy = energy

    def status(self):
        if self.hunger > 50 and self.energy > 50:
            time.sleep(1)
            print("I'm active but i want to eat")

        elif self.hunger < 50 and self.energy < 50:
            time.sleep(1)
            print("I'm not hungry but not active either")
        else:
            print("I'm in between")
y = random.randint(1,100)
z = random.randint(1,100)
hunger = y
energy = z
My_pet = Pet(hunger,energy)



My_pet.status()'''

'''import tkinter as tk
root = tk.Tk()
root.title('Drawing board')
canvas = tk.Canvas(root,bg= 'white', width=500, height=500)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
canvas.grid(row=0,column=0,sticky='nsew')




now_color = 'black'
def color(set_color):
    global now_color
    now_color = set_color
brush_size = tk.IntVar()
size_slider = tk.Scale(root,from_=1,to=20,orient = 'vertical',variable=brush_size)
size_slider.grid(row=1,column=1)


def draw(event):
    size = size_slider.get()
    x , y = event.x, event.y
    canvas.create_rectangle(x-size,y-size,x+size,y+size,fill = now_color , outline = 'Black')

def delete():
   canvas.delete('all')

button = tk.Button(root,text='delete',command=delete )
button2 = tk.Button(root,text = 'red', command = lambda: color('red'))
button3 = tk.Button(root,text = 'orange', command = lambda: color('orange'))
button4 = tk.Button(root,text = 'yellow', command = lambda: color('yellow'))
button5 = tk.Button(root,text = 'green', command = lambda: color('green'))
button6 = tk.Button(root,text = 'blue', command = lambda: color('blue'))
button7 = tk.Button(root,text = 'purple', command = lambda: color('purple'))
button8 = tk.Button(root,text = 'black', command = lambda: color('black'))
button9 = tk.Button(root,text = 'white', command = lambda: color('white'))



button.grid(row=0,column=1)
button2.grid(row=0,column=2)
button3.grid(row=0,column=3)
button4.grid(row=0,column=4)
button5.grid(row=0,column=5)
button6.grid(row=0,column=6)
button7.grid(row=0,column=7)
button8.grid(row=0,column=8)
button9.grid(row=0,column=9)






canvas.bind('<B1-Motion>',draw)
root.mainloop()'''
'''from tkinter import messagebox
import tkinter as tk

root = tk.Tk()
root.title('Simple GUI')
root.geometry('800x800')

font = ('Arial', 14, 'bold')

lbl_username = tk.Label(root, text='Username', font=font)
lbl_username.pack(pady=(50, 5))
entry_username = tk.Entry(root, font=font)
entry_username.pack(pady=5)

lbl_password = tk.Label(root, text='Password', font=font)
lbl_password.pack(pady=5)
entry_password = tk.Entry(root, show='*', font=font)
entry_password.pack(pady=5)
lbl_message = tk.Label(root, font=font)
lbl_message.pack(pady=5)

def message():
    user = entry_username.get()
    password = entry_password.get()

    if user and password:
        if len(user) < 4 or len(password) < 8:
            messagebox.showerror('Error', 'Username must be at least 4 characters and password at least 8.')
        else:
            lbl_message.config(text='Account has been successfully logged in', fg='green')
    elif user:
        lbl_message.config(text='Please enter password', fg='red')
    elif password:
        lbl_message.config(text='Please enter username', fg='red')
    else:
        lbl_message.config(text='Please enter username and password', fg='red')

btn = tk.Button(root, text='Sign in', font=font, command=message)
btn.pack(pady=20)

root.mainloop()'''
import tkinter as tk
import random
import os
import winsound
import time
from tkinter import simpledialog

# Game settings
WIDTH = 600
HEIGHT = 400
SNAKE_SIZE = 20
LEADERBOARD_FILE = "leaderboard.txt"
MINIMAP_SIZE = 120
MINIMAP_PADDING = 10


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Deluxe - Sarvesh Omega Edition")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black", highlightthickness=0)
        self.canvas.pack()

        # Default Settings
        self.wrap_mode = False
        self.obstacles_enabled = True
        self.difficulty = "Normal"
        self.game_mode = "Classic"
        self.skin = "Neon"

        # State Variables
        self.multiplier_active = False
        self.ghost_active = False
        self.particles = []
        self.game_over_flag = False
        self.paused = False
        self.input_queue = []
        self.food_eaten_count = 0
        self.obstacles = []
        self.portals = []
        self.food = (0, 0)
        self.food_color = "red"

        # Boss Variables
        self.boss_active = False
        self.boss_snake = []
        self.boss_move_counter = 0

        self.high_score = self.get_top_score()
        self.show_menu()

    # ---------------- UI MANAGEMENT ----------------
    def clear_ui(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()
        self.canvas.delete("all")

    def show_menu(self):
        self.clear_ui()
        self.canvas.create_text(WIDTH / 2, 60, fill="white", font=("Arial", 32, "bold"), text="SNAKE DELUXE")
        self.canvas.create_text(WIDTH / 2, 100, fill="#888", font=("Arial", 14), text="Sarvesh Omega Edition")

        tk.Button(self.root, text="Start Game", font=("Arial", 16), command=self.start_game, width=15).place(
            x=WIDTH / 2 - 90, y=130)
        self.wrap_btn = tk.Button(self.root, text=f"Warp Mode: {'ON' if self.wrap_mode else 'OFF'}",
                                  command=self.toggle_wrap, width=20)
        self.wrap_btn.place(x=WIDTH / 2 - 75, y=180)
        self.obs_btn = tk.Button(self.root, text=f"Obstacles: {'ON' if self.obstacles_enabled else 'OFF'}",
                                 command=self.toggle_obstacles, width=20)
        self.obs_btn.place(x=WIDTH / 2 - 75, y=210)
        self.diff_btn = tk.Button(self.root, text=f"Difficulty: {self.difficulty}", command=self.toggle_difficulty,
                                  width=20)
        self.diff_btn.place(x=WIDTH / 2 - 75, y=240)
        self.mode_btn = tk.Button(self.root, text=f"Mode: {self.game_mode}", command=self.toggle_mode, width=20)
        self.mode_btn.place(x=WIDTH / 2 - 75, y=270)
        self.skin_btn = tk.Button(self.root, text=f"Skin: {self.skin}", command=self.toggle_skin, width=20)
        self.skin_btn.place(x=WIDTH / 2 - 75, y=300)
        tk.Button(self.root, text="Leaderboard", command=self.show_leaderboard_screen, width=20).place(x=WIDTH / 2 - 75,
                                                                                                       y=330)

    def toggle_wrap(self):
        self.wrap_mode = not self.wrap_mode
        self.wrap_btn.config(text=f"Warp Mode: {'ON' if self.wrap_mode else 'OFF'}")

    def toggle_obstacles(self):
        self.obstacles_enabled = not self.obstacles_enabled
        self.obs_btn.config(text=f"Obstacles: {'ON' if self.obstacles_enabled else 'OFF'}")

    def toggle_difficulty(self):
        diffs = ["Easy", "Normal", "Hard"]
        self.difficulty = diffs[(diffs.index(self.difficulty) + 1) % 3]
        self.diff_btn.config(text=f"Difficulty: {self.difficulty}")

    def toggle_mode(self):
        modes = ["Classic", "Chaos", "Zen", "Time Attack"]
        self.game_mode = modes[(modes.index(self.game_mode) + 1) % len(modes)]
        self.mode_btn.config(text=f"Mode: {self.game_mode}")

    def toggle_skin(self):
        skins = ["Neon", "Rainbow", "Fire", "Tron", "Classic"]
        self.skin = skins[(skins.index(self.skin) + 1) % len(skins)]
        self.skin_btn.config(text=f"Skin: {self.skin}")

    # ---------------- DATA HANDLING ----------------
    def get_top_score(self):
        scores = self.load_leaderboard()
        return scores[0][1] if scores else 0

    def load_leaderboard(self):
        if not os.path.exists(LEADERBOARD_FILE): return []
        scores = []
        try:
            with open(LEADERBOARD_FILE, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3: scores.append((parts[0], int(parts[1]), parts[2]))
        except:
            pass
        return sorted(scores, key=lambda x: x[1], reverse=True)

    def save_to_leaderboard(self, name, score):
        scores = self.load_leaderboard()
        scores.append((name if name else "Anon", score, time.strftime("%Y-%m-%d")))
        scores.sort(key=lambda x: x[1], reverse=True)
        try:
            with open(LEADERBOARD_FILE, "w") as f:
                for n, s, d in scores[:5]: f.write(f"{n},{s},{d}\n")
        except:
            pass

    def show_leaderboard_screen(self):
        self.clear_ui()
        self.canvas.create_text(WIDTH / 2, 60, fill="white", font=("Arial", 26, "bold"), text="Top 5 Leaderboard")
        scores = self.load_leaderboard()[:5]
        y = 120
        if not scores:
            self.canvas.create_text(WIDTH / 2, y, fill="gray", font=("Arial", 14), text="No scores yet!")
        else:
            for i, (name, score, date_str) in enumerate(scores, start=1):
                self.canvas.create_text(WIDTH / 2, y, fill="white", font=("Arial", 14),
                                        text=f"{i}. {name} - {score} ({date_str})")
                y += 30
        tk.Button(self.root, text="Back", command=self.show_menu).place(x=WIDTH / 2 - 25, y=HEIGHT - 40)

    # ---------------- GAME LOGIC ----------------
    def start_game(self):
        self.clear_ui()
        self.root.focus_force()
        self.canvas.focus_set()

        self.score = 0
        self.food_eaten_count = 0
        self.high_score = self.get_top_score()

        self.game_over_flag = False
        self.paused = False
        self.ghost_active = False
        self.multiplier_active = False
        self.boss_active = False
        self.boss_snake = []
        self.direction = "Right"
        self.input_queue = []

        self.score_text = self.canvas.create_text(70, 20, fill="white", font=("Arial", 14), text=f"Score: {self.score}")
        self.high_score_text = self.canvas.create_text(WIDTH - 100, 20, fill="yellow", font=("Arial", 14),
                                                       text=f"High Score: {self.high_score}")

        if self.game_mode == "Time Attack":
            self.time_attack_start = time.time()
            self.time_text = self.canvas.create_text(WIDTH / 2, 20, fill="cyan", font=("Arial", 14), text="Time: 60")
            self.update_time_attack()

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.speed = {"Easy": 150, "Normal": 120, "Hard": 90}[self.difficulty]

        self.draw_grid()
        self.spawn_obstacles()
        self.spawn_portals()
        self.spawn_food()

        self.root.bind("<KeyPress>", self.handle_input)
        self.move_snake()
        self.update_particles()

    def update_time_attack(self):
        if self.game_mode == "Time Attack" and not self.game_over_flag:
            if not self.paused:
                elapsed = int(time.time() - self.time_attack_start)
                remaining = max(0, 60 - elapsed)
                self.canvas.itemconfig(self.time_text, text=f"Time: {remaining}")
                if remaining <= 0: self.game_over(); return
            self.root.after(1000, self.update_time_attack)

    def handle_input(self, event):
        key = event.keysym
        if key in ["Up", "Down", "Left", "Right"]:
            self.input_queue.append(key)
        elif key.lower() == "p":
            self.paused = not self.paused

    def spawn_boss(self):
        self.boss_active = True
        bx, by = WIDTH - SNAKE_SIZE, HEIGHT - SNAKE_SIZE
        # Boss starts as a small segment
        self.boss_snake = [(bx, by), (bx, by), (bx, by)]
        try:
            winsound.Beep(400, 200)
            winsound.Beep(200, 200)
        except:
            pass

    def move_boss(self):
        """Automated Boss AI Logic"""
        if not self.boss_active or self.game_over_flag or self.paused: return

        bhx, bhy = self.boss_snake[0]
        thx, thy = self.snake[0]
        fx, fy = self.food

        # AI DECISION: Priority 1 - Eat food if close. Priority 2 - Hunt player.
        dist_to_food = abs(bhx - fx) + abs(bhy - fy)
        target_x, target_y = (fx, fy) if dist_to_food < 250 else (thx, thy)

        directions = [(0, -SNAKE_SIZE), (0, SNAKE_SIZE), (-SNAKE_SIZE, 0), (SNAKE_SIZE, 0)]
        valid_moves = []

        for dx, dy in directions:
            nx, ny = bhx + dx, bhy + dy
            # Collision checks for Boss
            if 0 <= nx < WIDTH and 0 <= ny < HEIGHT and (nx, ny) not in self.obstacles and (nx,
                                                                                            ny) not in self.boss_snake:
                dist = abs(nx - target_x) + abs(ny - target_y)
                valid_moves.append(((nx, ny), dist))

        if valid_moves:
            # Choose the move that gets closest to the target
            valid_moves.sort(key=lambda x: x[1])
            best_move = valid_moves[0][0]

            self.boss_snake.insert(0, best_move)

            # Boss interaction logic
            if best_move == self.food:
                # Boss grows if it eats the food!
                self.spawn_food()
                try:
                    winsound.Beep(300, 50)
                except:
                    pass
            elif best_move in self.snake and not self.ghost_active:
                self.game_over()
            else:
                self.boss_snake.pop()

    def spawn_food(self):
        types = [("red", 1, 75), ("gold", 5, 15), ("cyan", 2, 10)]
        self.food_color, self.food_value = random.choices([(t[0], t[1]) for t in types], weights=[t[2] for t in types])[
            0]
        valid_pos = False
        attempts = 0
        while not valid_pos and attempts < 300:
            fx = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
            fy = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
            temp_food = (fx, fy)
            if (temp_food not in self.snake and temp_food not in self.obstacles and
                    temp_food not in self.boss_snake and temp_food not in self.portals):
                self.food = temp_food
                valid_pos = True
            attempts += 1
        self.canvas.delete("food")
        self.canvas.create_oval(self.food[0], self.food[1], self.food[0] + SNAKE_SIZE, self.food[1] + SNAKE_SIZE,
                                fill=self.food_color, outline="white", tag="food")

    def move_snake(self):
        if self.game_over_flag: return
        if self.paused:
            self.root.after(100, self.move_snake)
            return

        if self.input_queue:
            next_move = self.input_queue.pop(0)
            opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
            if next_move != opposites.get(self.direction): self.direction = next_move

        hx, hy = self.snake[0]
        if self.direction == "Up":
            hy -= SNAKE_SIZE
        elif self.direction == "Down":
            hy += SNAKE_SIZE
        elif self.direction == "Left":
            hx -= SNAKE_SIZE
        elif self.direction == "Right":
            hx += SNAKE_SIZE

        if self.wrap_mode:
            hx %= WIDTH;
            hy %= HEIGHT
        elif hx < 0 or hx >= WIDTH or hy < 0 or hy >= HEIGHT:
            self.game_over();
            return

        new_head = (hx, hy)

        if self.portals:
            if new_head == self.portals[0]:
                new_head = self.portals[1]
            elif new_head == self.portals[1]:
                new_head = self.portals[0]

        if not self.ghost_active:
            if (new_head in self.snake and self.game_mode != "Zen") or new_head in self.obstacles:
                self.game_over();
                return
            if self.boss_active and new_head in self.boss_snake:
                self.game_over();
                return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += self.food_value * (2 if self.multiplier_active else 1)
            self.food_eaten_count += 1
            if self.score > self.high_score:
                self.high_score = self.score
                self.canvas.itemconfig(self.high_score_text, text=f"High Score: {self.high_score}")
            if self.score >= 10 and not self.boss_active: self.spawn_boss()
            if self.food_eaten_count % 5 == 0 and self.speed > 40: self.speed -= 5
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            try:
                winsound.Beep(800 + (self.score * 2), 40)
            except:
                pass
            self.create_particles(hx, hy, self.food_color)
            if self.food_color == "gold": self.activate_multiplier()
            if self.food_color == "cyan": self.activate_ghost()
            self.spawn_food()
        else:
            self.snake.pop()

        # Boss moves independently but synced to game ticks
        self.boss_move_counter += 1
        if self.boss_active and self.boss_move_counter % 2 == 0:
            self.move_boss()

        self.draw_frame()
        self.draw_minimap()
        self.root.after(self.speed, self.move_snake)

    def activate_multiplier(self):
        self.multiplier_active = True
        self.canvas.itemconfig(self.score_text, fill="gold")
        self.root.after(7000, lambda: [setattr(self, 'multiplier_active', False),
                                       self.canvas.itemconfig(self.score_text, fill="white")])

    def activate_ghost(self):
        self.ghost_active = True
        self.root.after(5000, lambda: setattr(self, 'ghost_active', False))

    def draw_frame(self):
        self.canvas.delete("snake", "boss")
        for i, (x, y) in enumerate(self.snake):
            fill_color = "white" if self.ghost_active and i > 0 else self.get_snake_color(i)
            self.canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill=fill_color, outline="#222",
                                         tag="snake")
        if self.boss_active:
            for i, (x, y) in enumerate(self.boss_snake):
                color = "red" if i == 0 else "#8B0000"
                self.canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill=color, outline="white",
                                             tag="boss")

    def get_snake_color(self, i):
        if self.skin == "Neon": return "#39FF14" if i == 0 else "#00A36C"
        if self.skin == "Rainbow":
            colors = ["red", "orange", "yellow", "green", "blue", "purple"]
            return colors[i % 6]
        if self.skin == "Fire": return "#FF4500" if i == 0 else "#FF8C00"
        if self.skin == "Tron": return "#00FFFF" if i == 0 else "#00008B"
        return "lime" if i == 0 else "green"

    def draw_grid(self):
        for x in range(0, WIDTH, SNAKE_SIZE): self.canvas.create_line(x, 0, x, HEIGHT, fill="#111", tag="grid")
        for y in range(0, HEIGHT, SNAKE_SIZE): self.canvas.create_line(0, y, WIDTH, y, fill="#111", tag="grid")

    def spawn_obstacles(self):
        self.obstacles = []
        self.canvas.delete("obstacle")
        if not self.obstacles_enabled or self.game_mode == "Zen": return
        for _ in range(8):
            x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
            y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
            if (x, y) not in self.snake:
                self.obstacles.append((x, y))
                self.canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill="#444", tag="obstacle")

    def spawn_portals(self):
        self.portals = []
        self.canvas.delete("portal")
        if self.game_mode == "Zen": return
        for _ in range(2):
            px = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
            py = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
            self.portals.append((px, py))
            self.canvas.create_oval(px + 2, py + 2, px + SNAKE_SIZE - 2, py + SNAKE_SIZE - 2, outline="magenta",
                                    width=2, tag="portal")

    def draw_minimap(self):
        self.canvas.delete("minimap")
        m_x, m_y = WIDTH - MINIMAP_SIZE - MINIMAP_PADDING, HEIGHT - MINIMAP_SIZE - MINIMAP_PADDING
        self.canvas.create_rectangle(m_x, m_y, m_x + MINIMAP_SIZE, m_y + MINIMAP_SIZE, fill="#111", outline="#333",
                                     tag="minimap")
        ratio = MINIMAP_SIZE / WIDTH
        fx, fy = self.food
        self.canvas.create_rectangle(m_x + fx * ratio, m_y + fy * ratio, m_x + fx * ratio + 3, m_y + fy * ratio + 3,
                                     fill=self.food_color, tag="minimap")
        hx, hy = self.snake[0]
        self.canvas.create_rectangle(m_x + hx * ratio, m_y + hy * ratio, m_x + hx * ratio + 3, m_y + hy * ratio + 3,
                                     fill="white", tag="minimap")
        if self.boss_active:
            bx, by = self.boss_snake[0]
            self.canvas.create_rectangle(m_x + bx * ratio, m_y + by * ratio, m_x + bx * ratio + 3, m_y + by * ratio + 3,
                                         fill="red", tag="minimap")

    def create_particles(self, x, y, color):
        for _ in range(6):
            p = self.canvas.create_oval(x, y, x + 4, y + 4, fill=color, outline="")
            self.particles.append([p, random.uniform(-3, 3), random.uniform(-3, 3), 12])

    def update_particles(self):
        if self.game_over_flag: return
        for p_data in self.particles[:]:
            p, dx, dy, life = p_data
            self.canvas.move(p, dx, dy)
            p_data[3] -= 1
            if p_data[3] <= 0:
                self.canvas.delete(p)
                self.particles.remove(p_data)
        self.root.after(40, self.update_particles)

    def game_over(self):
        if self.game_over_flag: return
        self.game_over_flag = True
        try:
            winsound.Beep(200, 500)
        except:
            pass
        self.canvas.create_rectangle(WIDTH / 2 - 150, HEIGHT / 2 - 60, WIDTH / 2 + 150, HEIGHT / 2 + 80, fill="black",
                                     outline="red")
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2 - 10, text="GAME OVER", fill="red", font=("Arial", 30, "bold"))
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2 + 30, text=f"Final Score: {self.score}", fill="white",
                                font=("Arial", 16))
        tk.Button(self.root, text="Restart", command=self.start_game, width=10).place(x=WIDTH / 2 - 100,
                                                                                      y=HEIGHT / 2 + 90)
        tk.Button(self.root, text="Main Menu", command=self.show_menu, width=10).place(x=WIDTH / 2 + 20,
                                                                                       y=HEIGHT / 2 + 90)
        self.root.after(100, self.prompt_leaderboard)

    def prompt_leaderboard(self):
        if self.score > 0:
            name = simpledialog.askstring("High Score!", "Enter your name:", parent=self.root)
            if name:
                self.save_to_leaderboard(name, self.score)
                self.high_score = self.get_top_score()


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()