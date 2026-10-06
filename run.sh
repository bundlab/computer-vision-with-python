#!/usr/bin/env bash
set -e

SHOW_HELP() {
    echo "Computer Vision Repository CLI Launcher"
    echo "====================================="
    echo "Usage: ./run.sh <target> [args...]"
    echo ""
    echo "Available Targets:"
    echo "  ch1       Execute Chapter 01 (Image Basics)"
    echo "  ch2       Execute Chapter 02 (OpenCV Essentials)"
    echo "  ch3       Execute Chapter 03 (Image Processing)"
    echo "  lab-img   Execute Image Processing Lab"
    echo ""
    echo "Examples:"
    echo "  ./run.sh ch1"
    echo "  ./run.sh ch2"
    echo "  ./run.sh ch3"
    echo "  ./run.sh lab-img --demo"
}

if [ "$#" -eq 0 ] || [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
    SHOW_HELP
    exit 0
fi

python3 run_cv.py "$@"