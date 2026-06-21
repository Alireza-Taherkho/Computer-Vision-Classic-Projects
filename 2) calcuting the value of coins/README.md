# Coin Detection with OpenCV

This project uses **OpenCV** to detect coins in an image and calculate their total value.

## Steps

1. Read the input image.
2. Convert the image to grayscale.
3. Apply Gaussian Blur.
4. Detect coins using `cv2.HoughCircles()`.
5. Draw circles and display the radius of each coin.
6. Determine the coin value based on its radius.
7. Calculate and display the total value of all detected coins.

## Requirements

```bash
pip install opencv-python numpy matplotlib
```

## Output

* Detected coins highlighted with circles.
* Radius of each detected coin displayed on the image.
* Total value of all detected coins shown on the image.
