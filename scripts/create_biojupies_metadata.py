import pandas as pd

# Output path
OUTPUT_FILE = "data/processed/GSE252710_Metadata.csv"

# Define sample groups

metadata = {
    "Sample": [
        "Ctrl1", "Ctrl2", "Ctrl3",
        "ACS1", "ACS2", "ACS3",
        "SA1", "SA2", "SA3"
    ],
    "Condition": [
        "Control", "Control", "Control",
        "ACS", "ACS", "ACS",
        "Stable_Angina", "Stable_Angina", "Stable_Angina"
    ]
}

df_meta = pd.DataFrame(metadata)

# Save metadata CSV
df_meta.to_csv(OUTPUT_FILE, index=False)

print("Metadata file saved to:", OUTPUT_FILE)
print(df_meta)
