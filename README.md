# 👾 Alien Invasion (Pygame)

A classic Space Invaders-style vintage game built with Python and Pygame.  
Control a spaceship, shoot down alien fleets, and survive as long as possible while the difficulty increases over time.

---

## 🎮 Features

- Player-controlled spaceship (left/right movement)
- Shooting bullets to destroy aliens
- Increasing difficulty as levels progress
- Score tracking + high score system
- Lives system (game over after losing all ships)
- Play button to restart the game
- Dynamic alien fleet generation and movement

---

## 🧱 Project Structure

├── alien_invasion.py # Main game loop (entry point)
├── settings.py # Game configuration (speed, colors, etc.)
├── game_stats.py # Tracks score, level, ships left
├── scoreboard.py # Displays score, level, high score
├── ship.py # Player ship logic
├── alien.py # Alien behavior
├── bullet.py # Bullet mechanics
├── button.py # Start button UI
└── README.md

---

## 🚀 How to Run

### 1. Install dependencies

Make sure you have Python 3.6+ installed.

Install pygame:
```bash
pip install pygame

python alien_invasion.py
