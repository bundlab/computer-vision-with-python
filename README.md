# Computer Vision with Python

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-ee4c2c.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome to the **Computer Vision with Python** repository! This project serves as an end-to-end curriculum and resource hub designed to guide you from foundational digital image processing to cutting-edge deep learning architectures like Vision Transformers (ViTs).

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Repository Structure](#-repository-structure)
- [Curriculum Modules](#-curriculum-modules)
  - [Chapters](# chapters)
  - [Hands-on Labs](# hands-on-labs)
  - [Capstones & Projects](# capstones--projects)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#-usage)
- [Contributing](#-contributing)
- [License](#-license)

---

## 👁️ Overview

Computer Vision (CV) is one of the most rapidly evolving fields in modern Artificial Intelligence. This repository offers a structured hands-on learning path including:
* **Core Concepts:** Understanding pixel manipulation, color spaces, transformations, and filters.
* **Classical CV:** Mastering traditional algorithms using OpenCV.
* **Deep Learning for Vision:** Convolutional Neural Networks (CNNs) and Vision Transformers (ViT) using PyTorch and TensorFlow.
* **Practical Applications:** Practical lab exercises and real-world projects solving industry problems.

---

## 📁 Repository Structure

```text
computer-vision-with-python/
├── README.md
├── chapters/
│   ├── 01-images/
│   ├── 02-opencv/
│   ├── 03-image-processing/
│   ├── 04-image-classification/
│   ├── 05-object-detection/
│   ├── 06-image-segmentation/
│   ├── 07-ocr/
│   └── 08-vision-transformers/
│
├── labs/
│   ├── image-processing/
│   ├── face-detection/
│   ├── object-detection/
│   └── ocr/
│
└── projects/
    ├── plant-disease-detection/
    ├── traffic-sign-detection/
    └── waste-classification/
```

---

## 📚 Curriculum Modules

### Chapters

| Module | Title | Key Topics Covered | Link |
| :--- | :--- | :--- | :---: |
| **01** | **Images Basics** | Digital image representation, matrices, channels, color spaces (RGB, HSV, Grayscale) | [Explore](./chapters/01-images/) |
| **02** | **OpenCV Fundamentals** | Drawing, geometric transformations, video streams, event handling | [Explore](./chapters/02-opencv/) |
| **03** | **Image Processing** | Filtering, blurring, edge detection (Canny, Sobel), contours, thresholding | [Explore](./chapters/03-image-processing/) |
| **04** | **Image Classification** | CNN architectures, feature extraction, PyTorch/TensorFlow models | [Explore](./chapters/04-image-classification/) |
| **05** | **Object Detection** | Bounding boxes, Anchor boxes, YOLO, SSD, Faster R-CNN, IoU & NMS | [Explore](./chapters/05-object-detection/) |
| **06** | **Image Segmentation** | Semantic vs Instance segmentation, U-Net, Mask R-CNN | [Explore](./chapters/06-image-segmentation/) |
| **07** | **Optical Character Recognition (OCR)** | Text detection, Tesseract, EasyOCR, document parsing pipelines | [Explore](./chapters/07-ocr/) |
| **08** | **Vision Transformers** | Self-attention in vision, ViT architecture, Fine-tuning ViT models | [Explore](./chapters/08-vision-transformers/) |

---

### Hands-on Labs

Focused mini-labs designed to build practical intuition for standalone vision tasks.

* 🧪 [**Image Processing Lab**](./labs/image-processing/): Filtering, morphology, noise reduction, and histogram equalization techniques.
* 🧪 [**Face Detection Lab**](./labs/face-detection/): Building real-time face detection using Haar Cascades and DNN-based detectors.
* 🧪 [**Object Detection Lab**](./labs/object-detection/): Real-time target tracking and custom object detection implementation.
* 🧪 [**OCR Lab**](./labs/ocr/): Building an end-to-end text extraction tool for invoices and receipts.

---

### Capstones & Projects

Full-scale end-to-end projects demonstrating real-world applications of vision algorithms.

* 🌿 [**Plant Disease Detection**](./projects/plant-disease-detection/): Multi-class leaf classification using transfer learning to assist precision agriculture.
* 🚦 [**Traffic Sign Detection**](./projects/traffic-sign-detection/): Real-time road sign classification for autonomous vehicle systems.
* ♻️ [**Waste Classification**](./projects/waste-classification/): Automated waste sorting system using image classification to streamline recycling.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8 or higher installed on your machine.

* Python 3.8+
* `pip` package manager
* Virtual environment tool (`venv` or `conda`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/computer-vision-with-python.git
   cd computer-vision-with-python
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

Navigate into any specific chapter, lab, or project directory to run the code snippets or Jupyter notebooks:

```bash
# Example: Running the face detection lab
cd labs/face-detection
python detect_faces.py
```

Or start a Jupyter Notebook server to explore the chapters interactively:

```bash
jupyter notebook
```

---

## 🤝 Contributing

Contributions are welcome! If you find bugs, have improvements, or want to add a new project:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AwesomeFeature`)
3. Commit your Changes (`git commit -m 'Add some AwesomeFeature'`)
4. Push to the Branch (`git checkout -b feature/AwesomeFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.