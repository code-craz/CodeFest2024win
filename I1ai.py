import pandas as pd
import csv

# Function to calculate the total price
def calculate_total_price(price_inr, price_usd):
    return price_inr + price_usd * 83

# Read data from CSV file using Pandas
filename = 'Cleaned_data_version2_sanath.csv'  # Replace with your actual CSV file name
df = pd.read_csv(filename)

# Combine the functionality with the existing code
def suggest_products(category, sub_category):
    category = category.lower().strip()
    sub_category = sub_category.lower().strip()
    print("Category given is ", category, "\n")
    print("Sub category given is ", sub_category, "\n")
    
    # Filter data based on category and subcategory
    filtdf = df[(df['category'].str.lower().str.strip() == category) & (df['sub-category-1'].str.lower().str.strip() == sub_category)]
    sortfiltdf = filtdf.sort_values(['Reviews'], axis=0, ascending=[False])
    
    if not sortfiltdf.empty:
        # Display the suggested products as before
        print(f"Most popular products under {category} -> {sub_category}")
        print(f"Unique names under {category} -> {sub_category} are: ")
        unique_product_names = set(sortfiltdf['Product_Name'])
        for product_name in unique_product_names:
            print(product_name)

        common_ingredients = sortfiltdf['ingredients'].unique()
        if len(common_ingredients) > 0:
            print("\nCommon ingredients used in products like this are: ")
            for ingredient in common_ingredients:
                print(f"- {ingredient}")

        print("\nSuggested price range per 100g ")
        inrprice = sortfiltdf['India priceINR per 100g']
        usdprice = sortfiltdf['US price $ per 100g']
        mininr = min(inrprice)
        maxinr = max(inrprice)
        minusd = min(usdprice)
        maxusd = max(usdprice)

        if mininr == maxinr:
            print("India: Price your product around ", mininr, "rupees.")
        else:
            print("India: Price your product between ", mininr, "and", maxinr, "rupees.")
        if maxusd == minusd:
            print("USA: Price your product around ", minusd, "dollars.")
        else:
            print("USA: Price your product between ", minusd, "and", maxusd, "dollars.")
    else:
        print(f"No products found under {category} -> {sub_category}.")

# Get user input
user_category = input("Enter the category: ")
user_sub_category = input("Enter the sub category: ")

# Suggest products and prices
suggest_products(user_category, user_sub_category)
