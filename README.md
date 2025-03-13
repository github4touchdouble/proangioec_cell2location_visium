![Welcome](https://github.com/user-attachments/assets/691aa3ec-b420-4ce6-ad26-b637c7683f3e)

# Spatial Deconvolution of Pro-Angiogenic Endothelial Cells in Human Atherosclerotic Plaques
> [!NOTE]
> For further insights, refer to the corresponding paper accessible [here](https://drive.google.com/file/d/1FXrZSJqAV4TvRap4WQRqJCcdH-wUs99j/view?usp=sharing).

T. Truc Bui, Max-Malte Hansen, Jan P. Hummel, Julius J. Stein, Korbinian Traeuble 

Technical University of Munich & Helmholtz Munich

Contact via: [jan.hummel@tum.de](mailto:jan.hummel@tum.de)
---

## Overview  
We mapped endothelial cell subtypes using **Visium spatial transcriptomics** and **Cell2Location**, with a focus on **pro-angiogenic endothelial cells**. By integrating **single-cell RNA sequencing (scRNA-seq)**, we enhanced spatial resolution to uncover their **distribution, function, and role in angiogenesis** within tissue microenvironments.  


## Setting Up the Local Python Environment

### 1. Create a Virtual Environment
First, create a virtual environment using `venv`:

```sh
python -m venv venv
```

### 2. Activate the Virtual Environment
- **Windows (cmd/PowerShell):**
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux:** (currently no model training with mps)
  ```sh
  source venv/bin/activate
  ```

### 3. Install Dependencies
Once the virtual environment is activated, install the required dependencies:

```sh
pip install -r requirements.txt
```

### 4. Create a `.env` File
In the root directory of the project, create a `.env` file and copy-paste the following contents into it:

```
# Example .env file
PATH_TO_SCATLAS=/PATH/TO/PLAQUE/ATLAS.h5ad
PATH_TO_VISIUM=/PATH/TO/VISUM/SLIDES.h5ad
PATH_TO_ATLAS_MODEL2WO=./
PATH_TO_MAP_MODEL2WO_N5=./
PATH_TO_MAP_MODEL2WO_N7=./
PATH_TO_MAP_MODEL2WO_N10=./
```

### 5. Verify Setup
Ensure everything is installed correctly by running:

```sh
python -m pip check
```

## Usage of compare_plots.py
Script to create a diff of 3 plots with different hyperparameters [specifically cells per location]. Make sure, the plots have the same dimensions.

To run the script:
```sh
python3 compare_plots.py plot1.png plot2.png plot3.png [output.png]
```

### Arguments:
plot1: Path to the first plot image file. \
plot2: Path to the second plot image file. \
plot3: Path to the third plot image file. \
--output: Path to save the output comparison image (optional)

### Example
```sh
python3 compare_plots.py n5.png n7.png n10.png -o diff_ncells_5_7_10.png
```
#### Example output
![Output](https://github.com/user-attachments/assets/e6237cdf-c1c6-477d-a229-453649067843)

# Data and Material
Visium Data: Bleckwehl et al. (2024)  [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14007461.svg)](https://doi.org/10.5281/zenodo.14007461) \
Cell2location:  Kleshchevnikov et al. (2022) [![DOI](https://zenodo.org/badge/DOI/10.1038/s41587-021-01139-4.svg)](https://doi.org/10.1038/s41587-021-01139-4) \
Single Cell Atlas:  Traeuble et al. (2024) [![DOI](https://img.shields.io/badge/DOI-10.1101%2F2024.09.11.612431-blue)](https://doi.org/10.1101/2024.09.11.612431)

