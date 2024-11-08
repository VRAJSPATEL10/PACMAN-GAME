# PACMAN-GAME

A classic Pacman game implemented in Python using the Turtle graphics library. The game allows the player to control Pacman to collect dots while avoiding ghosts. The player's score is tracked and the highest score is saved.

## Features

- Control Pacman with arrow keys (Up, Down, Left, Right).
- Collect dots to earn points.
- Avoid ghosts to keep the game going.
- Tracks the current score and high score, with high scores stored in `score.txt`.
- Visual feedback for game over and new high scores.

## Game Files

- `Pacman Game.py`: The main game script. Handles the game logic, movement, scoring, and graphics.
- `score.txt`: A text file to store high scores across game sessions.

## Prerequisites

- Python 3.x
- `freegames` library
- `turtle` library (usually included with Python)

## How to Run

1. Install the necessary libraries:
    ```bash
    pip install freegames
    ```

2. Run the game.

## Gameplay

- Use the arrow keys to control Pacman.
- Collect all the dots on the map for points.
- Avoid the ghosts. The game ends if a ghost catches Pacman.
- The current score and high score are displayed on the screen.

## Code Overview

The game is implemented using the following key components:

- **Tiles Array**: Defines the layout of the game board where `1` represents paths with dots, and `0` represents walls.
- **Pacman Movement**: Pacman's movement is controlled by the arrow keys, which change the `aim` vector.
- **Ghosts**: Ghosts move randomly, changing directions at intersections.
- **Score**: The score is incremented whenever Pacman collects a dot. The high score is updated and saved in `score.txt`.
- **Game Over**: When a ghost reaches Pacman, the game ends and a "GAME OVER" message appears on the screen.

## Functions

- `square(x, y)`: Draws a square at position `(x, y)`.
- `offset(point)`: Calculates the tile index for a given point.
- `valid(point)`: Checks if a move is valid.
- `world()`: Draws the game board.
- `move()`: Handles the movement of Pacman and ghosts.
- `change(x, y)`: Updates Pacman's direction.

## Future Enhancements

- Additional levels with different maps.
- Enhanced ghost AI for more challenging gameplay.
- Sound effects and animations.


Enjoy playing Pacman!
