# Vehicle Detection and Counting

A simple OpenCV-based vehicle detection and counting system using frame differencing and contour analysis.

## Features

* Vehicle motion detection
* Vehicle counting
* Bounding box visualization
* Frame skipping for faster processing
* Region of Interest (ROI) analysis

## Requirements

```bash
pip install opencv-python numpy matplotlib
```

## Usage

1. Place the input video in the `data/` directory.
2. Update the video path if needed.
3. Run:

```bash
python main.py
```

## Results

### Sample Image

<p align="center">
  <img src="output/1.png" width="700">
  <img src="output/2.png" width="700">
</p>

### Demo Video

[https://github.com/user-attachments/assets/your-video-link](https://github.com/Alireza-Taherkho/Computer-Vision-Classic-Projects/blob/main/1)%20countung%20vehicles/output/output.mp4)

## Notes

The ROI coordinates and contour thresholds are customized for the provided street video and may require adjustment for other camera views.
