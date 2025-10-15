import tkinter as tk
import time
import threading

# Pomodoro settings (in minutes)
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
CYCLES = 4

# For testing, use shorter times
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.1

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("300x200")
        self.root.configure(bg="#f0f0f0")

        self.label = tk.Label(root, text="Ready", font=("Helvetica", 16), bg="#f0f0f0")
        self.label.pack(pady=20)

        self.timer_label = tk.Label(root, text="", font=("Helvetica", 24), bg="#f0f0f0")
        self.timer_label.pack()

        self.start_button = tk.Button(root, text="Start Pomodoro", command=self.start_pomodoro)
        self.start_button.pack(pady=10)

        self.cycle = 0

    def start_pomodoro(self):
        threading.Thread(target=self.run_cycles).start()

    def run_cycles(self):
        for i in range(1, CYCLES + 1):
            self.cycle = i
            self.run_timer(WORK_MIN * 60, f"Pomodoro {i}", "#4CAF50")
            if i < CYCLES:
                self.run_timer(SHORT_BREAK_MIN * 60, "Short Break", "#2196F3")
            else:
                self.run_timer(LONG_BREAK_MIN * 60, "Long Break", "#9C27B0")

    def run_timer(self, seconds, label_text, color):
        self.label.config(text=label_text, fg=color)
        for remaining in range(int(seconds), -1, -1):
            mins, secs = divmod(remaining, 60)
            time_str = f"{int(mins):02d}:{int(secs):02d}"
            self.timer_label.config(text=time_str)
            self.root.update()
            time.sleep(1)
        print('\a', end='', flush=True)  # System beep

# Run the app
root = tk.Tk()
app = PomodoroApp(root)
root.mainloop()
