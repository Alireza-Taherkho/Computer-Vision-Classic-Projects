Pong Game with OpenCV

This project implements a simple Pong-style game using OpenCV and classical computer vision. A green object detected by the webcam is used as the player's paddle to bounce the ball.

Features

- Detects a green object in real time using HSV color segmentation.
- Tracks the detected object and uses its position as the paddle.
- Ball movement with wall collisions.
- Score increases when the ball is successfully bounced.
- Ball speed increases as the score reaches predefined values.
- Displays the current score and ball speed.
- Ends the game when the ball reaches the bottom of the screen.

Requirements

- Python
- OpenCV
- NumPy
- A webcam
- A green object for controlling the paddle

Limitations

- Designed to track only one green object.
- Detection depends on lighting conditions and the selected HSV color range.
- A plain background improves detection accuracy.