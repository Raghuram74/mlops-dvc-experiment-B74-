# Git and DVC for Machine Learning Dataset and Model Versioning

Aim
---
Implement Git for source code version control and DVC for dataset and model versioning to enable reproducible machine learning experiments.

Installation (Windows PowerShell)
---
1. Create and enter project folder (if not already present):

```powershell
mkdir "mlops_experiment_3"
cd "mlops_experiment_3"
```

2. Create and activate a Python virtual environment, then install requirements:

```powershell
python -m venv .venv
. .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3. (Optional) Install or upgrade DVC:

```powershell
pip install --upgrade dvc
```

Running the dataset creation script
---
Create the dataset from sklearn and save it as `data/dataset.csv`:

```powershell
python src\create_dataset.py
```

Training models
---
Train model version 1:

```powershell
python src\train_v1.py
```

Train model version 2:

```powershell
python src\train_v2.py
```

Running predictions
---
Example:

```powershell
python src\predict.py --model models\random_forest_v1.pkl
```

Full lab commands for Git, GitHub and DVC are provided in `reports/experiment_report.md`.

