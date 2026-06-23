# Arrow Direction Detection with OpenCV

This project detects the direction of a single arrow in an image using classical computer vision techniques in OpenCV.

## Process

* Convert image to grayscale and apply Gaussian Blur.
* Detect edges and contours.
* Extract corner points using Shi-Tomasi Corner Detection.
* Estimate the arrow center from its contour.
* Find the arrow tip using geometric analysis of corner points.
* Compute the arrow angle and classify its direction as:

  * UP
  * DOWN
  * LEFT
  * RIGHT

## Limitations

* Designed to detect **only one arrow** per image.
* Performance degrades on **noisy images**.
* Works best when the **background is smooth and simple**.
* The arrow should have **sharp and well-defined corners**.
* Accuracy may decrease for distorted, blurred, or partially occluded arrows.
