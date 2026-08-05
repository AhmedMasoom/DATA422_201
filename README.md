## Deliverable 3

### Objective

The monthly New Zealand Inside Airbnb `listings.csv` snapshots from October 2025 to June 2026 were prepared and combined for Christchurch City.

### Workflow

1. Loaded all nine monthly CSV files.
2. Filtered each dataset to `neighbourhood_group == "Christchurch City"`.
3. Added a `month_year` column identifying the monthly snapshot.
4. Concatenated all filtered datasets into one dataset.
5. Produced numerical and categorical summary statistics.
6. Counted missing values for every column.
7. Saved the combined dataset and summary files.
8. Produced visualisations in Python.
9. Reproduced the analysis in Orange Data Mining.

### Results

- Combined dataset: 28,795 rows and 19 columns.
- Christchurch listing records increased from 2,991 in October 2025 to 3,469 in June 2026.
- `price` had 10,667 missing values, or 37.04%.
- December 2025, January 2026 and February 2026 had no usable price values, so monthly median prices could not be calculated for those months.
- Entire homes/apartments were the most common room type.
- Central Ward had the largest number of listing records.

### Files

- Python workflow: `src/python/datadeliverable4.py`
- Orange workflow: `workflows/deliverable3_orange.ows`
- Plots: `outputs/plots/`