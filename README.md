## Machine Learning Methods for Establishing Links Between Symmetries and Physical Properties of Molecular Systems

**Author:** Nikolaou Angeliki  
**Institution:** European University Cyprus, School of Sciences  
**Degree:** Master of Science in Artificial Intelligence  
**Date:** December 2025  

---

## 1. Overview
This repository contains the computational framework developed for the Master's thesis: *"Machine Learning methods for establishing links between symmetries and physical properties of molecular systems"*.

The project implements a pipeline that transforms molecular structures (specifically saturated hydrocarbons and their isomers) into graph-theoretic representations. It extracts spectral and symmetry-based descriptors—such as Perron-Frobenius eigenvalues, Fiedler values, and quotient graph compression ratios—to predict macroscopic physical properties using Kernel Principal Component Analysis (KPCA) and regression models.

## 2. System Requirements
The software has been developed and tested under the following environment specifications:

| Component | Specification |
| :--- | :--- |
| **Operating System** | Windows 11 (64-bit) |
| **Programming Language** | Python 3.13 |
| **Recommended IDE** | PyCharm |
| **Processor** | Minimum: Intel i5 or equivalent |
| **Memory** | Minimum: 8 GB RAM (16 GB recommended for KPCA operations) |
| **Disk Space** | Approx. 500 MB for repository and generated data |

## 3. Installation Procedure
Follow these steps to set up the computational environment

### 3.1 Clone the Repository
Open your terminal or command prompt and run:
```bash
git clone [https://github.com/ScoopySnack/thesis-code-and-analysis.git](https://github.com/ScoopySnack/thesis-code-and-analysis.git)
cd thesis-code-and-analysis
```
### 3.2 Set Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies:
— Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
- Linux:
```bash 
python3 -m venv venv
source venv/bin/activate
```

### 3.3 Install Dependencies
Install the required scientific and machine learning libraries listed in requirements.txt:
```bash
pip install -r requirements.txt
```

#### Key Dependencies:
 - numpy, scipy: Core numerical operations and matrix computations. 
 - pandas: Data handling and preprocessing. 
 - scikit-learn: Machine learning tasks (Kernel transformations, regression). 
 - networkx: Graph generation and manipulation.
 - matplotlib: Visualization of spectral manifolds.

## 4. Repository Structure

The project is organized into modular components to separate raw data, source code, and experimental notebooks :
````
thesis-code-and-analysis/
├── data/
│   ├── raw/               # Original datasets (e.g., Stenutz alkanes)
│   └── processed/         # Cleaned JSON/CSV files with graph descriptors
├── src/
│   ├── graph_gen.py       # Generates Adjacency/Laplacian matrices from chemical formulas
│   ├── descriptors.py     # Calculates Eigenvalues, Entropy, and Compression Ratios
│   ├── kpca_model.py      # KPCA implementation with spectral gap optimization
│   └── preprocessing.py   # Data normalization and cleaning
├── notebooks/             # Reproducible experiments (Figures & Tables)
├── requirements.txt       # Dependency list
└── README.md              # Installation Manual
````

<b>This work is part of a Master's Thesis at European University Cyprus. © December 2025 Nikolaou Angeliki