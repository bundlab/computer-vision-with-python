#!/usr/bin/env python3
"""
Computer Vision Suite Master Runner
Location: run_cv.py
"""

import sys
import os
import subprocess

MODULE_MAP = {
    "ch1": "chapters/01-images/image_basics.py",
    "ch2": "chapters/02-opencv/opencv_essentials.py",
    "ch3": "chapters/03-image-processing/core_processing.py",
    "lab-img": "labs/image-processing/enhance_pipeline.py",
}

def print_help():
    print("""
Computer Vision Suite Runner
============================
Usage:
  ./run_cv.py [target] [options]

Available Targets:
  ch1       : Chapter 01 - Basic Digital Image Manipulations
  lab-img   : Lab - Automated Image Enhancement & Filtering Pipeline

Examples:
  ./run_cv.py ch1
  ./run_cv.py lab-img --demo
  ./run_cv.py lab-img --input my_photo.jpg --output results
""")

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ["-h", "--help", "help"]:
        print_help()
        sys.exit(0)

    target = sys.argv[1].lower()
    extra_args = sys.argv[2:]

    if target not in MODULE_MAP:
        print(f"[Error] Unknown target '{target}'.")
        print_help()
        sys.exit(1)

    script_path = MODULE_MAP[target]
    if not os.path.exists(script_path):
        print(f"[Error] Target script not found at path: {script_path}")
        sys.exit(1)

    cmd_str = " ".join([sys.executable, script_path] + extra_args)
    print(f"==> Executing: {cmd_str}\n")
    try:
        res = subprocess.run([sys.executable, script_path] + extra_args)
        sys.exit(res.returncode)
    except Exception as e:
        print(f"[Error] Execution failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()