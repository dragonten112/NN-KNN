# NN-KNN Face Recognition
 
A Python implementation of **Nearest Neighbor (NN)** and **K-Nearest Neighbors (KNN)** algorithms for face recognition, applied to the AT&T (ORL) face database.
 
## Overview
 
This project compares NN and KNN classifiers for face recognition across multiple distance metrics and values of k. It evaluates each combination using two metrics: **Recognition Rate (RR)** and **Mean Query Time (TMI)**, then visualizes the results.
 
## Dataset
 
[AT&T Database of Faces (ORL)](https://cam-orl.co.uk/facedatabase.html)
 
- 40 subjects, 10 grayscale images each (112×92 px, `.pgm` format)
- **Training set**: 8 images per person (320 total)
- **Test set**: 2 images per person (80 total)
## Algorithms
 
### Nearest Neighbor (NN)
Finds the single training image closest to the query image using a chosen distance metric. Supports:
- **L1** (Manhattan), **L2** (Euclidean), **L∞** (Chebyshev), **Cosine** similarity
### K-Nearest Neighbors (KNN)
Classifies by majority vote among the k closest training images. Evaluated for:
- `k ∈ {3, 5, 7, 9}` and norms `{L1, L2, L∞, cosine}`
## Metrics
 
| Metric | Description |
|--------|-------------|
| **RR** (Rata de Recunoaștere) | Fraction of test images correctly identified |
| **TMI** (Timp Mediu de Interogare) | Average query time per test image (seconds) |
 
Results are saved to `ORL_8_KNN_RR.txt` and `ORL_8_KNN_TMI.txt` and plotted via the statistics scripts.
 
## Project Structure
 
```
NN-KNN/
└── KNN si NN Statistici/
    ├── Algoritmul NN si KNN.py      # Core NN & KNN implementation + evaluation
    ├── NN Statici Plot.py           # NN results visualization
    ├── KNN Statistici Plot RR.py    # KNN Recognition Rate plots
    ├── KNN Statistici Plot TMI.py   # KNN Mean Query Time plots
    ├── ORL_8_KNN_RR.txt             # Precomputed RR results
    └── ORL_8_KNN_TMI.txt            # Precomputed TMI results
```
 
## Requirements
 
```bash
pip install numpy opencv-python matplotlib
```
 
## Usage
 
1. Download the [AT&T face dataset](https://cam-orl.co.uk/facedatabase.html) and extract it.
2. Update the `caleBD` path in `Algoritmul NN si KNN.py` to point to your dataset folder.
3. Run the main script to train, evaluate, and save results:
```bash
python "Algoritmul NN si KNN.py"
```
 
4. Run the plot scripts to visualize RR and TMI results:
```bash
python "KNN Statistici Plot RR.py"
python "KNN Statistici Plot TMI.py"
python "NN Statici Plot.py"
```
 
## Technologies
 
- **Python 3**
- **NumPy** — matrix operations, norm computations
- **OpenCV** (`cv2`) — image loading and display
- **Matplotlib** — result visualization
## Results
 
The project outputs comparison plots showing how Recognition Rate and Mean Query Time vary across different values of k and distance norms (L1, L2, L∞, cosine), enabling direct comparison of classifier performance.
