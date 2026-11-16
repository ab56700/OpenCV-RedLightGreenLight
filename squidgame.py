import cv2
import os
import numpy as np
import time
import pygame
import random

# Initialize pygame for sounds
pygame.mixer.init()

# Load sounds
def play_sound(file, loop=False):
    sound = pygame.mixer.Sound(file)
    sound.play()

# Load frames and graphics
def load_graphics():
    folderPath = 'frames'
    mylist = sorted(os.listdir(folderPath))  # Ensure correct order
    return [cv2.imread(f'{folderPath}/{imPath}') for imPath in mylist]

# The main Squid Game function
def squid_game():
    # Load frames
    graphic = load_graphics()
    green = graphic[0]
    red = graphic[1]
    kill = graphic[2]
    winner = graphic[3]
    intro = graphic[4]

    # Play the squid song continuously before starting the game
    pygame.mixer.music.load('sounds/squidsong.mp3')
    pygame.mixer.music.play(loops=-1)  # Loop indefinitely before starting
    while True:
        cv2.imshow('Squid Game', cv2.resize(intro, (0, 0), fx=1, fy=1))
        key = cv2.waitKey(10) & 0xFF
        if key == ord('s'):  # Start the game when 's' is pressed
            pygame.mixer.music.stop()  # Stop the squid song once game starts
            break
        if key == ord('q'):  # Quit the game if 'q' is pressed
            pygame.mixer.music.stop()  # Stop the squid song when quitting
            return "quit"

    # Initialize variables
    TIMER_MAX = 60  # Increased timer to 3 minutes (180 seconds)
    TIMER = TIMER_MAX
    maxMove = 3000000  # Adjusted sensitivity
    font = cv2.FONT_HERSHEY_SIMPLEX
    cap = cv2.VideoCapture(0)

    win = False
    prev = time.time()
    isgreen = True
    showFrame = cv2.resize(green, (0, 0), fx=1, fy=1)

    # Randomize interval for changing frames
    frame_change_interval = 5  # Start with 5 seconds for green light
    last_change_time = time.time()

    # Play RLGLsong.mp3 for green frame
    pygame.mixer.music.load('sounds/RLGLsong.mp3')
    pygame.mixer.music.play(loops=-1)  # Loop during green frame

    # Game loop
    while cap.isOpened() and TIMER >= 0:
        ret, frame = cap.read()
        if not ret:
            break

        # Check key inputs
        key = cv2.waitKey(10) & 0xFF
        if key == ord('w') and isgreen:  # Win during green light
            win = True
            break
        if key == ord('r'):  # Restart
            return "restart"
        if key == ord('q'):  # Quit
            return "quit"

        # Timer display adjustments
        timer_text = str(TIMER)
        if TIMER > 100:
            font_scale = 1.5
        elif TIMER > 50:
            font_scale = 1.2
        else:
            font_scale = 1
        thickness = 4
        text_size = cv2.getTextSize(timer_text, font, font_scale, thickness)[0]
        text_width = text_size[0]
        text_height = text_size[1]
        text_x = 50
        text_y = 50 + text_height

        # Draw a solid rectangle to clear the timer text area
        cv2.rectangle(
            showFrame,
            (text_x - 10, text_y - text_height - 10),
            (text_x + text_width + 10, text_y + 10),
            (0, 0, 0),  # Black rectangle
            -1
        )

        # Draw the updated timer text
        cv2.putText(
            showFrame,
            timer_text,
            (text_x, text_y),
            font,
            font_scale,
            (0, int(255 * TIMER / TIMER_MAX), int(255 * (TIMER_MAX - TIMER) / TIMER_MAX)),
            thickness,
            cv2.LINE_AA
        )       

        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER -= 1

        # Frame change logic
        if cur - last_change_time >= frame_change_interval:
            if isgreen:
                # Switch to red frame
                showFrame = cv2.resize(red, (0, 0), fx=1, fy=1)
                isgreen = False
                ref = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                ref = cv2.GaussianBlur(ref, (11, 11), 0)
                frame_change_interval = random.randint(3, 6)  # Red light random between 3-6 seconds
                pygame.mixer.music.stop()  # Stop RLGLsong.mp3
            else:
                # Switch to green frame
                showFrame = cv2.resize(green, (0, 0), fx=1, fy=1)
                isgreen = True
                frame_change_interval = 5  # Green light fixed for 5 seconds
                pygame.mixer.music.load('sounds/RLGLsong.mp3')
                pygame.mixer.music.play(loops=-1)  # Play RLGLsong.mp3 again

            # Update the last change time
            last_change_time = cur

        if not isgreen:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (11, 11), 0)
            frameDelta = cv2.absdiff(ref, gray)
            thresh = cv2.threshold(frameDelta, 20, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)
            h, w = thresh.shape
            roi = thresh[int(h / 4):int(3 * h / 4), int(w / 4):int(3 * w / 4)]
            change = np.sum(roi)
            if change > maxMove:
                break

        camShow = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        camH, camW = camShow.shape[0], camShow.shape[1]
        showFrame[0:camH, -camW:] = camShow
        cv2.imshow('Squid Game', showFrame)

    cap.release()
    if not win:
        play_sound('sounds/kill.mp3')
        for _ in range(10):
            cv2.imshow('Squid Game', cv2.resize(kill, (0, 0), fx=1, fy=1))
        pygame.mixer.music.stop()
        while True:
            key = cv2.waitKey(10) & 0xFF
            if key == ord('r'):
                return "restart"
            if key == ord('q'):
                return "quit"
    else:
        play_sound('sounds/win.mp3')
        cv2.imshow('Squid Game', cv2.resize(winner, (0, 0), fx=1, fy=1))
        cv2.waitKey(125)
        pygame.mixer.music.stop()
        while True:
            key = cv2.waitKey(10) & 0xFF
            if key == ord('r'):
                return "restart"
            if key == ord('q'):
                return "quit"

    cv2.destroyAllWindows()

# Main Program Loop #Thank You Beyonce
while True:
    result = squid_game()
    if result == "quit":
        break

