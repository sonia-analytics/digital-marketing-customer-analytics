# Digital Marketing & Customer Analytics Case Study

## Executive Summary
This project analyzes multi-channel web clickstream and customer engagement datasets to evaluate acquisition funnels, digital campaign conversion rates, and marketing attribution models. 

## Business Problem & Objectives
* **Identify Drop-Off Bottlenecks:** Pinpoint where customers abandon the purchasing journey across desktop and mobile channels.
* **Evaluate Channel Performance:** Compare campaign conversion rates and ROI across Paid Ads, Organic Search, Social, and Email channels.
* **Attribution Modeling:** Assess revenue impact using First-Touch vs. Last-Touch digital attribution models.

## Tech Stack & Tools
* **Data ETL & Blending:** Alteryx (Workflow Automation), Python (Pandas)
* **Analytics & Attribution:** Adobe Analytics framework logic, SQL
* **Data Visualization:** Tableau Desktop / Tableau Public

## Key Insights & Findings
1. **Funnel Drop-Off:** The largest drop-off occurred between **Add-to-Cart** and **Checkout** (42% drop rate on mobile devices).
2. **Channel Performance:** Paid Social generated highest overall web traffic, but Email campaigns achieved the highest conversion rate (4.8% CVR).
3. **Attribution Variance:** Last-Touch attribution overestimated Paid Search revenue by 18% compared to multi-channel touchpoint models.

## Tableau Dashboard
https://public.tableau.com/views/D2C_Digital_Marketing_Analytics_Dashboard/DataFindingsInsights?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

## Dashboard Preview
<img width="1906" height="1092" alt="Screenshot 2026-07-31 004828" src="https://github.com/user-attachments/assets/0cfd642b-afde-422d-bfac-b37c53e510be" />

## How to Run the Workflow
1. Open `workflows/alteryx_marketing_etl.yxmd` in Alteryx Designer to inspect data cleaning and blending stages.
2. Run the workflow to output `data/processed/marketing_attribution_summary.csv`.
3. Open `dashboards/marketing_analytics.twbx` in Tableau Desktop or view via Tableau Public.
