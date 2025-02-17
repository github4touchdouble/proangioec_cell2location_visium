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

