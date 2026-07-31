import os
import pandas as pd

# 1. Load dataset directly from your Downloads folder
raw_data_path = (
    r"C:\Users\Soniamannepuli\Downloads\d2c_marketing_funnel_data.csv"
)

df = pd.read_csv(raw_data_path)

# 2. Fill missing channel values if any
df["channel"] = df["channel"].fillna("Direct")

# 3. Derive Purchase Flag directly from Revenue
# If revenue > 0, the customer completed a purchase!
df["is_purchase"] = (df["revenue"] > 0).astype(int)

# 4. Group by Marketing Channel and Device
channel_summary = (
    df.groupby(["channel", "device"])
    .agg(
        total_sessions=("session_id", "count"),
        total_purchases=("is_purchase", "sum"),
        total_revenue=("revenue", "sum"),
        avg_order_value=("order_value", "mean"),
    )
    .reset_index()
)

# 5. Calculate Conversion Rate
channel_summary["overall_conversion_rate"] = (
    channel_summary["total_purchases"] / channel_summary["total_sessions"]
)

# Format conversion rate as percentage for display
channel_summary["conversion_rate_pct"] = (
    (channel_summary["overall_conversion_rate"] * 100).round(2).astype(str)
    + "%"
)

# 6. Print Fixed KPI Summary Table
print("🎉 ACCURATE KPI SUMMARY:")
print(
    channel_summary[[
        "channel",
        "device",
        "total_sessions",
        "total_purchases",
        "conversion_rate_pct",
        "total_revenue",
    ]]
)

# 7. Save corrected CSV for Tableau
output_dir = "data/processed"
os.makedirs(output_dir, exist_ok=True)
channel_summary.to_csv(
    os.path.join(output_dir, "channel_kpi_summary_accurate.csv"), index=False
)