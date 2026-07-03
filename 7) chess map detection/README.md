# Chessboard Coordinate Detection

## Overview

This project detects the corner points of a chessboard using OpenCV and labels the board with standard chess coordinates (`a8` to `h1`).

> **Note:** This code is **specialized for a specific input image**. It is not designed to work reliably with arbitrary chessboard images without modifying the parameters.

## Requirements

- Python 3
- NumPy
- OpenCV

```bash
pip install numpy opencv-python
```

## How It Works

1. Load and resize the image.
2. Convert it to grayscale and apply Gaussian blur.
3. Detect chessboard corners using `goodFeaturesToTrack()`.
4. Sort the detected corners into the correct order.
5. Assign chess coordinates to each square.
6. Draw the coordinates and save the output image.

## Output

The program displays the labeled chessboard and saves the result as:

```
result/chess.png
```

## Technologies

- Python
- OpenCV
- NumPy