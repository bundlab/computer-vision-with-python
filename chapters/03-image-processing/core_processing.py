"""
Chapter 03: Core Image Processing Techniques
Location: chapters/03-image-processing/core_processing.py

Concepts Covered:
1. Spatial Filtering: Gaussian and Median smoothing.
2. Spatial Gradients & Edges: Sobel operators and Canny Edge Detection.
3. Adaptive Thresholding: Local neighborhood binarization under non-uniform lighting.
4. Morphological Transformations: Dilation, Erosion, Opening, and Closing.
"""

import argparse
from pathlib import Path
import cv2
import numpy as np


def apply_spatial_filtering(image: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Applies Gaussian and Median smoothing filters to reduce high-frequency noise.
    
    Parameters:
        image (np.ndarray): Input 3-channel or grayscale image matrix.
        
    Returns:
        tuple[np.ndarray, np.ndarray]: (Gaussian Blurred image, Median Blurred image)
    """
    # Gaussian Blur with a 5x5 kernel and auto-calculated standard deviation
    gaussian_blurred = cv2.GaussianBlur(image, ksize=(5, 5), sigmaX=0)
    
    # Median Blur with a kernel size of 5 (must be an odd integer)
    median_blurred = cv2.medianBlur(image, ksize=5)
    
    return gaussian_blurred, median_blurred


def extract_edges_and_gradients(gray_image: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Computes spatial derivatives using Sobel filters and detects structural edges via Canny.
    
    Parameters:
        gray_image (np.ndarray): Single-channel grayscale image matrix.
        
    Returns:
        tuple[np.ndarray, np.ndarray]: (Sobel Magnitude image, Canny Edge mask)
    """
    # 1. Compute 1st order derivatives along X and Y direction using 64-bit float to handle negative slopes
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, dx=1, dy=0, ksize=3)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, dx=0, dy=1, ksize=3)
    
    # Calculate gradient magnitude: sqrt(sobel_x^2 + sobel_y^2)
    sobel_magnitude = cv2.magnitude(sobel_x, sobel_y)
    sobel_magnitude = cv2.convertScaleAbs(sobel_magnitude)  # Convert back to uint8
    
    # 2. Apply multi-stage Canny Edge Detection (Lower threshold=50, Upper threshold=150)
    canny_edges = cv2.Canny(gray_image, threshold1=50, threshold2=150)
    
    return sobel_magnitude, canny_edges


def apply_adaptive_thresholding(gray_image: np.ndarray) -> np.ndarray:
    """
    Binarizes image dynamically based on local Gaussian-weighted pixel neighborhoods.
    
    Parameters:
        gray_image (np.ndarray): Grayscale input matrix.
        
    Returns:
        np.ndarray: Binary image (0 or 255).
    """
    binary_adaptive = cv2.adaptiveThreshold(
        gray_image,
        maxValue=255,
        adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        thresholdType=cv2.THRESH_BINARY,
        blockSize=11,  # Size of local pixel neighborhood
        C=2             # Constant subtracted from weighted mean
    )
    return binary_adaptive


def apply_morphology(binary_image: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Applies Morphological Opening (Erosion followed by Dilation) and Closing (Dilation followed by Erosion).
    
    Parameters:
        binary_image (np.ndarray): Single-channel binary image matrix.
        
    Returns:
        tuple[np.ndarray, np.ndarray]: (Opened image, Closed image)
    """
    # Define a 3x3 rectangular structuring element
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    
    # MORPH_OPEN removes small positive noise (isolated white specks)
    opened = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)
    
    # MORPH_CLOSE fills small internal holes within foreground objects
    closed = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
    
    return opened, closed


def main():
    parser = argparse.ArgumentParser(description="Chapter 03: Core Image Processing Execution")
    parser.add_argument("--output", type=str, default="chapters/03-image-processing/output", help="Output directory")
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=== Chapter 03: Core Image Processing Execution ===")

    # Step 1: Create synthetic test background with illumination gradient and shapes
    h, w = 300, 400
    canvas = np.zeros((h, w), dtype=np.uint8)
    
    # Add uneven lighting gradient across background
    x_grid = np.linspace(30, 220, w, dtype=np.uint8)
    canvas[:, :] = x_grid
    
    # Add geometric shapes
    cv2.rectangle(canvas, (40, 50), (160, 220), color=255, thickness=-1)
    cv2.circle(canvas, (280, 140), radius=65, color=0, thickness=-1)
    
    # Inject Gaussian/salt-and-pepper noise pattern
    noise = np.random.randint(0, 50, (h, w), dtype=np.uint8)
    noisy_canvas = cv2.add(canvas, noise)

    # Step 2: Spatial Filtering
    gauss_blur, median_blur = apply_spatial_filtering(noisy_canvas)

    # Step 3: Edge & Gradient Extraction
    sobel_mag, canny_edges = extract_edges_and_gradients(gauss_blur)

    # Step 4: Adaptive Local Thresholding
    binary_adaptive = apply_adaptive_thresholding(gauss_blur)

    # Step 5: Morphological Filtering
    opened, closed = apply_morphology(binary_adaptive)

    # Step 6: Save outputs
    cv2.imwrite(str(output_dir / "01_noisy_input.png"), noisy_canvas)
    cv2.imwrite(str(output_dir / "02_gaussian_blur.png"), gauss_blur)
    cv2.imwrite(str(output_dir / "03_sobel_gradients.png"), sobel_mag)
    cv2.imwrite(str(output_dir / "04_canny_edges.png"), canny_edges)
    cv2.imwrite(str(output_dir / "05_adaptive_threshold.png"), binary_adaptive)
    cv2.imwrite(str(output_dir / "06_morph_opened.png"), opened)

    print(f"\n[Success] Chapter 03 outputs successfully saved to: {output_dir.resolve()}")


if __name__ == "__main__":
    main()