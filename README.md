# DATA422 Project — Deliverable 2: New Zealand Airbnb Listings

## 1. Dataset Source

| Property | Detail |
|---|---|
| **Source** | [Inside Airbnb](https://insideairbnb.com/) — Get the Data page ([https://insideairbnb.com/get-the-data/](https://insideairbnb.com/get-the-data/)) |
| **Region** | New Zealand (country-wide) |
| **File used** | `listings.csv` (the lightweight **summary** file, used for visualisations — *not* the detailed `listings.csv.gz`) |
| **Snapshot period** | June 2026 |
| **License** | [Creative Commons Attribution 4.0 International (CC BY 4.0)](http://creativecommons.org/licenses/by/4.0/) |
| **Storage** | Stored locally on each team member's machine only. **Not committed to this GitHub repository** — see `.gitignore`. |
| **Rows** | 50,932 listings |
| **Columns** | 18 |

### About Inside Airbnb

Inside Airbnb is an independent, non-commercial project that scrapes and publishes publicly available data from the Airbnb website, in order to support public discussion and research about Airbnb's impact on residential housing and communities. Data is refreshed periodically per city/region (typically monthly or quarterly). Because it is scraped rather than provided directly by Airbnb, it reflects what is publicly visible on listing pages at the time of scraping, not Airbnb's internal booking or transaction records.

### ⚠️ Important note on the reference/scrape date

The **summary** `listings.csv` file (the version required by this deliverable) does **not** include a `last_scraped` or equivalent scrape-date column — that field only exists in the detailed `listings.csv.gz` export, which this deliverable explicitly asked us *not* to use.

To calculate "days since last review" (required by this deliverable), a reference date is needed. Since no scrape-date column is available:

> **Reference date used: 2026-06-22**
> This is the maximum (most recent) value observed in the `last_review` column across all 50,932 New Zealand listings. It is used as a documented proxy for the true scrape/publish date, since the dataset cannot have been compiled before its most recent review was posted. This is consistent with the deliverable's framing of the dataset as a "June 2026" snapshot.

If a more precise compiled date is later confirmed directly from the Inside Airbnb site, this section should be updated and the recency calculations re-run.

---

## 2. Data Dictionary

| # | Column | Data Type | Description | Notes / Missing Data |
|---|---|---|---|---|
| 1 | `id` | Integer | Unique numeric identifier for the listing, assigned by Airbnb. | No missing values. Treated as a **Meta**/identifier field, not an analytical feature. |
| 2 | `name` | Text | The listing's title, as written by the host (e.g. "Nice n cosy"). | Free text; may contain emoji, non-English characters, or unusual formatting. |
| 3 | `host_id` | Integer | Unique numeric identifier for the host account. A single host can have multiple listings. | 1 missing value. |
| 4 | `host_name` | Text | Host's display name, as shown publicly on Airbnb. | 6 missing values. Not a verified legal name — just whatever the host set publicly. |
| 5 | `neighbourhood_group` | Categorical | The broader administrative region/district/city the listing falls under (e.g. "Christchurch City", "Auckland", "Waikato District"). 67 unique values across NZ. | No missing values. **This is the column used to filter for Christchurch** (`neighbourhood_group == "Christchurch City"`), confirmed as a single clean string with no spelling variants. |
| 6 | `neighbourhood` | Categorical | A finer-grained sub-area within the `neighbourhood_group` (e.g. specific ward or suburb name). | No missing values, but naming conventions vary by region (e.g. some regions use "Ward" naming, others use suburb names). |
| 7 | `latitude` | Float | Latitude coordinate of the listing. | Airbnb may obfuscate exact coordinates slightly (typically within ~150m) for host privacy. |
| 8 | `longitude` | Float | Longitude coordinate of the listing. | Same privacy-obfuscation caveat as latitude. |
| 9 | `room_type` | Categorical | The type of space being offered. Standard Airbnb categories: "Entire home/apt", "Private room", "Shared room", "Hotel room". | No missing values. |
| 10 | `price` | Float (currency, NZD assumed) | The nightly price for the listing, as displayed on Airbnb at time of scraping. | **5,223 missing values (~10.3%)** — typically listings that don't publicly display a price (e.g. inactive, blocked, or requiring direct host contact). These rows are **excluded** from price histograms rather than imputed. |
| 11 | `minimum_nights` | Float | The minimum number of consecutive nights a guest must book. | 8 missing values. |
| 12 | `number_of_reviews` | Integer | Total number of reviews the listing has ever received (all-time). | No missing values; listings with 0 reviews are valid (never been reviewed). **This is the column used for the "top 10% most-reviewed" analysis.** |
| 13 | `last_review` | Date | The date of the most recent review left on the listing. | **5,128 missing values (~10.1%)** — these are exactly the listings with `number_of_reviews == 0` (no review exists, so there is no date to record). These rows are **excluded** from the "days since last review" feature and its histogram, rather than assigned a fabricated date. |
| 14 | `reviews_per_month` | Float | Average number of reviews received per month, calculated by Airbnb/Inside Airbnb over the listing's active review history. | 5,128 missing values — same rows as `last_review` (zero-review listings). |
| 15 | `calculated_host_listings_count` | Float | The number of listings the same host currently has active on Airbnb, as calculated by Inside Airbnb from the dataset itself (not Airbnb's internal system). | 1 missing value. Useful for identifying "professional"/multi-property hosts vs. single-listing hosts. |
| 16 | `availability_365` | Integer | Number of days within the next 365 days that the listing is marked as available for booking. | No missing values. A value of 0 can mean fully booked, blocked by the host, or removed/inactive — the dataset does not distinguish between these cases. |
| 17 | `number_of_reviews_ltm` | Integer | Number of reviews received in the **last twelve months** (ltm = "last twelve months"), as opposed to `number_of_reviews` which is all-time. | No missing values. Useful for identifying currently active vs. dormant listings. |
| 18 | `license` | Float/Text (effectively empty) | Intended to hold a short-term rental license/registration number, where local regulations require one. | **100% missing (50,932 / 50,932 rows)** — not applicable to this dataset/region as scraped, or not enforced/displayed in NZ. This column is **ignored entirely** for this deliverable. |

---

## 3. Key Wrangling Decisions (Documented for Reproducibility)

These decisions were made deliberately, in order to keep the analysis defensible and reproducible by any team member re-running the pipeline.

| Decision | Choice Made | Rationale |
|---|---|---|
| Reference date for "days since last review" | **2026-06-22** | No scrape-date column exists in the summary file; this is the max observed `last_review` date, documented as a proxy (see Section 1). |
| Handling of missing `price` | Excluded from price histograms | Cannot plot or compare a null value; imputing a fake price would distort the true distribution. |
| Handling of missing `last_review` | Excluded from recency histogram | These rows correspond to listings with zero reviews — there is no last-review date to compute a difference from. Fabricating one would misrepresent the data. |
| Christchurch identification | `neighbourhood_group == "Christchurch City"` | Verified as a single, clean, unambiguous string value in the dataset — no fuzzy matching or multiple spelling variants needed. |
| `license` column | Ignored entirely | 100% missing; not usable or relevant to any required task in this deliverable. |
| Identifier columns (`id`, `name`, `host_id`, `host_name`) | Set to **Meta** role in Orange | These are reference/labelling fields, not analytical variables, and should not be treated as numeric features in any statistical widget. |
| Price histogram outlier cutoff | Displayed range capped at **≤ $2,000/night** | Max price in the dataset is $84,438 — an extreme long tail that compresses the readable part of the distribution into a single bar. The $2,000 cutoff excludes only 391 listings (0.86% of priced listings), so almost no data is lost visually. This is a *display* filter only — it does not alter the underlying dataset used for other tasks. |
| Days-since-last-review outlier cutoff | Displayed range capped at **≤ 1,500 days** | Max value is 4,859 days (~13.3 years) — same long-tail problem as price. The 1,500-day cutoff excludes 513 listings (1.12%), keeping the methodology consistent with the price cutoff's logic. |
| Top 10% most-reviewed definition | `number_of_reviews > 185` (strictly greater than) | The 90th-percentile value (185 reviews) has a 39-listing tie sitting exactly on the boundary. Using `≥ 185` would include those ties and produce 5,130 listings (10.07% of the dataset); using strict `> 185` produces 5,091 listings (10.00%), a closer and cleaner approximation of a true top-10% split. |

---

## 4. Tools Used

| Tool | Purpose |
|---|---|
| **Orange Data Mining** | No-code data wrangling pipeline: loading, filtering, feature engineering, and visualisation (histograms) |
| **GitHub** | Version control and documentation (this README, `.gitignore`) — raw data itself is excluded per project rules |
| **ClickUp** | Team project management / task tracking |

---

## 5. Repository Structure Note

The dataset file (`listings.csv`) is intentionally **not included in this repository**. Each team member must download it independently from the [Inside Airbnb Get the Data page](https://insideairbnb.com/get-the-data/) (New Zealand, June 2026, summary `listings.csv`) and store it locally. See `.gitignore` for the exclusion rule.

---

## 6. Orange Pipeline Walkthrough — Method, Decisions, and Results

This section documents each analytical task in the Orange workflow: what was built, why, and what it showed. Written so any team member can reproduce the pipeline from this description alone, without needing to reverse-engineer the `.ows` file.

### 6.1 Data Loading & Type Verification

- **Widgets**: File → Data Table / Feature Statistics
- **Method**: Loaded `listings.csv` via the File widget, verified Orange's auto-detected column types (numeric, categorical, time) against expectations, and corrected roles where needed.
- **Decision**: `id`, `name`, `host_id`, `host_name`, and `license` were set to **Meta** role rather than **Feature**, since they are identifiers/labels, not analytical variables. `last_review` was confirmed as **Time** type (required for later date arithmetic).
- **Why it matters**: mis-typed columns (e.g. `price` importing as text due to blank cells) would silently break every downstream numeric operation. Verifying at load time avoids rebuilding the pipeline later.

### 6.2 Price Distribution — NZ-wide, Christchurch, and Combined

- **Widgets**: Select Rows (filter nulls, filter ≤ $2,000) → Distributions; Feature Constructor (derived `region_group` column: "Christchurch City" vs. "Rest of NZ") → Distributions (split by `region_group`)
- **Method**: Filtered out the 5,223 listings with missing `price`, then filtered the display range to ≤ $2,000 (see Section 3 for the outlier-cutoff rationale). Built separate histograms for all-of-NZ and Christchurch-only, then combined both into one plot using a derived `region_group` feature.
- **Key finding during testing**: Orange's Distributions widget, when a "Fitted distribution" (Normal curve) is applied on top of a "Split by" grouping, scales each group's fitted curve independently — **not** proportionally to actual sample size. This produced a visually misleading first version of the combined plot, where Christchurch's curve (n=3,193) appeared taller than the Rest of NZ's curve (n=42,125), despite Christchurch having 13× fewer listings. This was caught by manually recomputing raw bin counts in Python and comparing them against the plot — the fitted-curve view was discarded in favour of the raw-count view (`Fitted distribution: None`) for the final presentation, which is directly interpretable without hidden normalization.
- **Results**: Christchurch mean price ≈ $248 (σ ≈ 163); Rest of NZ mean price ≈ $355 (σ ≈ 279). Both distributions are right-skewed. Christchurch listings tend to be somewhat cheaper on average than the national distribution, though both groups show the same general shape.

### 6.3 Days Since Last Review — Feature Engineering & Distribution

- **Widgets**: Feature Constructor (new column `days_since_last_review`) → Select Rows (filter missing, filter ≤ 1,500 days) → Distributions
- **Method**: Computed `days_since_last_review = (1782086400 − last_review) / 86400`, where `1782086400` is the Unix timestamp for the documented reference date (2026-06-22 00:00:00 UTC), and `last_review` is Orange's internal timestamp representation (seconds since epoch) of that column. Dividing by 86,400 converts the seconds-based gap into days.
- **Verification**: The computed value was manually spot-checked against hand-calculated day differences for individual rows before trusting the column, and the non-missing row count (45,804) was cross-checked against the expected value (50,932 total − 5,128 listings with zero reviews).
- **Decision**: Listings with zero reviews (no `last_review` date to compute from) were excluded rather than assigned a fabricated value.
- **Results**: Median = 65 days, 75th percentile = 131 days, max = 4,859 days (~13.3 years) — a strongly right-skewed distribution. Most listings were reviewed recently (within a few months), while a smaller minority haven't been reviewed in over a year, potentially indicating seasonal or inactive listings.

### 6.4 Top 10% Most-Reviewed Listings & Christchurch Count

- **Widgets**: Select Rows (`number_of_reviews > 185`) → Data Info; chained Select Rows (`neighbourhood_group == "Christchurch City"`) → Data Info
- **Method**: Computed the 90th-percentile value of `number_of_reviews` (185) externally, checked for ties at that boundary (39 listings tied exactly at 185 — see Section 3 decision on `>` vs `≥`), then filtered the dataset to the top 10% and further filtered that group to Christchurch-only.
- **Results**:
  - Top 10% most-reviewed listings, NZ-wide: **5,091**
  - Of those, located in Christchurch City: **342**
  - Christchurch's share of the top-10% group: 6.72%
  - **Interpretation**: Christchurch has 3,469 listings in total, and 342 of them (9.86%) fall into the nationwide top-10%-by-reviews group — almost exactly the 10% baseline expected if Christchurch listings were reviewed at the same rate as the rest of the country. This suggests Christchurch is **proportionally represented** among NZ's most-reviewed listings, neither over- nor under-performing relative to the national pattern.

---

## 7. Lessons Learned / Notes for the Team

- Always verify a visualization widget's actual computation (e.g. "Show probabilities," fitted-curve normalization) before presenting it — labels like "Frequency" don't always mean raw counts, and smoothing/fitting features can normalize per group in non-obvious ways.
- Outlier-cutoff decisions for visualization should be quantified (how many/what % of rows excluded), not chosen arbitrarily, and should be applied as *display* filters separate from the underlying analytical dataset.
- Percentile-based filters (e.g. "top 10%") should be checked for ties at the boundary before choosing `>` vs. `≥`.