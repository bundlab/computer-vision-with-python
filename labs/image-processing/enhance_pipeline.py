"""
Lab: Automated Image Processing & Enhancement Pipeline
Location: labs/image-processing/enhance_pipeline.py
"""

import argparse
from pathlib import Path
from typing import Tuple
import cv2
import numpy as np


class ImageProcessor:
    """Core image processing and enhancement pipeline class."""

    def __init__(self, image: np.ndarray):
        """Initialize with a BGR image array."""
        if image is None or image.size == 0:
            raise ValueError("Input image array is empty or invalid.")
        self.original = image.copy()
        self.processed = image.copy()

    def apply_clahe(self, clip_limit: float = 2.0, tile_grid_size: Tuple[int, int] = (8, 8)) -> "ImageProcessor":
        """Enhance local contrast using Adaptive Histogram Equalization (CLAHE)."""
        if len(self.processed.shape) == 3:
            # Convert BGR to LAB color space
            lab = cv2.cvtColor(self.processed, cv2.COLOR_BGR2LAB)
            l, a, b = cv2.split(lab)
            
            # Apply CLAHE to Lightness channel only
            clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
            cl = clahe.apply(l)
            
            # Merge channels back
            limg = cv2.merge((cl, a, b))
            self.processed = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
        else:
            clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
            self.processed = clahe.apply(self.processed)
        return self

    def denoise_bilateral(self, d: int = 9, sigma_color: float = 75.0, sigma_space: float = 75.0) -> "ImageProcessor":
        """Smooth image while preserving sharp edges using Bilateral Filter."""
        self.processed = cv2.bilateralFilter(self.processed, d=d, sigmaColor=sigma_color, sigmaSpace=sigma_space)
        return self

    def extract_edges(self, low_thresh: int = 50, high_thresh: int = 150) -> np.ndarray:
        """Extract edges using Canny edge detector on grayscale conversion."""
        gray = cv2.cvtColor(self.processed, cv2.COLOR_BGR2GRAY) if len(self.processed.shape) == 3 else self.processed
        return cv2.Canny(gray, low_thresh, high_thresh)

    def adaptive_threshold(self, block_size: int = 11, c: int = 2) -> np.ndarray:
        """Apply adaptive thresholding (useful for document cleaning/binarization)."""
        gray = cv2.cvtColor(self.processed, cv2.COLOR_BGR2GRAY) if len(self.processed.shape) == 3 else self.processed
        return cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, c
        )

    def get_result(self) -> np.ndarray:
        """Return current processed image."""
        return self.processed


def create_synthetic_lab_image() -> np.ndarray:
    """Generate a low-contrast synthetic image for testing."""
    img = np.zeros((300, 400, 3), dtype=np.uint8)
    # Gradient low-contrast background
    gradient = np.tile(np.linspace(50, 120, 400, dtype=np.uint8), (300, 1))
    img[:, :, 0] = gradient
    img[:, :, 1] = gradient // 2
    img[:, :, 2] = gradient // 3

    # Add shapes
    cv2.circle(img, (200, 150), 60, (200, 200, 200), -1)
    cv2.putText(img, "LAB TEST", (110, 160), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (30, 30, 30), 2)
    
    # Add Gaussian noise
    noise = np.random.normal(0, 15, img.shape).astype(np.int16)
    noisy_img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    return noisy_img


def process_single_file(input_path: Path, output_dir: Path):
    """Process a single image and export enhanced variations."""
    output_dir.mkdir(parents=True, exist_ok=True)
    img = cv2.imread(str(input_path))
    
    if img is None:
        print(f"[Error] Failed to read {input_path}")
        return

    pipeline = ImageProcessor(img)
    
    # Step 1: Denoise & Enhance Contrast
    enhanced = pipeline.denoise_bilateral().apply_clahe().get_result()
    
    # Step 2: Edge Extraction & Thresholding
    edges = pipeline.extract_edges()
    thresholded = pipeline.adaptive_threshold()

    # Save outputs
    base_name = input_path.stem
    cv2.imwrite(str(output_dir / f"{base_name}_enhanced.png"), enhanced)
    cv2.imwrite(str(output_dir / f"{base_name}_edges.png"), edges)
    cv2.imwrite(str(output_dir / f"{base_name}_binary.png"), thresholded)
    print(f"[Success] Processed and saved results for: {input_path.name}")


def main():
    parser = argparse.ArgumentParser(description="Lab 01: Image Enhancement & Filtering Pipeline")
    parser.add_argument("--input", type=str, help="Path to input image file or directory")
    parser.add_argument("--output", type=str, default="output", help="Output directory for processed images")
    parser.add_argument("--demo", action="store_true", help="Run self-contained synthetic image demo")
    
    args = parser.parse_args()

    if args.demo or not args.input:
        print("Running pipeline demo with synthetic noisy image...")
        output_dir = Path("labs/image-processing/output")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        synthetic_img = create_synthetic_lab_image()
        demo_input_path = output_dir / "sample_input.png"
        cv2.imwrite(str(demo_input_path), synthetic_img)
        
        process_single_file(demo_input_path, output_dir)
        print(f"\nDemo completed successfully. Check output folder: {output_dir.resolve()}")
        return

    input_path = Path(args.input)
    output_dir = Path(args.output)

    if input_path.is_file():
        process_single_file(input_path, output_dir)
    elif input_path.is_dir():
        image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tiff"}
        files = [f for f in input_path.iterdir() if f.suffix.lower() in image_extensions]
        print(f"Found {len(files)} images in directory.")
        for f in files:
            process_single_file(f, output_dir)


if __name__ == "__main__":
    main()
