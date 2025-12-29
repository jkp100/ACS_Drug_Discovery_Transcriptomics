import pandas as pd
# Input / Output paths
INPUT_FILE = "data/raw/GSE252710_Expression_Gene.txt"
OUTPUT_FILE = "data/processed/GSE252710_Expression_Table_Biojupies_Clean.csv"

# Load raw expression table
df = pd.read_csv(INPUT_FILE, sep="\t")

# Keep only gene name + expression
expression_cols = [
    "Ctrl1", "Ctrl2", "Ctrl3",
    "ACS1", "ACS2", "ACS3",
    "SA1", "SA2", "SA3"
]

df_clean = df[["Gene_Name"] + expression_cols]
# Handle duplicated gene names
df_clean = (
    df_clean
    .groupby("Gene_Name", as_index=False)
    .mean()
)
# Set gene names as row inde
df_clean = df_clean.set_index("Gene_Name")

# Save BioJupies-ready CS
df_clean.to_csv(OUTPUT_FILE)

print("Clean expression matrix saved to:", OUTPUT_FILE)
print("Shape:", df_clean.shape)
