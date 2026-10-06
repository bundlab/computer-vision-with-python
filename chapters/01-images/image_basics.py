"""
Chapter 01: Fundamental Digital Image Manipulations
Location: chapters/01-images/image_basics.py

Concepts Covered:
1. Creating synthetic images using NumPy arrays.
2. Inspecting matrix properties (shape, dtype, min/max intensity).
3. Extracting and manipulating BGR color channels.
4. Region of Interest (ROI) cropping and spatial resizing.
5. Saving output images to disk.
"""

import argparse
from pathlib import Path
import cv2
import numpy as np


def inspect_image_properties(image: np.ndarray, label: str = "Image"):
    """Prints fundamental array attributes defining a digital image."""
    print(f"\n--- {label} Properties ---")
    print(f"Dimensions (H x W x C): {image.shape}")
    print(f"Data Type            : {image.dtype}")
    print(f"Intensity Range      : Min = {image.min()}, Max = {image.max()}")


def create_synthetic_canvas(height: int = 300, width: int = 400) -> np.ndarray:
    """
    Generates a 3-channel color image matrix from scratch.
    Digital images in OpenCV are 3D NumPy arrays: (Height, Width, Channels).
    Default memory layout in OpenCV is BGR (Blue, Green, Red).
    """
    canvas = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Fill background with a light neutral color
    canvas[:, :] = [220, 220, 220]  # Light gray in BGR
    
    # Create colored rectangular patches using array slicing
    # Top-left quadrant -> Blue patch
    canvas[20:120, 20:150] = [255, 0, 0]
    
    # Top-right quadrant -> Green patch
    canvas[20:120, 220:370] = [0, 255, 0]
    
    # Bottom center -> Red patch
    canvas[160:260, 120:280] = [0, 0, 255]
    
    return canvas


def split_and_merge_channels(image: np.ndarray):
    """
    Splits a multi-channel BGR image into 3 isolated single-channel matrices.
    Demonstrates zeroing out specific channels to observe color contribution.
    """
    b, g, r = cv2.split(image)
    
    # Create blank single-channel canvas of identical dimensions
    zeros = np.zeros(image.shape[:2], dtype=np.uint8)
    
    # Reconstruct 3-channel representations for visualization
    blue_only = cv2.merge([b, zeros, zeros])   # Isolated Blue channel
    green_only = cv2.merge([zeros, g, zeros])  # Isolated Green channel
    red_only = cv2.merge([zeros, zeros, r])    # Isolated Red channel
    
    return blue_only, green_only, red_only


def extract_roi_and_resize(image: np.ndarray, crop_coords: tuple, target_size: tuple):
    """
    Crops a Region of Interest (ROI) using array indexing: img[y1:y2, x1:x2].
    Resizes the cropped patch using linear interpolation.
    """
    y1, y2, x1, x2 = crop_coords
    roi = image[y1:y2, x1:x2]
    
    # Resize cropped region
    resized_roi = cv2.resize(roi, target_size, interpolation=cv2.INTER_LINEAR)
    return roi, resized_roi


def main():
    parser = argparse.ArgumentParser(description="Chapter 01: Image Basics")
    parser.add_argument("--output", type=str, default="chapters/01-images/output", help="Directory to store outputs")
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=== Chapter 01: Image Basics Execution ===")

    # 1. Generate synthetic image
    img = create_synthetic_canvas()
    inspect_image_properties(img, label="Synthetic Canvas")

    # 2. Channel decomposition
    blue_ch, green_ch, red_ch = split_and_merge_channels(img)

    # 3. ROI Cropping & Resizing
    # Crop the central red box region (y: 150 to 270, x: 110 to 290)
    roi, resized = extract_roi_and_resize(img, crop_coords=(150, 270, 110, 290), target_size=(200, 200))
    inspect_image_properties(roi, label="Cropped ROI Patch")

    # 4. Save results to disk
    cv2.imwrite(str(output_dir / "01_synthetic_canvas.png"), img)
    cv2.imwrite(str(output_dir / "02_channel_blue.png"), blue_ch)
    cv2.imwrite(str(output_dir / "03_channel_green.png"), green_ch)
    cv2.imwrite(str(output_dir / "04_channel_red.png"), red_ch)
    cv2.imwrite(str(output_dir / "05_roi_cropped.png"), roi)
    cv2.imwrite(str(output_dir / "06_roi_resized.png"), resized)

    print(f"\n[Success] Chapter 01 outputs successfully saved to: {output_dir.resolve()}")


if __name__ == "__main__":
    main()