# imports
import os
import csv
import sys
import pandas as pd
from rdkit import Chem
from rdkit.Chem.Descriptors import MolWt
from eosce.models import ErsiliaCompoundEmbeddings
import joblib

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.abspath(os.path.join(root, "..", "..", "checkpoints", "AutoML_ersilia.joblib"))

# Load ErsiliaCompoundEmbeddings model
ersilia_model = ErsiliaCompoundEmbeddings()

# Load AutoML model
def load_automl_model(model_path):
    return joblib.load(model_path)

automl_model = load_automl_model(model_path)

# my model
def my_model(embeddings_list):
    # Convert embeddings to DataFrame
    embeddings_df = pd.DataFrame(embeddings_list)

    # Make predictions using the AutoML model's predict_proba
    tdc_predictions_proba = automl_model.predict_proba(embeddings_df.values)[:, 1]

    return tdc_predictions_proba

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# Convert SMILES to embeddings using Ersilia model
embeddings_list = [ersilia_model.transform([smi])[0] for smi in smiles_list]

# run model
outputs = my_model(embeddings_list)

# check input and output have the same length
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["value"])  # header
    for o in outputs:
        writer.writerow([o])
