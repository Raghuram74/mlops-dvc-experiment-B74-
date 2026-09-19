# Experiment 3 Report

Title: Git and DVC for Machine Learning Dataset and Model Versioning

Aim: Implement Git for source code version control and DVC for dataset and model versioning to enable reproducible ML experiments.

Objectives:
- Track code with Git
- Track datasets and models with DVC
- Train two Random Forest models and version them
- Demonstrate dataset and model restoration
- Verify reproducibility from a fresh clone

Tools: Python, pandas, scikit-learn, joblib, Git, GitHub, DVC

Dataset: Breast Cancer Wisconsin dataset from scikit-learn saved as data/dataset.csv

Project files include:
- src/create_dataset.py
- src/train_v1.py
- src/train_v2.py
- src/predict.py
- data/dataset.csv
- models/
- dvc_storage/

Key commands (PowerShell):
- Create dataset: python src\create_dataset.py
- Track dataset: dvc add data\dataset.csv ; git add data\dataset.csv.dvc ; git commit -m "Add dataset v1"
- Make dataset v2: run a small script to add column experiment_version='v2', then dvc add and commit
- Train v1: python src\train_v1.py ; dvc add models\random_forest_v1.pkl ; git commit -m "Add model v1" ; dvc push
- Train v2: python src\train_v2.py ; dvc add models\random_forest_v2.pkl ; git commit -m "Add model v2" ; dvc push
- Restore dataset/model: git checkout <commit> -- data\dataset.csv.dvc ; dvc pull ; dvc checkout

Comparison (Git vs DVC):
Feature | Git | DVC
Source code versioning | Yes | No
Dataset versioning | Limited | Yes
Model versioning | Limited | Yes
Large files | Not ideal | Suitable
Reproducibility | Code only | Code + data + models

Conclusion: Use Git for code and DVC for large data/models to enable reproducible experiments.
