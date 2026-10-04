# Digital Image Processing

This repository contains a collection of academic exercises, assignments, and practical experiments focused on digital image processing. The work is organized by laboratory session and includes Python scripts, Jupyter notebooks, sample images, and supporting research material. The goal is to understand how digital images are represented, manipulated, transformed, filtered, and interpreted using computational techniques.

## Overview

Digital Image Processing (DIP) is the field of applying signal-processing methods to images to improve their quality, extract meaningful information, or prepare them for analysis. In this repository, the emphasis is on learning foundational DIP operations such as:

- reading and displaying images
- resizing and resampling
- grayscale conversion
- color-space understanding
- basic image enhancement
- image quantization
- filtering and denoising concepts
- practical experimentation using Python and OpenCV

The repository is intended for educational use and demonstrates how image-processing tasks can be implemented using Python-based tools and libraries.

## Repository Structure

```text
Digital-Image-Processing/
├── Lab-1/
│   ├── Lab1_DIP.py
│   ├── Lab1_DIP.ipynb
│   ├── RGB_image.jpg
│   ├── GrayScale.jpg
│   ├── Black&white.jpg
│   └── LAB 1.docx
├── Lab-(2&3)/
│   └── Combined coursework for Labs 2 and 3
├── Lab-4/
│   └── Yin_Side_Window_Filtering_CVPR_2019_paper_2.pdf
├── Lab-5/
│   └── Additional lab activity
├── README.md
└── .gitignore
```

## Laboratory Breakdown

### Lab 1: Introduction to Digital Image Processing

This is the foundational lab in the repository. It contains practical examples related to:

- reading an image from disk
- visualizing the image in Python
- resizing an image to a new resolution
- downsampling or reducing spatial resolution
- image quantization for reducing color levels
- understanding the visual effect of compression-like operations

The script `Lab-1/Lab1_DIP.py` demonstrates several basic DIP operations. It uses Python libraries such as:

- Pillow (PIL)
- OpenCV
- NumPy
- Matplotlib

The notebook `Lab1_DIP.ipynb` provides an interactive version of the same work in a Jupyter environment.

Key exercises in Lab 1 include:

1. Image Reading and Display
   - Load an image file using Pillow and OpenCV
   - Display it in a Python environment

2. Image Resolution
   - Resize the image to a custom width and height
   - Analyze how resolution changes affect appearance and size

3. Image Sampling
   - Reduce image resolution by a given factor
   - Understand how downsampling affects detail and quality

4. Image Quantization
   - Reduce the number of colors in an image
   - Explore how fewer color levels affect image representation

This lab gives the basic intuition behind image representation and transformation in digital systems.

### Lab (2 & 3)

This folder contains the coursework for the second and third lab sessions. These labs likely build on the fundamentals from Lab 1 and explore more advanced or intermediate image-processing topics. The exact content may vary depending on the course structure, but the overall focus is on expanding practical understanding of image manipulation, processing workflows, and visual experimentation.

### Lab 4: Filtering and Research Study

The `Lab-4` folder includes a research paper titled:

- `Yin_Side_Window_Filtering_CVPR_2019_paper_2.pdf`

This suggests the lab is associated with image filtering, denoising, or side-window filtering approaches in computer vision. The paper likely provides theoretical and practical context for advanced filtering techniques used in image enhancement and restoration.

### Lab 5

The `Lab-5` folder contains additional coursework or exercises, likely continuing the progression of digital image processing topics introduced in earlier labs.

## Tools and Libraries

This project primarily relies on the following technologies:

- Python
- OpenCV (`cv2`)
- NumPy
- Matplotlib
- Pillow (`PIL`)
- Jupyter Notebook

These tools are widely used in digital image processing because they support image loading, pixel manipulation, transformations, visualization, and experimentation.

## Dependencies

To run the scripts in this repository, you may need to install the following packages:

```bash
pip install numpy matplotlib opencv-python pillow pandas jupyter
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/husnainahmed971/Digital-Image-Processing.git
cd Digital-Image-Processing
```

### 2. Open the project in a Python environment

You can either:

- run the `.py` scripts directly, or
- open the `.ipynb` notebook with Jupyter

Example:

```bash
jupyter notebook
```

### 3. Navigate through the lab folders

Open the relevant folder for your assignment, then run the script or notebook to reproduce the image-processing steps.

## Example Workflow

A sample workflow from Lab 1 is:

```python
from PIL import Image

image = Image.open('starryNight.jpg')
image.show()

resized_image = image.resize((800, 600))
resized_image.save('resized_image.jpg')
```

This demonstrates the basic flow:

1. load image
2. process it
3. save or display output

## Learning Goals

This repository is designed to help students and learners understand:

- how images are represented digitally
- how pixel data can be manipulated
- how resizing, quantization, and sampling affect image quality
- how filtering concepts support enhancement and restoration
- how Python can be used for practical image-processing workflows

## Notes

This repository is intended for academic and educational use. It reflects coursework and experiment-based learning in the field of digital image processing. Some folders contain assignment material, research papers, and image assets used during lab work.

## License

This project does not currently contain a formal license file. If you plan to publish, reuse, or distribute the project beyond coursework, consider adding an appropriate open-source license.

## Author

This repository was created for digital image processing coursework and laboratory practice.
