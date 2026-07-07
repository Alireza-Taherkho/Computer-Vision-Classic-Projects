# Angle Of Deviation Detection

## Overview

This project is a simple computer vision application that estimates a vehicle's **angle of deviation** from the center of the road using OpenCV.

The program detects road lane lines, estimates the road center, calculates the steering deviation angle, and displays a visual warning when the deviation exceeds a threshold.

> **Note:** This is a classic computer vision project based on edge and line detection. It is intended for demonstration purposes and is not designed to work reliably in every driving scenario.

## Requirements

- Python 3
- OpenCV
- NumPy

```bash
pip install numpy opencv-python
```

## How It Works

1. Read frames from a video.
2. Extract the lower region of the frame (road area).
3. Detect lane lines using Canny Edge Detection and Hough Line Transform.
4. Estimate the road center from the detected lane lines.
5. Calculate the angle of deviation between the vehicle and the road center.
6. Display the deviation angle and show a warning if the deviation remains high for several frames.