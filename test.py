import time
import random
import os

print("hello")
for i in range(1, 11):
    print(i)

fireworks = [
    "        *        ",
    "       ***       ",
    "      *****      ",
    "    *********    ",
    "  *************  ",
    "*****************",
    "  *************  ",
    "    *********    ",
    "      *****      ",
    "       ***       ",
    "        *        "
]

colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
    "\033[97m",  # White
]

def clear():
    os.system('clear')

def show_firework():
    color = random.choice(colors)
    for line in fireworks:
        print(color + line + "\033[0m")
        time.sleep(0.05)
    time.sleep(0.3)
    clear()

def fireworks_show(times=10):
    clear()
    for _ in range(times):
        show_firework()
    print("🎆 Happy Fireworks Show! 🎆")

if __name__ == "__main__":
    fireworks_show()