$ErrorActionPreference = "Stop"

Write-Host "====================================="
Write-Host " MLOps Experiment 3 - Dataset V2"
Write-Host "====================================="

# Check dataset
if (-not (Test-Path "data\dataset.csv")) {
    Write-Host "ERROR: data\dataset.csv not found." -ForegroundColor Red
    exit 1
}

Write-Host "Dataset found."

# Check Python
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: Python is not installed or not in PATH." -ForegroundColor Red
    exit 1
}

Write-Host "Python found."

# Check DVC
if (-not (Get-Command dvc -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: DVC is not installed or not in PATH." -ForegroundColor Red
    exit 1
}

Write-Host "DVC found."

# Create Dataset Version 2
Write-Host ""
Write-Host "Creating Dataset Version 2..."

python -c "import pandas as pd; p='data/dataset.csv'; df=pd.read_csv(p); df['experiment_version']='v2'; df.to_csv(p,index=False)"

Write-Host "Dataset Version 2 created."

# Track dataset with DVC
Write-Host ""
Write-Host "Updating DVC..."

dvc add data/dataset.csv

Write-Host "Dataset tracked by DVC."

# Push dataset to DVC remote
Write-Host ""
Write-Host "Pushing dataset to DVC remote..."

dvc push

Write-Host "DVC push completed."

# Git staging
Write-Host ""
Write-Host "Staging DVC metadata..."

git add data/dataset.csv.dvc data/.gitignore

# Git commit
Write-Host ""
Write-Host "Creating Git commit..."

git commit -m "Create dataset version 2"

Write-Host ""
Write-Host "====================================="
Write-Host " Dataset Version 2 Completed!"
Write-Host "====================================="

Write-Host ""
Write-Host "DVC Status:"
dvc status

Write-Host ""
Write-Host "Git Status:"
git status

Write-Host ""
Write-Host "Latest Git Commits:"
git log --oneline -5

Write-Host ""
Write-Host "IMPORTANT: git push was NOT executed."
Write-Host "Review the changes and run 'git push' manually."