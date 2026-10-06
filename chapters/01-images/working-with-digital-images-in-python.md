# Chapter 01: Working with Digital Images in Python

Welcome to **Chapter 01** of the Computer Vision series. Before applying machine learning models or complex filters, you must understand how computers view, process, and manipulate digital images using numerical arrays.

---

## 1. Introduction

To the human eye, an image is a collection of colors, shapes, textures, and semantic objects. To a computer, an image is simply a 2D or 3D numerical matrix containing intensity values.

Computer vision models operate directly on these numerical grids. Understanding digital image representation, color models, bit depth, and NumPy array operations is the foundational prerequisite for all downstream processing tasks—from simple edge detection to complex Vision Transformers.

---

## 2. Aims & Objectives

### **Aims**

To establish a complete foundational understanding of digital image representations and master image manipulation in Python using NumPy, PIL (Pillow), and Matplotlib.

### **Learning Objectives**

* **Understand Image Representation:** Master pixel values, dimensions, channels, bit-depth, and spatial coordinates.
* **Master NumPy Array Manipulations:** Slice, crop, rotate, normalize, and reshape image matrices programmatically.
* **Perform Color Space Conversion:** Understand and translate between RGB, BGR, Grayscale, and HSV spaces.
* **Apply Pixel-Level Transformations:** Execute brightness adjustment, contrast manipulation, and thresholding using direct vector operations.

---

## 3. Types of Digital Images

| Image Type | Channels | Value Range per Pixel | Typical Bit Depth | Primary Use Cases |
| --- | --- | --- | --- | --- |
| **Binary Image** | 1 | `0` (Black) or `1` / `255` (White) | 1-bit or 8-bit | Edge masks, document analysis, segmentation masks |
| **Grayscale Image** | 1 | `0` to `255` | 8-bit (`uint8`) | Classical image processing, feature extraction |
| **RGB Image** | 3 (Red, Green, Blue) | `(0..255, 0..255, 0..255)` | 24-bit total | General web display, deep learning models |
| **RGBA Image** | 4 (RGB + Alpha) | `(0..255, 0..255, 0..255, 0..255)` | 32-bit total | Graphic design, transparent overlays |
| **HSV / HSL Image** | 3 (Hue, Saturation, Value) | Varied (e.g., Hue: `0..180` in OpenCV) | 24-bit total | Color segmentation, object tracking under lighting changes |

---

## 4. Key Concept Checklist

1. **Spatial Representation:** Coordinates in image matrices are indexed as `[row, column]` or `[y, x]`, where `(0, 0)` is the **top-left** corner.
2. **Channel Ordering:** PIL, Matplotlib, and PyTorch expect **RGB**, while OpenCV reads images in **BGR** format by default.
3. **Data Types:** Images are almost always represented as 8-bit unsigned integers (`np.uint8`). When performing mathematical computations, convert to `np.float32` first to avoid overflow or underflow bugs, then clip back to `[0, 255]`.

---

## 5. Conclusion

In this chapter, you learned:

* How computers encode images into 2D and 3D numerical matrices.
* The structure and properties of binary, grayscale, RGB, and HSV image formats.
* How to manipulate pixel values programmatically using vectorized NumPy operations.
* Practical conversions between color channels and brightness adjustment formulas.

---