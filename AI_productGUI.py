import pandas as pd
import tkinter as tk
from tkinter import ttk


# Read csv file
df = pd.read_csv('Cleaned_data_version2_sanath.csv')


# Function to calculate the total price and profit
def calculate_total_price_and_profit(price_inr, price_usd):
   total_price = price_inr + price_usd * 83
   profit = total_price * 0.10  # Assuming a 10% profit margin
   return total_price, profit


# Create function to suggest products
def suggest_products():
   category = category_var.get().lower().strip()
   sub_category = sub_category_var.get().lower().strip()


   result_text.delete(1.0, tk.END)  # Clear previous results


   filtdf = df[(df['category'].str.lower().str.strip() == category) & (df['sub-category-1'].str.lower().str.strip() == sub_category)]
   sortfiltdf = filtdf.sort_values(['Reviews'], axis=0, ascending=[False])


   if not sortfiltdf.empty:
       numfiltprods = len(sortfiltdf)
       numtodisplay = min(2, numfiltprods)
       shortlistfiltdf = sortfiltdf.head(numtodisplay)


       result_text.insert(tk.END, f"Most popular products under {category} -> {sub_category}\n")
       result_text.insert(tk.END, f"Unique names under {category} -> {sub_category} are: \n")


       unique_product_names = set()
       for product_name in sortfiltdf['Product_Name']:
           unique_product_names.add(product_name)
           if len(unique_product_names) >= 2:
               break


       for product_name in unique_product_names:
           result_text.insert(tk.END, f"{product_name}\n")


       common_ingredients = shortlistfiltdf['ingredients'].unique()
       if len(common_ingredients) > 0:
           result_text.insert(tk.END, "\nCommon ingredients used in products like this are: \n")
           for ingredient in common_ingredients:
               result_text.insert(tk.END, f"- {ingredient}\n")


       result_text.insert(tk.END, "\nSuggested price range per 100g \n")
       inrprice = shortlistfiltdf['India priceINR per 100g']
       usdprice = shortlistfiltdf['US price $ per 100g']
       mininr = min(inrprice)
       maxinr = max(inrprice)
       minusd = min(usdprice)
       maxusd = max(usdprice)


       if mininr == maxinr:
           result_text.insert(tk.END, f"India: Price your product around {mininr} rupees.\n")
       else:
           result_text.insert(tk.END, f"India: Price your product between {mininr} and {maxinr} rupees.\n")


       if maxusd == minusd:
           result_text.insert(tk.END, f"USA: Price your product around {minusd} dollars.\n")
       else:
           result_text.insert(tk.END, f"USA: Price your product between {minusd} and {maxusd} dollars.\n")


       # Calculate and display the total price and profit
       total_price, profit = calculate_total_price_and_profit(mininr, minusd)
       result_text.insert(tk.END, f"\nTotal Price (INR + USD converted to INR): {total_price} rupees\n")
       result_text.insert(tk.END, f"Profit (assuming 10% profit margin): {profit} rupees\n")
   else:
       result_text.insert(tk.END, f"No products found under {category} -> {sub_category}.\n")


# Create GUI
root = tk.Tk()
root.title("Product Suggestion")


# Create and place widgets
category_label = ttk.Label(root, text="Select the category:")
category_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")


categories = df['category'].unique()
category_var = tk.StringVar(value=categories[0])
category_dropdown = ttk.Combobox(root, textvariable=category_var, values=categories)
category_dropdown.grid(row=0, column=1, padx=10, pady=10)


sub_category_label = ttk.Label(root, text="Select the sub category:")
sub_category_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")


sub_categories = df['sub-category-1'].unique()
sub_category_var = tk.StringVar(value=sub_categories[0])
sub_category_dropdown = ttk.Combobox(root, textvariable=sub_category_var, values=sub_categories)
sub_category_dropdown.grid(row=1, column=1, padx=10, pady=10)


suggest_button = ttk.Button(root, text="Suggest Products", command=suggest_products)
suggest_button.grid(row=2, column=0, columnspan=2, pady=10)


result_text = tk.Text(root, height=15, width=50)
result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
