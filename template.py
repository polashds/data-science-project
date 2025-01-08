import os
from pathlib import Path


project_name = "ds_housing_price"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/data/__init__.py",
    f"{project_name}/data/raw__init__.py",
    f"{project_name}/data/processed/__init__.py",
    f"{project_name}/data/external/__init__.py",
    f"{project_name}/notebooks/__init__.py",
    f"{project_name}/notebooks/01-data-exploration.ipynb",
    f"{project_name}/notebooks/02-feature-engineering.ipynb",
    f"{project_name}/notebooks/03-model-training.ipynb",
    f"{project_name}/notebooks/04-model-evaluation.ipynb",
    f"{project_name}/src/data/__init__.py",
    f"{project_name}/src/data/load_data.py",
    f"{project_name}/src/data/process_data.py",
    f"{project_name}/src/data/split_data.py",    
    f"{project_name}/src/features/__init__.py",    
    f"{project_name}/src/features/feature_selection.py",
    f"{project_name}/src/models/__init__.py",
    f"{project_name}/src/models/train_model.py",
    f"{project_name}/src/models/predict_model.py",
    f"{project_name}/src/models/evaluate_model.py",
    f"{project_name}/src/visualizations/__init__.py",
    f"{project_name}/src/visualizations/plot_results.py",
    f"{project_name}/src/tests/__init__.py",
    f"{project_name}/src/tests/test_data_preprocessing.py",
    f"{project_name}/src/tests/test_models.py",
    f"{project_name}/src/tests/test_visualizations.py",
    f"{project_name}/reports/__init__.py",
    f"{project_name}/reports/figures/__init__.py",
    f"{project_name}/reports/figures/report.md",
    f"{project_name}/docs/__init__.py",
    f"{project_name}/docs/README.md",
    "requirements.txt",
    ".gitignore",
    "setup.py",
    "README.md",
    "LICENSE"
]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filepath = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
    else: 
        print(f"file is already exists: {filepath}")