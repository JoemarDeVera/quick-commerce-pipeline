# Quick Commerce ETL Pipeline — v1

## Overview
A beginner-friendly ETL (Extract, Transform, Load) pipeline that processes nearly **1 million quick commerce orders** from Kaggle into a SQLite database using a star schema. Includes a Jupyter Notebook with SQL analysis and data visualizations.

---

## About the Dataset
This dataset is a **synthetic yet realistic simulation** of Quick Commerce (Q-Commerce) business data with nearly **1 Million Records**, inspired by popular platforms such as:

**Blinkit, Zepto, Swiggy Instamart, Dunzo, JioMart, BigBasket, Amazon Now, and Flipkart Minutes**

It is designed for learners, analysts, and data science enthusiasts who want to practice real-world data analytics workflows using Python, Pandas, and data visualization tools.

**Source:** [Kaggle — Quick Commerce Dataset by Rohit Grewal](https://www.kaggle.com/datasets/rohitgrewal/quick-commerce-dataset)

---

## Tech Stack
- **Language:** Python 3.13
- **Database:** SQLite
- **Libraries:** Pandas, SQLAlchemy, Matplotlib, Seaborn
- **Notebook:** Jupyter

---

## Project Structure
```
quick-commerce-pipeline/
├── extract.py        ← loads data from Kaggle
├── transform.py      ← builds star schema
├── load.py           ← saves to SQLite
├── pipeline.py       ← runs full ETL
├── analysis.ipynb    ← SQL analysis + visualizations
├── quick_commerce.db ← SQLite database
└── quick_commerce_dashboard.png
```

---

## Star Schema
```
fact_orders
├── dim_customers
├── dim_delivery_partners
└── dim_promotions
```

---

## Key SQL Insights

| Question | Finding |
|----------|---------|
| Avg delivery time | 16.51 minutes |
| Discounted vs non-discounted orders | ₹712 vs ₹476 avg order value |
| Distance effect on delivery | 0-5km=13.67min, 5-10km=16.36min, 10+km=19.27min |
| Most common order size | Medium (₹300-800) at 49.1% |
| Delivery partner consistency | All partners avg ~16.5 mins |
| Top ordering age group | 46+ age group with 314,724 orders |

---

## How to Run
1. Clone the repo
2. Install dependencies: `pip install pandas sqlalchemy kagglehub matplotlib seaborn`
3. Run pipeline: `python pipeline.py`
4. Open `analysis.ipynb` in Jupyter

---

## Related Projects
- [v2 - PostgreSQL + Validation](https://github.com/JoemarDeVera/quick-commerce-pipeline-v2)
- [v3 - Apache Airflow](https://github.com/JoemarDeVera/quick-commerce-pipeline-v3)
- [v4 - dbt Transformations](https://github.com/JoemarDeVera/quick-commerce-pipeline-v4)
- [v5 - Power BI Dashboard](https://github.com/JoemarDeVera/quick-commerce-pipeline-v5)