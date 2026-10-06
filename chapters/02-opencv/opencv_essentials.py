"""
Chapter 02: OpenCV Essentials (Drawing, Color Spaces, and Spatial Transformations)
Location: chapters/02-opencv/opencv_essentials.py

Concepts & Theory:
------------------
1. Drawing Primitives:
   OpenCV image coordinates start at (0,0) in the top-left corner.
   Colors are specified as BGR tuples: (Blue, Green, Red) in range 0-255.
   Negative thickness (-1 or cv2.FILLED) generates filled shapes.

2. Color Spaces:
   - BGR: Default storage ordering in OpenCV.
   - HSV: Hue (0-179), Saturation (0-255), Value (0-255). Essential for color segmentation.
   - LAB: Lightness (L), Green-Red (A), Blue-Yellow (B). Perceptually uniform space.

3. Affine Transformations:
   Combines rotation, translation, and uniform scaling using a 2x3 transformation matrix.
   cv2.getRotationMatrix2D computes rotation around an arbitrary origin point (x, y).
   cv2.warpAffine applies the transformation across pixel coordinates using interpolation.
"""

import argparse
from pathlib import Path
import cv2
import numpy as np


def draw_geometric_primitives(canvas: np.ndarray) -> np.ndarray:
    """
    Renders bounding boxes, target markers, diagonal vectors, and text overlays.
    
    Parameters:
        canvas (np.ndarray): Input 3-channel image matrix.
    
    Returns:
        np.ndarray: Modified canvas containing rendered primitives.
    """
    img = canvas.copy()
    h, w = img.shape[:2]

    # 1. Bounding Box (Rectangle)
    # cv2.rectangle(img, pt1, pt2, color, thickness)
    top_left = (int(w * 0.08), int(h * 0.15))
    bottom_right = (int(w * 0.42), int(h * 0.75))
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), thickness=2)

    # Label text overlay on bounding box
    text_origin = (top_left[0], top_left[1] - 8)
    cv2.putText(
        img,
        "Target ROI",
        text_origin,
        cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=0.55,
        color=(0, 255, 0),
        thickness=1,
        lineType=cv2.LINE_AA
    )

    # 2. Target Circle Marker (Filled)
    circle_center = (int(w * 0.72), int(h * 0.35))
    radius = int(min(h, w) * 0.18)
    cv2.circle(img, circle_center, radius, (255, 0, 0), thickness=-1)  # Blue filled circle

    # 3. Vector Line
    cv2.line(img, (0, h), (w, 0), (0, 0, 255), thickness=2)  # Red diagonal vector

    return img


def convert_and_extract_colorspaces(image: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Converts BGR canvas into HSV and CIELAB representations.
    
    Parameters:
        image (np.ndarray): Input image in BGR format.
        
    Returns:
        tuple[np.ndarray, np.ndarray]: (HSV image, LAB image)
    """
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    return hsv_image, lab_image


def rotate_and_scale_image(image: np.ndarray, angle_deg: float = 30.0, scale_factor: float = 0.85) -> np.ndarray:
    """
    Computes a 2D affine rotation matrix around the image center and warps the canvas.
    
    Parameters:
        image (np.ndarray): Input image array.
        angle_deg (float): Counter-clockwise rotation angle in degrees.
        scale_factor (float): Isotropic scaling factor.
        
    Returns:
        np.ndarray: Transformed/rotated image array.
    """
    h, w = image.shape[:2]
    center_pt = (w // 2, h // 2)

    # Generate 2x3 affine matrix: M = [ [alpha, beta, (1-alpha)*x_c - beta*y_c], [-beta, alpha, beta*x_c + (1-alpha)*y_c] ]
    rotation_matrix = cv2.getRotationMatrix2D(center=center_pt, angle=angle_deg, scale=scale_factor)

    # Warp affine transformation across matrix dimensions
    transformed_img = cv2.warpAffine(
        src=image,
        M=rotation_matrix,
        dsize=(w, h),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=(0, 0, 0)
    )

    return transformed_img


def main():
    parser = argparse.ArgumentParser(description="Chapter 02: OpenCV Essentials Execution")
    parser.add_argument("--output", type=str, default="chapters/02-opencv/output", help="Directory for output images")
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=== Chapter 02: OpenCV Essentials Execution ===")

    # Step 1: Base synthetic background
    canvas = np.zeros((300, 400, 3), dtype=np.uint8)
    canvas[:, :] = [45, 45, 45]  # Dark gray surface

    # Step 2: Draw geometric primitives
    annotated = draw_geometric_primitives(canvas)

    # Step 3: Color space transformations
    hsv_img, lab_img = convert_and_extract_colorspaces(annotated)

    # Step 4: Spatial affine transformation
    rotated_img = rotate_and_scale_image(annotated, angle_deg=35.0, scale_factor=0.8)

    # Step 5: Save generated outputs
    cv2.imwrite(str(output_dir / "01_annotated_primitives.png"), annotated)
    cv2.imwrite(str(output_dir / "02_hsv_colorspace.png"), hsv_img)
    cv2.imwrite(str(output_dir / "03_lab_colorspace.png"), lab_img)
    cv2.imwrite(str(output_dir / "04_rotated_affine.png"), rotated_img)

    print(f"\n[Success] Chapter 02 outputs successfully saved to: {output_dir.resolve()}")


if __name__ == "__main__":
    main()