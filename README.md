# Tutorial:
---

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
- **Mac/Linux:**
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
PATH_TO_MAP_MODEL2WO=./
```

### 5. Verify Setup
Ensure everything is installed correctly by running:

```sh
python -m pip check
```

### 1. Working on the `ipynb` File
- The main analysis is conducted in a Jupyter Notebook (`.ipynb`).
- Always create a new branch before making changes:  
  ```sh
  git checkout -b feature/your-feature-name
  ```
- Before committing, ensure that all cells are executed and outputs are saved.
- To prevent merge conflicts, always clear unnecessary output cells before committing:
  ```sh
  jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace your_notebook.ipynb
  ```
- Use `nbdime` to compare and merge notebooks cleanly:
  ```sh
  nbdime diff your_notebook.ipynb
  ```

### 2. Version Control & Merging
- Commit your changes with meaningful messages:
  ```sh
  git commit -m "Added spatial data analysis for XYZ"
  ```
- Push your changes to your branch:
  ```sh
  git push origin feature/your-feature-name
  ```
- Open a pull request (PR) and request a review before merging into `master`.
- Resolve conflicts using `nbdime merge` instead of manually editing `.ipynb` files:
  ```sh
  nbdime merge your_notebook.ipynb
  ```
- Sync your branch with `master` regularly:
  ```sh
  git pull origin master
  ```
