import sqlite3

def load(dim_customers, dim_partners, dim_promotions, fact_orders):
    print("Loading into SQLite...")

    conn = sqlite3.connect("quick_commerce.db")

    dim_customers.to_sql("dim_customers", conn, if_exists="replace", index=False)
    print("dim_customers loaded!")

    dim_partners.to_sql("dim_delivery_partners", conn, if_exists="replace", index=False)
    print("dim_delivery_partners loaded!")

    dim_promotions.to_sql("dim_promotions", conn, if_exists="replace", index=False)
    print("dim_promotions loaded!")

    fact_orders.to_sql("fact_orders", conn, if_exists="replace", index=False)
    print("fact_orders loaded!")

    conn.commit()
    conn.close()
    print("\nDatabase saved as quick_commerce.db!")

if __name__ == "__main__":
    from extract import extract
    from transform import transform
    df = extract()
    dim_customers, dim_partners, dim_promotions, fact_orders = transform(df)
    load(dim_customers, dim_partners, dim_promotions, fact_orders)