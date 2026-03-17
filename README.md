# 🐍 Snake Game

A classic Snake Game built with **Python** and the **Turtle graphics library** — featuring smooth movement, collision detection, food spawning, and a live scoreboard.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Library](https://img.shields.io/badge/Library-Turtle-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 📸 Preview

> *Snake navigates the screen, eats food to grow longer, and ends when it hits a wall or itself.*

---

## 🎮 Features

- 🟩 **Classic Snake Movement** — smooth, segment-based motion
- 🍎 **Random Food Spawning** — food appears at random positions each time it's eaten
- 📊 **Live Scoreboard** — score updates in real time as you eat food
- 💥 **Collision Detection** — wall collision and self-collision end the game
- ⌨️ **Keyboard Controls** — Arrow key navigation with direction lock (no 180° reversals)

---

## 🗂️ Project Structure

```
snake-game/
│
├── main.py       # Entry point — sets up screen, game loop, and event handling
├── snake.py      # Snake class — movement, growth, and direction control
├── food.py       # Food class — spawns food at random positions
├── score.py      # Scoreboard class — tracks and displays the score
└── README.md     # Project documentation
```

---

## ⚙️ Requirements

- Python 3.x
- No external libraries needed — uses the built-in `turtle` module

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/snake-game.git
cd snake-game
```

### 2. Run the game

```bash
python main.py
```

> Make sure you have Python 3 installed. You can check with `python --version`.

---

## 🕹️ Controls

| Key        | Action       |
|------------|--------------|
| ⬆️ Up Arrow  | Move Up      |
| ⬇️ Down Arrow | Move Down   |
| ➡️ Right Arrow | Move Right |
| ⬅️ Left Arrow | Move Left   |

> **Note:** The snake cannot reverse direction directly (e.g., moving right → left instantly is blocked).

---

## 🧠 How It Works

| Module | Responsibility |
|--------|---------------|
| `main.py` | Initializes the screen, creates game objects, runs the game loop |
| `snake.py` | Manages the list of turtle segments, movement, extension, and direction |
| `food.py` | Places a small blue circle at a random (x, y) within the screen bounds |
| `score.py` | Writes the current score to the screen; displays GAME OVER on collision |

---

## 📈 Future Improvements

- [ ] High score persistence (save to file)
- [ ] Difficulty levels (speed increases over time)
- [ ] Sound effects
- [ ] Restart without closing the window
- [ ] Colorful snake with gradient segments

---

## 👤 Author

**Your Name**
- GitHub: https://github.com/RevanthGaraga7

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> *Built as a Python learning project using OOP principles and the Turtle graphics module.*
