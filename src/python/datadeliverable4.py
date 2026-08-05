# ============================================================
# DATA422 DELIVERABLE 3
# Combine monthly Airbnb datasets for Christchurch
# October 2025 to June 2026
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ------------------------------------------------------------
# 1. SET FILE LOCATIONS
# ------------------------------------------------------------

# This is the folder where all 9 monthly raw CSV files are stored.
raw_folder = Path(
    "/Users/maxburford/Documents/GitHub/DATA422_201/data/raw/deliverable 3"
)

# This is where the cleaned dataset and summary files will be saved.
processed_folder = Path(
    "/Users/maxburford/Documents/GitHub/DATA422_201/data/processed"
)

# This is where the graphs will be saved.
plots_folder = Path(
    "/Users/maxburford/Documents/GitHub/DATA422_201/outputs/plots"
)

# Create the output folders if they do not already exist.
processed_folder.mkdir(parents=True, exist_ok=True)
plots_folder.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# 2. MATCH EACH FILE WITH ITS MONTH AND YEAR
# ------------------------------------------------------------

# A dictionary is used so each filename is linked to the correct month.
# This lets us add the month and year before combining the datasets.
files = {
    "Oct 2025": raw_folder / "listings_october.csv",
    "Nov 2025": raw_folder / "listings_november.csv",
    "Dec 2025": raw_folder / "listings_december.csv",
    "Jan 2026": raw_folder / "listings_january.csv",
    "Feb 2026": raw_folder / "listings_february.csv",
    "Mar 2026": raw_folder / "listings_march.csv",
    "Apr 2026": raw_folder / "listings_april.csv",
    "May 2026": raw_folder / "listings_may.csv",
    "Jun 2026": raw_folder / "listings_june.csv"
}


# ------------------------------------------------------------
# 3. LOAD, FILTER AND PREPARE EACH MONTH
# ------------------------------------------------------------

# This empty list will store the Christchurch data from each month.
monthly_data = []

# The loop repeats the same preparation steps for all 9 files.
for month_year, file_path in files.items():

    print(f"Processing {month_year}")

    # Load one monthly CSV file into a pandas DataFrame.
    df = pd.read_csv(file_path)

    # Keep only rows where the broader region is Christchurch City.
    # .copy() creates a separate DataFrame that can be safely changed.
    christchurch = df[
        df["neighbourhood_group"] == "Christchurch City"
    ].copy()

    # Add a new column showing which monthly snapshot each row came from.
    christchurch["month_year"] = month_year

    # Store the prepared monthly dataset in the list.
    monthly_data.append(christchurch)

    # Print the number of Christchurch listings found for that month.
    print(f"Christchurch rows: {len(christchurch)}")


# ------------------------------------------------------------
# 4. COMBINE ALL MONTHS
# ------------------------------------------------------------

# Concatenate means stack all monthly DataFrames underneath each other.
# ignore_index=True creates a new row index from 0 onwards.
combined = pd.concat(
    monthly_data,
    ignore_index=True
)

print("\nCombined dataset shape:")
print(combined.shape)


# ------------------------------------------------------------
# 5. CLEAN IMPORTANT COLUMNS
# ------------------------------------------------------------

# Convert price into a numeric column.
# This removes dollar signs and commas if they are present.
combined["price"] = (
    combined["price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

# Any invalid or missing price values become NaN.
combined["price"] = pd.to_numeric(
    combined["price"],
    errors="coerce"
)

# Convert last_review into a date column.
combined["last_review"] = pd.to_datetime(
    combined["last_review"],
    errors="coerce"
)


# ------------------------------------------------------------
# 6. NUMERICAL SUMMARY STATISTICS
# ------------------------------------------------------------

# Select only numerical columns.
numeric_columns = combined.select_dtypes(
    include="number"
).columns

# Calculate count, mean, standard deviation, minimum,
# quartiles and maximum for every numerical column.
numeric_summary = combined[numeric_columns].describe().T

# Add the number of missing values for each numerical column.
numeric_summary["missing_count"] = (
    combined[numeric_columns].isna().sum()
)

# Add the percentage of missing values.
numeric_summary["missing_percentage"] = (
    combined[numeric_columns].isna().mean() * 100
).round(2)

print("\nNumerical summary statistics:")
print(numeric_summary)


# ------------------------------------------------------------
# 7. CATEGORICAL SUMMARY STATISTICS
# ------------------------------------------------------------

# Select text and categorical columns.
categorical_columns = combined.select_dtypes(
    include=["object", "string", "category"]
).columns

categorical_rows = []

# Summarise each categorical column.
for column in categorical_columns:

    # Count how often each value appears.
    counts = combined[column].value_counts()

    categorical_rows.append({
        "column": column,

        # Number of different categories or values.
        "unique_values": combined[column].nunique(),

        # Most common value in the column.
        "most_common_value": (
            counts.index[0] if not counts.empty else None
        ),

        # Number of times the most common value appears.
        "most_common_count": (
            counts.iloc[0] if not counts.empty else 0
        ),

        # Number of missing values.
        "missing_count": combined[column].isna().sum(),

        # Percentage of missing values.
        "missing_percentage": round(
            combined[column].isna().mean() * 100,
            2
        )
    })

# Convert the list of results into a DataFrame.
categorical_summary = pd.DataFrame(categorical_rows)

print("\nCategorical summary:")
print(categorical_summary)


# ------------------------------------------------------------
# 8. MISSING VALUES FOR EVERY COLUMN
# ------------------------------------------------------------

# Create one table showing missing values for all columns.
missing_summary = pd.DataFrame({
    "column": combined.columns,
    "missing_count": combined.isna().sum().values,
    "missing_percentage": (
        combined.isna().mean().values * 100
    ).round(2)
})

print("\nMissing values:")
print(missing_summary)


# ------------------------------------------------------------
# 9. LISTINGS PER MONTH
# ------------------------------------------------------------

# Keep the months in chronological order.
month_order = list(files.keys())

# Count how many Christchurch listing rows appear in each month.
listings_per_month = (
    combined["month_year"]
    .value_counts()
    .reindex(month_order)
    .rename_axis("month_year")
    .reset_index(name="number_of_listings")
)

print("\nListings per month:")
print(listings_per_month)


# ------------------------------------------------------------
# 10. SAVE THE DATA AND SUMMARY TABLES
# ------------------------------------------------------------

# Save the full concatenated Christchurch dataset.
combined.to_csv(
    processed_folder /
    "christchurch_listings_oct2025_jun2026.csv",
    index=False
)

# Save the summary tables as separate CSV files.
numeric_summary.to_csv(
    processed_folder / "numerical_summary.csv"
)

categorical_summary.to_csv(
    processed_folder / "categorical_summary.csv",
    index=False
)

missing_summary.to_csv(
    processed_folder / "missing_values_summary.csv",
    index=False
)

listings_per_month.to_csv(
    processed_folder / "listings_per_month.csv",
    index=False
)


# ------------------------------------------------------------
# 11. PLOT: NUMBER OF LISTINGS BY MONTH
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    listings_per_month["month_year"],
    listings_per_month["number_of_listings"]
)

plt.title("Number of Christchurch Airbnb Listings by Month")
plt.xlabel("Month")
plt.ylabel("Number of Listings")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the graph as a PNG file.
plt.savefig(
    plots_folder / "listings_by_month.png",
    dpi=300
)

plt.show()


# ------------------------------------------------------------
# 12. PLOT: MEDIAN PRICE BY MONTH
# ------------------------------------------------------------

# Median is used because Airbnb prices are strongly right-skewed
# and extreme prices can pull the mean upward.
median_price = (
    combined.groupby("month_year")["price"]
    .median()
    .reindex(month_order)
)

plt.figure(figsize=(10, 6))

plt.plot(
    median_price.index,
    median_price.values,
    marker="o"
)

plt.title("Median Christchurch Airbnb Price by Month")
plt.xlabel("Month")
plt.ylabel("Median Price ($)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    plots_folder / "median_price_by_month.png",
    dpi=300
)

plt.show()


# ------------------------------------------------------------
# 13. PLOT: ROOM TYPE COUNTS
# ------------------------------------------------------------

room_type_counts = combined["room_type"].value_counts()

plt.figure(figsize=(9, 6))

plt.bar(
    room_type_counts.index,
    room_type_counts.values
)

plt.title("Christchurch Airbnb Listings by Room Type")
plt.xlabel("Room Type")
plt.ylabel("Number of Listings")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    plots_folder / "room_type_counts.png",
    dpi=300
)

plt.show()


# ------------------------------------------------------------
# 14. PLOT: PRICE DISTRIBUTION
# ------------------------------------------------------------

# Remove missing prices.
# Limit the graph to prices of $2,000 or less so extreme outliers
# do not make the main distribution unreadable.
price_plot_data = combined[
    combined["price"].notna()
    & (combined["price"] <= 2000)
]["price"]

plt.figure(figsize=(10, 6))

plt.hist(
    price_plot_data,
    bins=40
)

plt.title("Distribution of Christchurch Airbnb Prices")
plt.xlabel("Nightly Price ($)")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig(
    plots_folder / "price_distribution.png",
    dpi=300
)

plt.show()


# ------------------------------------------------------------
# 15. FINAL MESSAGE
# ------------------------------------------------------------

print("\nFinished successfully.")
print(f"Final rows: {combined.shape[0]}")
print(f"Final columns: {combined.shape[1]}")
print(f"Data saved in: {processed_folder}")
print(f"Plots saved in: {plots_folder}")