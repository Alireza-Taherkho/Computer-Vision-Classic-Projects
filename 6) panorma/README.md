# Panorama Image Stitching with OpenCV

## Overview

This project demonstrates a simple panorama stitching workflow using **OpenCV**.
The program loads multiple panorama images, divides each image into overlapping sections, and stitches those sections together using OpenCV's built-in `Stitcher` module.

The implementation is intended as a basic experiment with image stitching and panorama reconstruction.

---

## Project Structure

```
project/
│
├── data/
│   ├── panorma1.jpg
│   ├── panorma2.jpg
│   ├── ...
│   └── panorma7.jpg
│
├── main.py
└── README.md
```

---

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Matplotlib

Install the required packages:

```bash
pip install opencv-python numpy matplotlib
```

---

## Workflow

The program performs the following main steps:

### 1. Load Images

All panorama images are loaded from the `data/` directory and displayed briefly to verify that they have been read correctly.

### 2. Create Overlapping Sections

Each image is divided into two horizontal sections with a small overlap between them. The overlap helps the stitching algorithm find matching features.

### 3. Stitch Sections

OpenCV's `Stitcher` is used to merge the overlapping sections into a single image.

### 4. Error Handling

The program checks the stitching status and reports common errors such as:

- Not enough matching images
- Homography estimation failure
- Camera parameter adjustment failure

---

## Notes

- The input images should contain sufficient overlapping regions.
- Images are expected to be stored inside the `data/` folder.
- The project uses OpenCV's default stitching pipeline without additional preprocessing or feature engineering.



## License

This project is provided for educational and research purposes.
