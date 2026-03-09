from extract import extract
from transform import transform
from load import load

print("tarting Quick Commerce Pipeline...\n")

# Step 1: Extract
df = extract()

# Step 2: Transform
dim_customers, dim_partners, dim_promotions, fact_orders = transform(df)

# Step 3: Load
load(dim_customers, dim_partners, dim_promotions, fact_orders)

print("\nPipeline complete!")