# 🚀 Alien Invasion

A fast-paced arcade shooter built with **Python** and **Pygame**. Pilot your ship, fire bullets at incoming alien fleets, and aim for the highest score. The game features a dynamic scoreboard, responsive controls, and a modular codebase for easy extension.

!Alien Invasion Banner <!-- Optional: add a banner image -->

---

## ✨ Features

- **Arcade shooter gameplay**: Move your ship and fire bullets at alien waves.
- **Scoreboard & High Score**: Track your current score and best record.
- **Game States**: Start, active gameplay, pause, and game over.
- **Scalable Difficulty**: Speed increases and wave density ramp up over time.
- **Modular Architecture**: Clean separation of concerns (aliens, bullets, ship, settings, UI buttons).
- **Keyboard Controls**: Smooth movement and shooting.
- **Cross-platform**: Runs on Windows, macOS, and Linux with Python + Pygame.

> Note: Pygame primarily renders in 2D; this project emulates a “3D feel” via sprites, scaling, and motion.

---

🧠 How It Works (Architecture Overview)

alien_invasion.py: Initializes the game, handles the main loop, events, updates, and drawing.
settings.py: Centralized constants and dynamic scaling for difficulty progression.
ship.py: Player ship sprite; movement and rendering.
bullet.py: Bullet sprite; fired from the ship, checks collisions with aliens.
alien.py: Alien sprite; fleet creation, movement patterns, and edge detection.
game_states.py: Encapsulates gameplay states (menu/active/pause/game-over).
scoreboard.py: Displays current score, high score, and level; can persist high score to a file (optional).
button.py: Simple, clickable UI components (Play, Restart, etc.).


🏆 Score & Persistence

Current score increases when aliens are destroyed.
High score can be saved to highscore.txt (if implemented).
To enable persistence, ensure scoreboard.py reads/writes from a file.


📦 Assets
Place your images and sounds in assets/:
assets/
├─ images/
│  ├─ ship.png
│  ├─ alien.png
│  └─ background.png
└─ sounds/
   ├─ shoot.wav
   └─ explosion.wav

Update loading paths in ship.py, alien.py, or wherever you load assets.
If assets are missing, fallback to simple shapes/colors.

🧪 Development Tips

Run with the terminal open to see logs or errors.
Use settings.py to cap bullet count and tweak speeds.
Separate collision logic in bullet.py to simplify testing.

## 🧱 Project Structure
