# Invisibility Cloak

## Overview

This project is a simple computer vision implementation of an **invisibility cloak** effect using OpenCV.

A specific color is detected in the image, and the corresponding region is replaced with the background, creating the illusion that the object has disappeared.

> **Note:** This project is based on classic computer vision techniques (color segmentation and image processing). The result depends on lighting conditions, background quality, and the cloak color, so it may not produce perfectly clean outputs in every case.

## Requirements

- Python 3
- OpenCV
- NumPy

```bash
pip install numpy opencv-python
```

## How It Works

1. Load the background and foreground images.
2. Convert the foreground image to HSV color space.
3. Detect the cloak color using color thresholding.
4. Refine the mask with morphological operations.
5. Replace the detected cloak region with the corresponding background.
6. Display and save the final result.