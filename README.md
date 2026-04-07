# SP500-EDA
Exploratory Data Analysis of S&P 500 companies using Python, Pandas, and the Yahoo Finance API.

## Data Project Architecture Plan

**1. Problem Definition & Business Goal**
Analyze the fundamental metrics of S&P 500 companies to understand market composition, uncover financial correlations, and spot anomalies across different sectors.

**2. Data Source & Input**
**Primary Source:** A static dataset (`sp500_companies.csv`).
**Secondary Source (API):** Live data extraction using the `yfinance` API to impute missing values dynamically.
**Structure:** Cross-sectional data where each row represents a single S&P 500 company.
**Key Features:** Sector, Exchange, Market Cap, EBITDA, Revenue Growth, Current Price, and Full-Time Employees.

**3. Target Variable / Output (Research Focus)**
Since this is an Exploratory Data Analysis (EDA) phase, there is no single target variable to predict. The main objective is to identify correlations, 
distributions, and anomalies within the financial metrics across the market.

**4. Evaluation Metric & Deliverables**
The final product is a fully functional, clean pipeline script containing:
* Data cleaning and imputation logic (API fetching & statistical mode filling).
* A comprehensive Correlation Heatmap to identify multicollinearity between metrics.
* Sector breakdown dashboards (comparing company count, total market cap, and revenue growth).
* A comparative visual dashboard analyzing the Top 12 market-cap leaders.

**5. The Baseline**
The overarching macroeconomic state of the S&P 500 index and standard sector-level averages.

**6. Tech Stack & Tools**
**Data Extraction API:** `yfinance`
**Data Processing:** `pandas`, `numpy`
**Data Visualization:** `matplotlib`, `seaborn`

---

**Acknowledgments:** The initial inspiration and baseline code for the data visualizations in this project were adapted from the excellent Kaggle notebook by 
Faryar Memon. 
I modified the code to run as a standalone Python script, updated deprecated functions to modern Seaborn standards, and added dynamic API fetching to handle missing values.
