# Fall Warning Alarm

## Overview

This project is a simple fall warning system built with OpenCV and a Support Vector Machine (SVM).

The program detects motion between consecutive video frames, tracks the vertical position of the detected object, and uses a trained SVM model to determine whether a falling event has occurred.

> **Note:** This project is intended as a simple demonstration and is trained on a small manually created dataset. It is not designed for real-world fall detection.

## Requirements

- Python 3
- OpenCV
- NumPy
- scikit-learn

```bash
pip install numpy opencv-python scikit-learn
```

## Files

- **train.ipynb** – Creates and trains the SVM model, then saves it as `model1.pkl`.
- **main.py** – Loads the trained model, processes a video, and displays a "Falling" warning when a fall is detected.

## How It Works

1. Train an SVM model using sample data.
2. Load the trained model.
3. Detect motion between consecutive video frames.
4. Track the object's vertical movement.
5. Predict whether the movement represents a fall.
6. Display a warning if a fall is detected.