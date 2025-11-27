# 🚀 Alien Invasion (Space-Invaders Style Arcade Game)
*Built using Pygame, learned and developed from the Python Crash Course book*

---

## 🎮 About the Game  
Alien Invasion is a classic **arcade shooter game** inspired by **Space Invaders**.  
The player controls a **spaceship at the bottom of the screen**, fires **bullets to destroy descending aliens**, and has **3 lives (3 ships) before game over**.

Each time you destroy an entire fleet of aliens, the **level increases**, and your goal is to **beat the high score**!

---

## ✨ Features  
- Player spaceship movement (Left & Right)  
- Bullet firing using spacebar  
- 3 chances before game over  
- Level upgrade after every alien fleet destroyed  
- High Score tracking (doesn’t reset after restarting the game)  
- Background space-arcade theme  

---

## 🕹️ How to Play  
| Control Key | Action |
|-----------|--------|
| `←  →` Arrow Keys | Move Ship |
| `SPACE` | Fire Bullet |
| Destroy all aliens | Level Up |
| Lose all 3 ships | Game Over |

---

## 🔊 Background Music  
The game includes looping background music (`lightyear.ogg`) for a smooth arcade experience.  
The music **automatically stops when the player loses all 3 ships**.

---

## ▶️ Run the Game  
Make sure you have Python and Pygame installed, then run:

```bash
python alien_invasion.py

⚙️ Requirements

- Python 3.x

- Pygame

Install Pygame using:
pip install pygame


📂 Project Structure
alien-invasion-game/
│── alien_invasion.py
│── game_functions.py
│── settings.py
│── game_stats.py
│── scoreboard.py
├──  lightyear.ogg (background music)
│
├── images/
│     └── alien.png  (sprite image)
│     └── ship.png   
│
└── README.md


💡 Learning Source

This project was built while learning from the Python Crash Course book.
It reflects my hands-on practice in game development using Pygame.


🏆 Goal

✅ Understand Pygame sprite handling
✅ Work with rectangles (get_rect()) for positioning
✅ Implement bullet movement and deletion
✅ High score persistence
✅ Game loop and event handling


⭐ If you like this project, don’t forget to star the repo!
