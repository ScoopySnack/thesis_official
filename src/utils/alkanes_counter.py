import pandas as pd


# ---------- 1. Per-Alkane Analysis (Row-by-Row) ----------
def per_alkane_missing_counts(df):
    # We set 'name' as the index so we don't count the name itself as a "feature"
    # We operate on a copy so we don't modify the original dataframe
    if 'name' in df.columns:
        work_df = df.set_index('name')
    else:
        work_df = df.copy()

    # Pandas Magic:
    # .isna() creates a table of True/False (True if missing)
    # .sum(axis=1) counts the "Trues" across the columns for each row
    missing_series = work_df.isna().sum(axis=1)
    total_cols = work_df.shape[1]

    # Build the result DataFrame
    counts_df = pd.DataFrame({
        'missing': missing_series,
        'total': total_cols,
        'available': total_cols - missing_series
    })

    # Sort: Alkanes with the fewest missing values first
    return counts_df.sort_values("missing")


# ---------- 2. Feature Availability (Column-by-Column) ----------
def feature_availability(df):
    # Drop 'name' from stat calculations if it exists
    if 'name' in df.columns:
        work_df = df.drop(columns=['name'])
    else:
        work_df = df

    # .isna().sum() (default axis=0) counts missing values down each column
    missing_counts = work_df.isna().sum()
    total_rows = len(work_df)

    # Build stats table
    stats_df = pd.DataFrame({
        'missing': missing_counts,
        'total': total_rows,
        'available': total_rows - missing_counts
    })

    stats_df["availability_rate"] = (stats_df["available"] / stats_df["total"]) * 100

    # Sort: Best features (100% available) at the top
    return stats_df.sort_values(["availability_rate", "available"], ascending=[False, False])


# ---------- Main Execution ----------
if __name__ == "__main__":
    # 1. Load your CSV
    df = pd.read_csv('alkanes_Stenutz.csv')
    print(f"Loaded data with {len(df)} rows and {len(df.columns)} columns.")

    # 2. Run Per-Alkane Analysis
    df_alkanes = per_alkane_missing_counts(df)
    print("\n=== Per-alkane missing counts (Best 5) ===")
    print(df_alkanes.head(5))

    print("\n=== Per-alkane missing counts (Worst 5) ===")
    print(df_alkanes.tail(5))

    # 3. Run Feature Analysis
    df_features = feature_availability(df)
    print("\n=== Feature availability (Best to Worst) ===")
    print(df_features[["missing", "available", "availability_rate"]])

    # 4. Show worst features specifically
    print("\n=== Most incomplete features (Worst 10) ===")
    worst = df_features.sort_values(["availability_rate", "missing"], ascending=[True, False]).head(10)
    print(worst[["missing", "total", "availability_rate"]])