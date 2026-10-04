# Digital Image Processing

This repository contains a collection of academic laboratory exercises and practical experiments in the field of Digital Image Processing (DIP). The project is organized by laboratory session and demonstrates how images can be loaded, transformed, enhanced, compressed, visualized, and analyzed using Python-based tools.

The work in this repository is intended for learning and coursework purposes and provides a practical foundation in image processing concepts, image manipulation, and computer vision-related workflows.

## Project Overview

Digital Image Processing is the study of manipulating digital images through mathematical and computational techniques to improve quality, extract useful information, or simplify representation. In this repository, the emphasis is on fundamentals such as:

- image acquisition and loading
- grayscale and color image handling
- resizing and resampling
- spatial reduction and image downsampling
- quantization and color reduction
- simple enhancement techniques
- filtering and denoising concepts
- image analysis using Python libraries

This project is designed to help students understand how raw digital image data can be converted into useful results through programming and experimentation.

## Objectives

The main goals of this repository are to:

- introduce basic concepts of digital image processing
- provide hands-on coding examples using Python
- explore how digital image properties affect processing outcomes
- demonstrate manipulations such as resizing, sampling, and quantization
- expose students to practical image-processing workflows used in computer vision
- build a structured set of lab-based exercises for academic learning

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
│   └── Coursework for Labs 2 and 3
├── Lab-4/
│   └── Yin_Side_Window_Filtering_CVPR_2019_paper_2.pdf
├── Lab-5/
│   └── Additional lab activity or coursework
├── README.md
├── .gitignore
└── LICENSE (if added later)
```

## Lab-by-Lab Description

### Lab 1: Introduction to Digital Image Processing

This is the starting point of the repository and covers the most fundamental DIP operations.

Included in this folder:

- `Lab1_DIP.py` — Python script containing basic image-processing examples
- `Lab1_DIP.ipynb` — notebook version of the same experiments
- sample images such as `RGB_image.jpg`, `GrayScale.jpg`, and `Black&white.jpg`
- `LAB 1.docx` — document containing assignment-related information

Core tasks demonstrated in Lab 1 include:

1. Image Reading
   - Load an image using Python libraries such as Pillow and OpenCV.
   - Understand digital image representation in terms of pixels and color channels.

2. Image Visualization
   - Display an image inside Python for inspection.
   - Understand how image data is rendered visually.

3. Image Resolution
   - Resize an image to different dimensions.
   - Observe how resolution changes affect appearance and file size.

4. Image Sampling
   - Downsample an image by reducing its width and height.
   - Learn how sampling influences detail and quality.

5. Image Quantization
   - Reduce the number of colors used in an image.
   - Explore how lower quantization levels produce simpler, more compressed-looking outputs.

This lab gives students their first practical understanding of how images are represented, modified, and displayed in code.

### Lab (2 & 3)

This folder contains the combined coursework for the second and third laboratory sessions. These exercises likely build upon the concepts introduced in Lab 1 and expand the student’s understanding of image processing operations. The exact content is not fully exposed in the repository naming alone, but the presence of this folder indicates continued applied work on digital image processing topics.

### Lab 4: Research and Filtering Concepts

The `Lab-4` directory includes a PDF titled:

- `Yin_Side_Window_Filtering_CVPR_2019_paper_2.pdf`

This suggests that this lab is focused on filtering, denoising, or advanced image-processing methods in computer vision. The paper likely provides a theoretical basis for side-window filtering approaches, which are relevant in tasks involving noise reduction and edge-preserving image enhancement.

### Lab 5

The `Lab-5` folder contains additional coursework or lab material related to further image-processing concepts. This indicates the progressive structure of the course, where each lab builds upon earlier topics and introduces more advanced tasks.

## Technologies and Libraries Used

This project uses Python as the main programming language and leverages several libraries commonly used in image processing and computer vision:

- Python
- OpenCV (`cv2`)
- NumPy
- Matplotlib
- Pillow (`PIL`)
- Pandas
- Jupyter Notebook

These tools enable image loading, pixel manipulation, filtering, transformation, plotting, and experimentation in a simple and accessible workflow.

## Dependencies

To run the scripts in this repository, install the required packages with:

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
- open the `.ipynb` notebook in Jupyter

Example:

```bash
jupyter notebook
```

### 3. Explore the lab folders

Navigate to the relevant lab folder you want to study or execute and run the script or notebook to reproduce the experiment.

## Example Workflow

A typical workflow from Lab 1 looks like this:

```python
from PIL import Image

# Open an image file
image = Image.open('starryNight.jpg')

# Display the image
image.show()

# Resize the image
resized_image = image.resize((800, 600))
resized_image.save('resized_image.jpg')
```

This demonstrates the core process used in digital image processing:

1. load image
2. process image data
3. display or save the output

## Learning Outcomes

By working through this repository, learners can develop understanding in:

- digital image representation and structure
- image loading and visualization
- resizing and spatial transformation
- color reduction and quantization
- practical image enhancement methods
- basic filtering concepts and denoising ideas
- application of Python in computational imaging tasks

## Notes

This repository is designed for academic and educational use. It reflects a practical course-based approach to understanding image-processing concepts through coding, experimentation, and assignment-based exploration. The resources included in the lab folders are suitable for learning and reviewing image-processing techniques.

## License

This project does not currently include a formal license file. If the repository is to be reused, distributed, or published beyond coursework, adding an appropriate open-source license is recommended.

## Author

This repository was created for digital image processing coursework and laboratory practice.
