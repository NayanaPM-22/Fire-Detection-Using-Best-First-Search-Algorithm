# 🔥 Fire Detection Using Best First Search Algorithm

This project implements a **lightweight, vision-based fire detection system** using the **Best First Search (BFS) algorithm** guided by pixel brightness heuristics.  
It is designed for **real-time detection** on **low-resource and edge devices**, avoiding heavy deep learning models while maintaining high sensitivity to fire regions.

---

## 📌 Project Overview

Traditional fire detection systems rely on sensors such as smoke or heat detectors, which may suffer from limited coverage and false alarms.  
This project uses **image processing and heuristic search** to detect fire regions directly from images and GIFs.

The algorithm starts from the **brightest pixel** in an image and expands to neighboring pixels using **Best First Search**, grouping high-intensity regions that are likely to represent fire.

---

## ✨ Key Features

-  Fire detection using **Best First Search (BFS)**
-  Heuristic based on **pixel brightness intensity**
-  Supports **images (JPG, PNG)** and **GIFs**
-  Interactive **Tkinter-based GUI**
-  **Audio alarm** on fire detection
-  Low memory footprint (~300 KB for 224×224 images)
-  Suitable for **edge and embedded systems**

---

## 🏗️ System Architecture

1. **Input Module** – Loads images or GIFs  
2. **Preprocessing** – Grayscale conversion and Gaussian blur  
3. **Detection Engine** – BFS-based fire region detection  
4. **Validation** – Filters small or sparse bright regions  
5. **Alert System** – Triggers audio alarm  
6. **GUI Interface** – Displays original and processed images  

---

## 🔬 Algorithm Used

### Best First Search (BFS)

- Each pixel is treated as a node
- Search starts from the brightest pixel
- Neighboring pixels are expanded based on intensity
- A priority queue ensures high-intensity pixels are explored first

This approach focuses computation only on **fire-like regions**, improving efficiency.

---

## 📊 Results Summary

| Metric | Value |
|------|------|
| Accuracy | 50% |
| Precision (Fire) | 50% |
| Recall (Fire) | 99% |
| F1-Score | 66% |
| Avg Detection Time | ~180 ms |
| Peak Memory Usage | ~295 KB |

> High recall ensures fire incidents are rarely missed, prioritizing safety.

---

## 🧪 Limitations

- False positives in bright non-fire regions
- Fixed brightness threshold
- Works on static frames (no temporal analysis)

---

## 🚀 Future Improvements

- Add color-based heuristics (red/yellow dominance)
- Extend to video stream processing
- Reduce false positives using motion analysis
- Integrate IoT/cloud-based alert systems
- Deploy on Raspberry Pi / Jetson devices

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/NayanaPM-22/Fire-Detection-Using-Best-First-Search-Algorithm
   cd Fire-Detection-Using-Best-First-Search-Algorithm

2. Install required dependencies:
   ```bash
   pip install opencv-python numpy pillow

3. Run the Application:
   ```bash
   python Python\ code.py
4. Select an image or GIF from the GUI to detect fire.

---

## 🛠️ Technologies Used
-  Python
-  OpenCV
-  NumPy
-  Tkinter
-  PIL (Pillow)

---

## 👩‍💻 Authors

-  Nayana Yogeshwari P M

-  Nandeesh Nayak

-  Prajwal Boodihal

-  Yogeesh

Department of Information Technology

National Institute of Technology, Surathkal

---
