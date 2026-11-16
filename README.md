# Squid Game – Red Light, Green Light

A Python-based **Red Light, Green Light game** inspired by the popular Squid Game series. The project uses computer vision and real-time motion detection to detect player movements through a webcam.

The game challenges players to reach the finish line during the Green Light phase while remaining completely still during the Red Light phase. Any detected movement during Red Light results in elimination!

## Features

- **Real-Time Motion Detection:** Uses OpenCV to detect player movements through a webcam.
- **Red Light, Green Light Mechanism:** Switches between Red and Green Light phases.
- **Randomized Intervals:** Red Light duration changes randomly to make the game challenging.
- **Countdown Timer:** Displays the remaining game time.
- **Sound Effects:** Includes background music and separate winning and elimination sounds.
- **Game Controls:** Keyboard controls to start, restart, win, or quit the game.
- **Visual Interface:** Custom game screens for introduction, Green Light, Red Light, elimination, and winning.

## Technologies Used

- **Python** – Core programming language
- **OpenCV (cv2)** – Webcam access, image processing, and motion detection
- **NumPy** – Image processing and pixel difference calculations
- **Pygame** – Background music and sound effects
- **OS** – File and directory handling
- **Time** – Countdown timer and game intervals
- **Random** – Randomized Red Light durations


## How to Play

1. Run the Python application.
2. The introductory screen appears with background music.
3. Press **S** to start the game.
4. Move during the Green Light phase.
5. Stop moving when the Red Light phase begins.
6. Movement detected during Red Light results in elimination.
7. Reach the finish before the countdown timer runs out.

### Keyboard Controls

| Key | Action |
|---|---|
| S | Start the game |
| W | Declare victory during Green Light |
| R | Restart the game |
| Q | Quit the game |

## How Motion Detection Works

The project uses OpenCV to detect movement during the Red Light phase:

1. Captures live video frames using the webcam.
2. Converts frames into grayscale images.
3. Applies Gaussian Blur to reduce noise.
4. Calculates the absolute difference between the reference frame and the current frame.
5. Applies thresholding and dilation to highlight movement.
6. Checks the amount of movement within a selected region of interest (ROI).
7. If the detected movement exceeds a predefined threshold, the player is eliminated.

## Requirements

- Python 3.x
- Working webcam
- Microphone is not required.
- Required graphics and audio assets.
- OpenCV, NumPy, and Pygame libraries.

## Future Improvements

- Add multiplayer functionality.
- Introduce multiple difficulty levels.
- Implement player scoring and leaderboards.
- Improve motion detection accuracy.
- Add a graphical settings menu.

## Developed With

Python | OpenCV | NumPy | Pygame

