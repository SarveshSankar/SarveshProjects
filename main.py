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

# Game settings
WIDTH = 600
HEIGHT = 400
SNAKE_SIZE = 20

HIGH_SCORE_FILE = "highscore.txt"
LEADERBOARD_FILE = "leaderboard.txt"

MINIMAP_SIZE = 120
MINIMAP_PADDING = 10


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Deluxe - Sankar Omega Edition")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black", highlightthickness=0)
        self.canvas.pack()

        # Default Settings
        self.wrap_mode = False
        self.obstacles_enabled = True
        self.difficulty = "Normal"
        self.game_mode = "Classic"
        self.skin = "Neon"

        self.multiplier_active = False
        self.multiplier_timer_id = None
        self.particles = []
        self.game_over_flag = False
        self.paused = False
        self.next_direction = "Right"

        self.time_attack_duration = 60
        self.time_attack_start = None

        self.show_menu()

    # ---------------- MENU SCREEN ----------------
    def show_menu(self):
        self.canvas.delete("all")
        self.canvas.create_text(WIDTH / 2, 60, fill="white", font=("Arial", 32, "bold"), text="SNAKE DELUXE")
        self.canvas.create_text(WIDTH / 2, 100, fill="#888", font=("Arial", 14), text="Sankar Omega Edition")

        self.start_btn = tk.Button(self.root, text="Start Game", font=("Arial", 16), command=self.start_game, width=15)
        self.start_btn.place(x=WIDTH / 2 - 90, y=130)

        self.wrap_btn = tk.Button(self.root, text=f"Wrap Mode: {'ON' if self.wrap_mode else 'OFF'}",
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

        self.leader_btn = tk.Button(self.root, text="Show Leaderboard", command=self.show_leaderboard_screen, width=20)
        self.leader_btn.place(x=WIDTH / 2 - 75, y=330)

        self.quit_btn = tk.Button(self.root, text="Quit", command=self.root.quit, width=10)
        self.quit_btn.place(x=WIDTH / 2 - 40, y=370)

    def toggle_wrap(self):
        self.wrap_mode = not self.wrap_mode
        self.wrap_btn.config(text=f"Wrap Mode: {'ON' if self.wrap_mode else 'OFF'}")

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

    # ---------------- LOGIC & DATA ----------------
    def load_leaderboard(self):
        if not os.path.exists(LEADERBOARD_FILE): return []
        scores = []
        with open(LEADERBOARD_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3: scores.append((parts[0], int(parts[1]), parts[2]))
        return sorted(scores, key=lambda x: x[1], reverse=True)[:5]

    def save_to_leaderboard(self, name, score):
        scores = self.load_leaderboard()
        scores.append((name, score, time.strftime("%Y-%m-%d")))
        scores.sort(key=lambda x: x[1], reverse=True)
        with open(LEADERBOARD_FILE, "w") as f:
            for n, s, d in scores[:5]: f.write(f"{n},{s},{d}\n")

    def show_leaderboard_screen(self):
        self.canvas.delete("all")
        self.canvas.create_text(WIDTH / 2, 60, fill="white", font=("Arial", 26, "bold"), text="Leaderboard")
        scores = self.load_leaderboard()
        y = 120
        if not scores: self.canvas.create_text(WIDTH / 2, y, fill="white", text="No scores yet.")
        for i, (name, score, date_str) in enumerate(scores, start=1):
            self.canvas.create_text(WIDTH / 2, y, fill="white", font=("Arial", 14),
                                    text=f"{i}. {name} - {score} ({date_str})")
            y += 30
        back_btn = tk.Button(self.root, text="Back", command=lambda: [back_btn.destroy(), self.show_menu()])
        back_btn.place(x=WIDTH / 2 - 20, y=HEIGHT - 40)

    # ---------------- GAME START ----------------
    def start_game(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button): widget.destroy()

        self.score = 0
        self.high_score = self.load_high_score()
        self.score_text = self.canvas.create_text(70, 20, fill="white", font=("Arial", 14), text=f"Score: {self.score}")
        self.high_score_text = self.canvas.create_text(WIDTH - 100, 20, fill="yellow", font=("Arial", 14),
                                                       text=f"High Score: {self.high_score}")

        if self.game_mode == "Time Attack":
            self.time_attack_start = time.time()
            self.time_text = self.canvas.create_text(WIDTH / 2, 20, fill="cyan", font=("Arial", 14), text="Time: 60")

        self.reset_game()
        self.root.bind("<KeyPress>", self.handle_input)
        self.move_snake()
        self.update_particles()

    def load_high_score(self):
        try:
            with open(HIGH_SCORE_FILE, "r") as f:
                return int(f.read().strip())
        except:
            return 0

    def reset_game(self):
        self.direction = "Right"
        self.next_direction = "Right"
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.speed = {"Easy": 150, "Normal": 120, "Hard": 90}[self.difficulty]
        self.paused = False
        self.game_over_flag = False
        self.multiplier_active = False

        self.canvas.delete("snake", "food", "grid", "obstacle", "game_over", "portal", "minimap")
        self.draw_grid()
        self.spawn_obstacles()
        self.spawn_food()
        self.spawn_portals()
        self.draw_snake()

    # ---------------- RENDERING ----------------
    def draw_grid(self):
        for x in range(0, WIDTH, SNAKE_SIZE): self.canvas.create_line(x, 0, x, HEIGHT, fill="#111", tag="grid")
        for y in range(0, HEIGHT, SNAKE_SIZE): self.canvas.create_line(0, y, WIDTH, y, fill="#111", tag="grid")

    def spawn_obstacles(self):
        self.obstacles = []
        if not self.obstacles_enabled or self.game_mode == "Zen": return
        for _ in range(8):
            x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
            y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
            if (x, y) not in self.snake: self.obstacles.append((x, y))
        for x, y in self.obstacles:
            self.canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill="#444", tag="obstacle")

    def spawn_portals(self):
        self.portals = None
        if self.game_mode == "Zen": return
        x1, y1 = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE, random.randint(0, (
                    HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        x2, y2 = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE, random.randint(0, (
                    HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        self.portals = ((x1, y1), (x2, y2))
        colors = ["cyan", "magenta"]
        for i, (x, y) in enumerate(self.portals):
            self.canvas.create_oval(x + 2, y + 2, x + SNAKE_SIZE - 2, y + SNAKE_SIZE - 2, outline=colors[i], width=2,
                                    tag="portal")

    def draw_snake(self):
        self.canvas.delete("snake")
        for i, (x, y) in enumerate(self.snake):
            h_col, b_col = self.get_colors(i)
            self.canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill=h_col if i == 0 else b_col,
                                         tag="snake")

    def get_colors(self, index):
        if self.skin == "Neon": return ("#39FF14", "#00A36C") if index == 0 else ("#00FF9C", "#006B3C")
        if self.skin == "Rainbow":
            c = ["red", "orange", "yellow", "green", "blue", "purple"][index % 6]
            return (c, c)
        if self.skin == "Fire": return ("#FF4500", "#FF8C00")
        return ("lime", "green")

    def spawn_food(self):
        self.canvas.delete("food")
        types = [("red", 1), ("gold", 5), ("blue", 0)]
        self.food_color, self.food_value = random.choices(types, weights=[80, 15, 5])[0]
        while True:
            self.food = (random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
                         random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)
            if self.food not in self.snake and self.food not in self.obstacles: break
        self.canvas.create_oval(self.food[0], self.food[1], self.food[0] + SNAKE_SIZE, self.food[1] + SNAKE_SIZE,
                                fill=self.food_color, tag="food")

    # ---------------- MINIMAP ----------------
    def draw_minimap(self):
        self.canvas.delete("minimap")
        m_x, m_y = WIDTH - MINIMAP_SIZE - MINIMAP_PADDING, HEIGHT - MINIMAP_SIZE - MINIMAP_PADDING
        self.canvas.create_rectangle(m_x, m_y, m_x + MINIMAP_SIZE, m_y + MINIMAP_SIZE, fill="#111", outline="#333",
                                     tag="minimap")

        ratio = MINIMAP_SIZE / WIDTH
        # Snake head on minimap
        hx, hy = self.snake[0]
        self.canvas.create_rectangle(m_x + hx * ratio, m_y + hy * ratio, m_x + hx * ratio + 2, m_y + hy * ratio + 2,
                                     fill="white", tag="minimap")
        # Food on minimap
        fx, fy = self.food
        self.canvas.create_rectangle(m_x + fx * ratio, m_y + fy * ratio, m_x + fx * ratio + 2, m_y + fy * ratio + 2,
                                     fill=self.food_color, tag="minimap")

    # ---------------- CORE LOOP ----------------
    def handle_input(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.next_direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.next_direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.next_direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.next_direction = "Right"
        elif key.lower() == "p":
            self.paused = not self.paused

    def move_snake(self):
        if self.game_over_flag: return
        if self.paused:
            self.root.after(100, self.move_snake)
            return

        # Time Attack check
        if self.game_mode == "Time Attack":
            rem = max(0, int(self.time_attack_duration - (time.time() - self.time_attack_start)))
            self.canvas.itemconfig(self.time_text, text=f"Time: {rem}")
            if rem <= 0: self.game_over(); return

        self.direction = self.next_direction
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
            hx %= WIDTH; hy %= HEIGHT
        elif hx < 0 or hx >= WIDTH or hy < 0 or hy >= HEIGHT:
            self.game_over(); return

        new_head = (hx, hy)
        if self.portals:
            if new_head == self.portals[0]:
                new_head = self.portals[1]
            elif new_head == self.portals[1]:
                new_head = self.portals[0]

        if new_head in self.snake or new_head in self.obstacles: self.game_over(); return

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += self.food_value * (2 if self.multiplier_active else 1)
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            self.create_particles(hx, hy, self.food_color)
            winsound.Beep(1000, 50)
            self.spawn_food()
            if self.food_color == "gold": self.activate_multiplier()
        else:
            self.snake.pop()

        self.draw_snake()
        self.draw_minimap()
        self.root.after(self.speed, self.move_snake)

    def activate_multiplier(self):
        self.multiplier_active = True
        self.canvas.itemconfig(self.score_text, fill="gold")
        self.root.after(5000, lambda: [setattr(self, 'multiplier_active', False),
                                       self.canvas.itemconfig(self.score_text, fill="white")])

    def create_particles(self, x, y, color):
        for _ in range(8):
            p = self.canvas.create_oval(x, y, x + 4, y + 4, fill=color, outline="")
            self.particles.append([p, random.uniform(-2, 2), random.uniform(-2, 2), 10])

    def update_particles(self):
        try:
            for p_data in self.particles[:]:
                p, dx, dy, life = p_data
                self.canvas.move(p, dx, dy)
                p_data[3] -= 1
                if p_data[3] <= 0: self.canvas.delete(p); self.particles.remove(p_data)
            self.root.after(30, self.update_particles)
        except:
            pass

    def game_over(self):
        self.game_over_flag = True
        if self.score > self.high_score:
            with open(HIGH_SCORE_FILE, "w") as f: f.write(str(self.score))
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2, text="GAME OVER", fill="red", font=("Arial", 32, "bold"),
                                tag="game_over")
        btn = tk.Button(self.root, text="Restart", command=self.start_game)
        btn.place(x=WIDTH / 2 - 30, y=HEIGHT / 2 + 50)


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()