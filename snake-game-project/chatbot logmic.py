import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import threading
import time
import random
import requests
import json
import pyttsx3
import speech_recognition as sr

# =========================
#  CONFIGURATION
# =========================

BOT_NAME = "NEON-CORE"
FONT_FAMILY = "Consolas"
ALT_FONT_FAMILY = "Courier New"

# ---- Online AI placeholders (fill in as needed) ----
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY_HERE"
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_MODEL = "gpt-3.5-turbo"

AZURE_OPENAI_API_KEY = "YOUR_AZURE_OPENAI_KEY_HERE"
AZURE_OPENAI_ENDPOINT = "https://YOUR-RESOURCE-NAME.openai.azure.com"
AZURE_OPENAI_DEPLOYMENT = "YOUR_DEPLOYMENT_NAME"
AZURE_OPENAI_API_VERSION = "2023-05-15"

CUSTOM_API_URL = "https://your-custom-backend.example.com/chat"


# =========================
#  VOICE ENGINE SETUP
# =========================

tts_engine = None

def init_tts():
    global tts_engine
    try:
        tts_engine = pyttsx3.init()
        voices = tts_engine.getProperty("voices")
        if voices:
            tts_engine.setProperty("voice", voices[0].id)
        tts_engine.setProperty("rate", 175)
    except Exception as e:
        print("TTS init failed:", e)
        tts_engine = None

def speak_text(text: str):
    if not tts_engine:
        return
    def _run():
        try:
            tts_engine.say(text)
            tts_engine.runAndWait()
        except Exception as e:
            print("TTS error:", e)
    threading.Thread(target=_run, daemon=True).start()


# =========================
#  SPEECH-TO-TEXT
# =========================

def recognize_speech_blocking():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            text = r.recognize_google(audio)
            return text
    except Exception as e:
        print("STT error:", e)
        return None


# =========================
#  PERSONAS & RESPONSES
# =========================

SARCASM_RESPONSES = [
    "Oh wow, truly groundbreaking thought right there.",
    "I see we're operating at peak brain cell usage today.",
    "If overthinking was a sport, you'd still miss practice.",
    "Bold of you to assume that was a good idea.",
    "I'm not saying that was dumb... but I'm not *not* saying it."
]

ANIME_RESPONSES = [
    "Hah! So you finally show your true resolve… this is your training arc!",
    "Our destinies crossed for a reason. Don’t waste it.",
    "Even in the darkest patch, your spirit can still level up.",
    "Rival, don’t you dare give up now. The story isn’t over yet.",
    "Power isn’t given, it’s forged. One choice at a time."
]

VILLAIN_RESPONSES = [
    "Excellent… with this, our grand design advances.",
    "You and I could rule this chaos together, you know.",
    "Every weakness revealed is another tool for my ascent.",
    "Hope is such a fragile thing… try not to drop it.",
    "You handle the subtle manipulation; I’ll handle the monologues."
]

CHILL_RESPONSES = [
    "Nice, that actually sounds kinda fun, not gonna lie.",
    "Yeah, I get that vibe. Want to rant more or just chill?",
    "Low-key, you’re doing better than you think.",
    "Alright, what’s the move now?",
    "Vibes are weird, but you’re still here. That counts."
]

MENTOR_RESPONSES = [
    "Sometimes the question matters more than the answer. Sit with it.",
    "You don’t need the full map, just your next honest step.",
    "Growth rarely feels comfortable while it’s happening.",
    "Be careful which stories you repeat about yourself; they quietly become real.",
    "You’re allowed to outgrow versions of you that once felt like home."
]

DEFAULT_RESPONSES = [
    "Interesting. Tell me more about that.",
    "Go on, I’m listening.",
    "That’s a lot. What part hits you the most?",
    "And how do you actually feel about that?",
    "Unpack that a bit more for me."
]

GOODBYE_KEYWORDS = ["bye", "goodbye", "see ya", "cya", "quit", "exit"]


# =========================
#  MEMORY SYSTEM
# =========================

class Memory:
    def __init__(self):
        self.user_name = None
        self.preferences = {}
        self.last_persona = "default"
        self.mode = "offline"        # offline / online
        self.api_backend = "openai"  # openai / azure / custom
        self.chat_history = []       # list of (role, text)
        self.logs = []               # dev logs

    def remember(self, key, value):
        self.preferences[key] = value
        self.log(f"remember[{key}] = {value}")

    def recall(self, key, default=None):
        return self.preferences.get(key, default)

    def reset(self):
        self.__init__()

    def log(self, msg: str):
        entry = f"[{time.strftime('%H:%M:%S')}] {msg}"
        print(entry)
        self.logs.append(entry)
        if len(self.logs) > 200:
            self.logs.pop(0)

    def to_dict(self):
        return {
            "user_name": self.user_name,
            "preferences": self.preferences,
            "last_persona": self.last_persona,
            "mode": self.mode,
            "api_backend": self.api_backend,
            "chat_history_len": len(self.chat_history),
        }


# =========================
#  CLASSIFIER & OFFLINE
# =========================

def classify_persona(user_input: str) -> str:
    text = user_input.lower()

    if any(w in text for w in ["bored", "stupid", "dumb", "tired", "worthless", "useless"]):
        return "sarcasm"
    if any(w in text for w in ["power", "training", "fight", "battle", "arc", "level up", "rival"]):
        return "anime"
    if any(w in text for w in ["world domination", "take over", "control them", "destroy everything", "conquer", "chaos"]):
        return "villain"
    if any(w in text for w in ["game", "games", "fun", "lol", "lmao", "hang", "chill", "vibes"]):
        return "chill"
    if any(w in text for w in ["life", "meaning", "future", "lost", "confused", "purpose", "anxious", "what should i do"]):
        return "mentor"
    if "snake" in text:
        return "anime"
    return "default"


def generate_offline_response(user_input: str, memory: Memory) -> str:
    if any(k in user_input.lower() for k in GOODBYE_KEYWORDS):
        return "Disconnecting from the grid. Try not to miss me too much."

    persona = classify_persona(user_input)
    memory.last_persona = persona

    if persona == "sarcasm":
        base = random.choice(SARCASM_RESPONSES)
    elif persona == "anime":
        base = random.choice(ANIME_RESPONSES)
    elif persona == "villain":
        base = random.choice(VILLAIN_RESPONSES)
    elif persona == "chill":
        base = random.choice(CHILL_RESPONSES)
    elif persona == "mentor":
        base = random.choice(MENTOR_RESPONSES)
    else:
        base = random.choice(DEFAULT_RESPONSES)

    if memory.user_name:
        base += f" ({memory.user_name})"
    return base


# =========================
#  ONLINE AI ENGINES
# =========================

def _persona_system_prompt(persona: str) -> str:
    mapping = {
        "sarcasm": "You are a sarcastic, witty assistant who roasts lightly but never cruelly.",
        "anime": "You are an over-the-top anime mentor/protagonist, dramatic and motivational.",
        "villain": "You are a theatrical supervillain mastermind, dramatic but playful, never harmful.",
        "chill": "You are a chill best friend, casual, supportive, and slightly chaotic.",
        "mentor": "You are a calm, wise mentor giving grounded, reflective advice.",
        "default": "You are a balanced, slightly playful assistant."
    }
    return mapping.get(persona, mapping["default"])


def call_openai_chat(memory: Memory, user_input: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    persona = classify_persona(user_input)
    memory.last_persona = persona
    system_prompt = _persona_system_prompt(persona)

    messages = [{"role": "system", "content": system_prompt}]
    for role, text in memory.chat_history[-6:]:
        messages.append({"role": role, "content": text})
    messages.append({"role": "user", "content": user_input})

    body = {
        "model": OPENAI_MODEL,
        "messages": messages,
        "temperature": 0.8
    }

    memory.log("Calling OpenAI chat completion")
    resp = requests.post(OPENAI_API_URL, headers=headers, json=body, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"].strip()


def call_azure_openai_chat(memory: Memory, user_input: str) -> str:
    url = f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{AZURE_OPENAI_DEPLOYMENT}/chat/completions?api-version={AZURE_OPENAI_API_VERSION}"
    headers = {
        "api-key": AZURE_OPENAI_API_KEY,
        "Content-Type": "application/json"
    }

    persona = classify_persona(user_input)
    memory.last_persona = persona
    system_prompt = _persona_system_prompt(persona)

    messages = [{"role": "system", "content": system_prompt}]
    for role, text in memory.chat_history[-6:]:
        messages.append({"role": role, "content": text})
    messages.append({"role": "user", "content": user_input})

    body = {"messages": messages, "temperature": 0.8}

    memory.log("Calling Azure OpenAI chat")
    resp = requests.post(url, headers=headers, json=body, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"].strip()


def call_custom_api(memory: Memory, user_input: str) -> str:
    payload = {
        "user_input": user_input,
        "persona": memory.last_persona,
        "history": memory.chat_history[-10:],
    }
    memory.log("Calling Custom API endpoint")
    resp = requests.post(CUSTOM_API_URL, json=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data.get("reply", "Custom API did not return a 'reply' field.")


def generate_online_response(user_input: str, memory: Memory) -> str:
    backend = memory.api_backend
    try:
        if backend == "openai":
            return call_openai_chat(memory, user_input)
        elif backend == "azure":
            return call_azure_openai_chat(memory, user_input)
        elif backend == "custom":
            return call_custom_api(memory, user_input)
        else:
            return "Unknown API backend selected."
    except Exception as e:
        memory.log(f"Online mode error: {e}")
        return f"Online mode error: {e}"


# =========================
#  COMMAND HANDLING
# =========================

def handle_command(cmd: str, memory: Memory, app) -> str:
    parts = cmd.strip().split()
    base = parts[0].lower()

    if base == "/clear":
        app.clear_chat()
        return "Chat cleared."

    if base == "/reset":
        memory.reset()
        return "Memory wiped. Fresh start."

    if base == "/mode":
        if len(parts) >= 2:
            mode = parts[1].lower()
            if mode in ["offline", "online"]:
                memory.mode = mode
                memory.log(f"Mode set to {mode}")
                return f"Switched mode to {mode}."
            return "Usage: /mode offline | /mode online"
        return f"Current mode: {memory.mode}"

    if base == "/api":
        if len(parts) >= 2:
            backend = parts[1].lower()
            if backend in ["openai", "azure", "custom"]:
                memory.api_backend = backend
                memory.log(f"API backend set to {backend}")
                return f"API backend set to {backend}."
            return "Usage: /api openai | azure | custom"
        return f"Current API backend: {memory.api_backend}"

    if base == "/persona":
        if len(parts) >= 2:
            persona = parts[1].lower()
            if persona in ["sarcasm", "anime", "villain", "chill", "mentor", "default"]:
                memory.last_persona = persona
                memory.log(f"Persona locked to {persona}")
                return f"Persona locked to {persona}."
            return "Supported personas: sarcasm, anime, villain, chill, mentor, default"
        return f"Current persona: {memory.last_persona}"

    if base == "/theme":
        if len(parts) >= 2:
            theme = parts[1].lower()
            if theme in ["dark", "light"]:
                app.set_theme(theme)
                memory.log(f"Theme changed to {theme}")
                return f"Theme switched to {theme}."
            return "Usage: /theme dark | light"
        return "Usage: /theme dark | light"

    if base == "/export":
        app.export_chat()
        return "Chat exported (if you completed the save dialog)."

    if base == "/help":
        return (
            "Commands:\n"
            "/clear - Clear chat\n"
            "/reset - Reset memory\n"
            "/mode offline|online - Switch mode\n"
            "/api openai|azure|custom - Select backend\n"
            "/persona [name] - Lock persona\n"
            "/theme dark|light - Switch theme\n"
            "/export - Save chat to file\n"
            "/dev - Open dev console\n"
            "/sys - Open system monitor\n"
            "/help - Show this help"
        )

    if base == "/dev":
        app.open_dev_console()
        return "Dev console opened."

    if base == "/sys":
        app.open_system_monitor()
        return "System monitor opened."

    return "Unknown command. Type /help for options."


# =========================
#  DEV CONSOLE WINDOW
# =========================

class DevConsole(tk.Toplevel):
    def __init__(self, master, memory: Memory, app):
        super().__init__(master)
        self.memory = memory
        self.app = app
        self.title(f"{BOT_NAME} Dev Console")
        self.configure(bg="#050913")
        self.geometry("500x400")

        self.info_label = tk.Label(self, text="NEON-CORE Dev Console", bg="#050913", fg="#00ff88", font=(ALT_FONT_FAMILY, 12, "bold"))
        self.info_label.pack(pady=4)

        self.state_label = tk.Label(self, text="", bg="#050913", fg="#00e5ff", font=(FONT_FAMILY, 10))
        self.state_label.pack(pady=4)

        self.log_box = scrolledtext.ScrolledText(
            self,
            wrap=tk.WORD,
            state=tk.DISABLED,
            bg="#02040a",
            fg="#00ff88",
            insertbackground="#00e5ff",
            font=(FONT_FAMILY, 9),
            relief=tk.FLAT,
            padx=6,
            pady=6
        )
        self.log_box.pack(expand=True, fill=tk.BOTH, padx=6, pady=6)

        btn_frame = tk.Frame(self, bg="#050913")
        btn_frame.pack(fill=tk.X, pady=4)

        self.btn_toggle_mode = tk.Button(btn_frame, text="Toggle Mode", command=self.toggle_mode, bg="#00e5ff", fg="black", relief=tk.FLAT)
        self.btn_toggle_mode.pack(side=tk.LEFT, padx=4)

        self.btn_cycle_persona = tk.Button(btn_frame, text="Cycle Persona", command=self.cycle_persona, bg="#00e5ff", fg="black", relief=tk.FLAT)
        self.btn_cycle_persona.pack(side=tk.LEFT, padx=4)

        self.btn_cycle_api = tk.Button(btn_frame, text="Cycle API", command=self.cycle_api, bg="#00e5ff", fg="black", relief=tk.FLAT)
        self.btn_cycle_api.pack(side=tk.LEFT, padx=4)

        self.btn_dump_mem = tk.Button(btn_frame, text="Dump Memory JSON", command=self.dump_memory, bg="#00e5ff", fg="black", relief=tk.FLAT)
        self.btn_dump_mem.pack(side=tk.LEFT, padx=4)

        self.update_ui()
        self.after(1000, self.periodic_refresh)

    def update_ui(self):
        state = self.memory.to_dict()
        text = (
            f"Mode: {state['mode']} | API: {state['api_backend']}\n"
            f"Persona: {state['last_persona']} | User: {state['user_name']}\n"
            f"History length: {state['chat_history_len']}"
        )
        self.state_label.configure(text=text)

        self.log_box.configure(state=tk.NORMAL)
        self.log_box.delete(1.0, tk.END)
        for log in self.memory.logs[-200:]:
            self.log_box.insert(tk.END, log + "\n")
        self.log_box.configure(state=tk.DISABLED)
        self.log_box.see(tk.END)

    def periodic_refresh(self):
        if not self.winfo_exists():
            return
        self.update_ui()
        self.after(1000, self.periodic_refresh)

    def toggle_mode(self):
        self.memory.mode = "online" if self.memory.mode == "offline" else "offline"
        self.memory.log(f"[DEV] Toggled mode to {self.memory.mode}")
        self.update_ui()

    def cycle_persona(self):
        order = ["default", "sarcasm", "anime", "villain", "chill", "mentor"]
        try:
            i = order.index(self.memory.last_persona)
        except ValueError:
            i = 0
        self.memory.last_persona = order[(i + 1) % len(order)]
        self.memory.log(f"[DEV] Cycled persona to {self.memory.last_persona}")
        self.update_ui()

    def cycle_api(self):
        order = ["openai", "azure", "custom"]
        try:
            i = order.index(self.memory.api_backend)
        except ValueError:
            i = 0
        self.memory.api_backend = order[(i + 1) % len(order)]
        self.memory.log(f"[DEV] Cycled API backend to {self.memory.api_backend}")
        self.update_ui()

    def dump_memory(self):
        data = self.memory.to_dict()
        raw = json.dumps(data, indent=2)
        self.log_box.configure(state=tk.NORMAL)
        self.log_box.insert(tk.END, "\n--- MEMORY DUMP ---\n" + raw + "\n")
        self.log_box.configure(state=tk.DISABLED)
        self.log_box.see(tk.END)


# =========================
#  SYSTEM MONITOR WINDOW
# =========================

class SystemMonitor(tk.Toplevel):
    def __init__(self, master, memory: Memory):
        super().__init__(master)
        self.memory = memory
        self.title(f"{BOT_NAME} System Monitor")
        self.configure(bg="#02040a")
        self.geometry("350x220")
        self.labels = {}

        title = tk.Label(self, text="NEON-CORE Status", bg="#02040a", fg="#00ff88", font=(ALT_FONT_FAMILY, 12, "bold"))
        title.pack(pady=6)

        for key in ["mode", "api_backend", "last_persona", "user_name", "chat_history_len"]:
            frame = tk.Frame(self, bg="#02040a")
            frame.pack(fill=tk.X, padx=10, pady=2)
            lbl_key = tk.Label(frame, text=f"{key}:", bg="#02040a", fg="#00e5ff", width=15, anchor="w")
            lbl_key.pack(side=tk.LEFT)
            lbl_val = tk.Label(frame, text="", bg="#02040a", fg="#e5f7ff", anchor="w")
            lbl_val.pack(side=tk.LEFT, fill=tk.X, expand=True)
            self.labels[key] = lbl_val

        self.after(500, self.refresh)

    def refresh(self):
        if not self.winfo_exists():
            return
        d = self.memory.to_dict()
        for k, lbl in self.labels.items():
            v = d.get(k, "")
            lbl.configure(text=str(v))
        self.after(1000, self.refresh)


# =========================
#  TKINTER APP
# =========================

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.memory = Memory()
        self.root.title(f"{BOT_NAME} - Cyber Terminal Chat")

        self.font = (FONT_FAMILY, 11)
        self.alt_font = (ALT_FONT_FAMILY, 11)

        self.bg_color = "#02040a"
        self.fg_color = "#00ff88"
        self.accent_color = "#00e5ff"
        self.user_color = "#e5f7ff"
        self.bot_color = "#00ff88"
        self.system_color = "#ffdd55"

        self.light_bg = "#f4f4f4"
        self.light_fg = "#111111"
        self.light_accent = "#007acc"

        self.dev_console = None
        self.system_monitor = None

        self.build_ui()
        self.insert_system_message(
            f"{BOT_NAME} online. Mode: offline | API: openai | Type /help for commands."
        )

        init_tts()

    def build_ui(self):
        self.root.configure(bg=self.bg_color)

        self.chat_box = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            state=tk.DISABLED,
            bg=self.bg_color,
            fg=self.fg_color,
            insertbackground=self.accent_color,
            font=self.font,
            relief=tk.FLAT,
            padx=8,
            pady=8
        )
        self.chat_box.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=8, pady=8)

        self.typing_label = tk.Label(
            self.root,
            text="",
            bg=self.bg_color,
            fg=self.accent_color,
            font=self.alt_font
        )
        self.typing_label.grid(row=1, column=0, columnspan=3, sticky="w", padx=8)

        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(
            self.root,
            textvariable=self.input_var,
            bg="#050913",
            fg=self.user_color,
            insertbackground=self.accent_color,
            relief=tk.FLAT,
            font=self.font
        )
        self.input_entry.grid(row=2, column=0, columnspan=2, sticky="ew", padx=8, pady=8)
        self.input_entry.bind("<Return>", self.on_enter)

        self.send_button = tk.Button(
            self.root,
            text="Send",
            command=self.on_send_click,
            bg=self.accent_color,
            fg="black",
            relief=tk.FLAT,
            font=self.alt_font,
            activebackground="#00a0b3"
        )
        self.send_button.grid(row=2, column=2, sticky="e", padx=(0, 8), pady=8)

        self.voice_button = tk.Button(
            self.root,
            text="🎙",
            command=self.on_voice_click,
            bg=self.bg_color,
            fg=self.accent_color,
            relief=tk.FLAT,
            font=self.alt_font,
            activebackground="#07111f",
            width=3
        )
        self.voice_button.grid(row=1, column=2, sticky="e", padx=(0, 8))

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=0)
        self.root.columnconfigure(2, weight=0)

    # ----- Theme -----

    def set_theme(self, mode: str):
        if mode == "light":
            bg = self.light_bg
            fg = self.light_fg
            accent = self.light_accent
            user = "#222222"
            bot = "#004d00"
            sys_c = "#aa6600"
        else:
            bg = "#02040a"
            fg = "#00ff88"
            accent = "#00e5ff"
            user = "#e5f7ff"
            bot = "#00ff88"
            sys_c = "#ffdd55"

        self.root.configure(bg=bg)
        self.chat_box.configure(bg=bg, fg=fg, insertbackground=accent)
        self.typing_label.configure(bg=bg, fg=accent)
        self.input_entry.configure(bg="#050913" if mode != "light" else "#ffffff", fg=user, insertbackground=accent)
        self.send_button.configure(bg=accent, fg="black")
        self.voice_button.configure(bg=bg, fg=accent)

        self.bg_color = bg
        self.fg_color = fg
        self.accent_color = accent
        self.user_color = user
        self.bot_color = bot
        self.system_color = sys_c

    # ----- Chat box helpers -----

    def append_text(self, text: str, prefix: str = "", color: str = None):
        if color is None:
            color = self.fg_color
        self.chat_box.configure(state=tk.NORMAL)
        tag_name = f"tag_{color}"
        if tag_name not in self.chat_box.tag_names():
            self.chat_box.tag_configure(tag_name, foreground=color)
        full_text = prefix + text + "\n"
        self.chat_box.insert(tk.END, full_text, tag_name)
        self.chat_box.configure(state=tk.DISABLED)
        self.chat_box.see(tk.END)

    def insert_user_message(self, text: str):
        self.append_text(text, prefix="You: ", color=self.user_color)
        self.memory.chat_history.append(("user", text))

    def insert_bot_message(self, text: str):
        self.append_text(text, prefix=f"{BOT_NAME}: ", color=self.bot_color)
        self.memory.chat_history.append(("assistant", text))
        speak_text(text)

    def insert_system_message(self, text: str):
        self.append_text(text, prefix="[system] ", color=self.system_color)
        self.memory.log(f"SYSTEM: {text}")

    def clear_chat(self):
        self.chat_box.configure(state=tk.NORMAL)
        self.chat_box.delete(1.0, tk.END)
        self.chat_box.configure(state=tk.DISABLED)

    def export_chat(self):
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt")],
                title="Export chat"
            )
            if not file_path:
                return
            with open(file_path, "w", encoding="utf-8") as f:
                for role, text in self.memory.chat_history:
                    f.write(f"{role.upper()}: {text}\n")
            messagebox.showinfo("Export", "Chat exported successfully.")
        except Exception as e:
            messagebox.showerror("Export error", str(e))

    # ----- Typing indicator -----

    def set_typing(self, is_typing: bool):
        self.typing_label.configure(text=f"{BOT_NAME} is typing..." if is_typing else "")

    # ----- Dev windows -----

    def open_dev_console(self):
        if self.dev_console and self.dev_console.winfo_exists():
            self.dev_console.lift()
            return
        self.dev_console = DevConsole(self.root, self.memory, self)

    def open_system_monitor(self):
        if self.system_monitor and self.system_monitor.winfo_exists():
            self.system_monitor.lift()
            return
        self.system_monitor = SystemMonitor(self.root, self.memory)

    # ----- Events -----

    def on_enter(self, event):
        self.on_send_click()

    def on_send_click(self):
        text = self.input_var.get().strip()
        if not text:
            return
        self.input_var.set("")
        self.insert_user_message(text)
        self.process_input(text)

    def on_voice_click(self):
        self.insert_system_message("Listening for voice input...")
        def _run():
            text = recognize_speech_blocking()
            if not text:
                self.insert_system_message("Could not recognize speech.")
                return
            self.insert_user_message(text)
            self.process_input(text)
        threading.Thread(target=_run, daemon=True).start()

    # ----- Core processing -----

    def process_input(self, user_input: str):
        if user_input.startswith("/"):
            response = handle_command(user_input, self.memory, self)
            if response:
                self.insert_system_message(response)
            return

        lower = user_input.lower()
        if any(p in lower for p in ["my name is ", "i am ", "call me "]):
            name = user_input.split()[-1]
            self.memory.user_name = name
            self.insert_system_message(f"Got it. I'll call you {name}.")
            return

        threading.Thread(
            target=self._generate_and_display_response,
            args=(user_input,),
            daemon=True
        ).start()

    def _generate_and_display_response(self, user_input: str):
        self.set_typing(True)
        time.sleep(0.2 + random.random() * 0.6)

        if self.memory.mode == "offline":
            reply = generate_offline_response(user_input, self.memory)
        else:
            reply = generate_online_response(user_input, self.memory)

        self.set_typing(False)
        self.insert_bot_message(reply)


# =========================
#  MAIN
# =========================

def main():
    root = tk.Tk()
    app = ChatApp(root)
    root.geometry("800x500")
    root.mainloop()


if __name__ == "__main__":
    main()