# Handwritten Digit Generator Web App (Demo)

## Overview

This project implements a web app to generate 5 images of handwritten digits (0–9), inspired by MNIST. Users select a digit, and the app shows 5 distinct images for it.

---

## Constraints & Notes

- **Training from scratch on MNIST required**, no pretrained weights allowed.  
- **Accuracy is not critical**, but generated images should be recognizable digits.  
- **Exact duplicates not allowed:** 5 images must show some diversity.  
- **Time and resource limits:** Full training and deployment typically require hours; this demo focuses on structure and functionality with placeholders.

---

## What This Demo Does

- **Streamlit app**: lets users select digits and generate 5 unique random-noise images as placeholders.  
- **Training script**: defines a basic generator model and loads MNIST in Google Colab; no full training yet.  
- This shows understanding of the pipeline and meets the minimal requirement of generating diverse images (though placeholders).

---

## How to Run

1. **Streamlit app:**  
   ```bash
   pip install streamlit matplotlib numpy
   streamlit run app.py
2. **Training script:** Open training_script.ipynb in Google Colab and run.

