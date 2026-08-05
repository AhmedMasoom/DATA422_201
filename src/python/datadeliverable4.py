import pandas as pd
from pathlib import Path

# Folder containing the raw Airbnb files
folder = Path("data/raw/deliverable 3")

# Match each file to its correct month and year
files = {
    "Oct 2025": folder / "listings_october.csv",
    "Nov 2025": folder / "listings_november.csv",
    "Dec 2025": folder / "listings_december.csv",
    "Jan 2026": folder / "listings_january.csv",
    "Feb 2026": folder / "listings_february.csv",
    "Mar 2026": folder / "listings_march.csv",
    "Apr 2026": folder / "listings_april.csv",
    "May 2026": folder / "listings_may.csv",
    "Jun 2026": folder / "listings_june.csv"
}

processed_data = []

# Load, filter, and prepare every file
for month_year, file_path in files.items():

    print(f"Processing {month_year}: {file_path}")

    df = pd.read_csv(file_path)

    # Filter to Christchurch City only
    christchurch = df[
        df["neighbourhood_group"] == "Christchurch City"
    ].copy()

    # Add month and year column
    christchurch["month_year"] = month_year

    processed_data.append(christchurch)

    print(f"Christchurch rows: {len(christchurch)}")

# Combine all months
combined = pd.concat(
    processed_data,
    ignore_index=True
)

print("\nCombined dataset shape:")
print(combined.shape)

# Convert price to a number if needed
if "price" in combined.columns:
    combined["price"] = (
        combined["price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    combined["price"] = pd.to_numeric(
        combined["price"],
        errors="coerce"
    )

# Numerical summary statistics
numeric_summary = (
    combined
    .select_dtypes(include="number")
    .describe()
    .T
)

numeric_summary["missing_count"] = (
    combined
    .select_dtypes(include="number")
    .isna()
    .sum()
)

print("\nNumerical summary statistics:")
print(numeric_summary)

# Missing values for every column
missing_summary = pd.DataFrame({
    "column": combined.columns,
    "missing_count": combined.isna().sum().values,
    "missing_percentage": (
        combined.isna().mean().values * 100
    ).round(2)
})

print("\nMissing values:")
print(missing_summary)

# Categorical summary
categorical_columns = combined.select_dtypes(
    include=["object", "category"]
).columns

categorical_summary = []

for column in categorical_columns:

    mode_value = (
        combined[column].mode().iloc[0]
        if not combined[column].mode().empty
        else None
    )

    categorical_summary.append({
        "column": column,
        "unique_values": combined[column].nunique(),
        "most_common_value": mode_value,
        "most_common_count": (
            combined[column].value_counts().iloc[0]
            if not combined[column].value_counts().empty
            else 0
        ),
        "missing_count": combined[column].isna().sum()
    })

categorical_summary = pd.DataFrame(categorical_summary)

print("\nCategorical summary:")
print(categorical_summary)

# Count listings per month
listings_per_month = (
    combined["month_year"]
    .value_counts()
    .reindex(files.keys())
    .reset_index()
)

listings_per_month.columns = [
    "month_year",
    "number_of_rows"
]

print("\nListings per month:")
print(listings_per_month)

# Create processed output folder
output_folder = Path("data/processed")
output_folder.mkdir(parents=True, exist_ok=True)

# Save combined dataset
combined.to_csv(
    output_folder / "christchurch_listings_oct2025_jun2026.csv",
    index=False
)

# Save summaries
numeric_summary.to_csv(
    output_folder / "numerical_summary.csv"
)

missing_summary.to_csv(
    output_folder / "missing_values_summary.csv",
    index=False
)

categorical_summary.to_csv(
    output_folder / "categorical_summary.csv",
    index=False
)

listings_per_month.to_csv(
    output_folder / "listings_per_month.csv",
    index=False
)

print("\nFinished.")
print("Files saved in data/processed/")