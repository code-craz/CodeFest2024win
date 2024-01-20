#Import necessary module
import pandas as pd 

#Read csv file
df= pd.read_csv('Cleaned_data_version2_sanath.csv')

#Print index
print("Printing index")
print(df.keys)

#Create function to suggest products
def suggest_products(category, sub_category):
    #Convert to lower case and remove trailing or leading whitespaces
    category= category.lower().strip()
    sub_category= sub_category.lower().strip()
    print("Category given is ", category, "\n")
    print("Sub category given is ", sub_category, "\n")
    filtdf= df[(df['category'].str.lower().strip() == category & df['sub_category'].str.strip().str.lower())]
    sortfiltdf= filtdf.sort_values(['Reviews'], axis=0, ascending=[False])
    if sortfiltdf.empty:
        numfiltprods= len(sortfiltdf)
        print("There were ", numfiltprods, "products\n")
        numtodisplay= min(2, numfiltprods)
        print("I am showing ", numtodisplay, "products\n")
        shortlistfiltdf= sortfiltdf.head(numtodisplay)
        print(f"Most popular products under {category} -> {sub_category}")
        print(f"Unique names under {category} -> {sub_category} are: ")
        unique_product_names= set()
        for product_name in sortfiltdf['Product_name']:
            unique_product_names.add(product_name)
            if len(unique_product_names)>= 2:
                break
        for product_name in unique_product_names:
            print(product_name)
        
        common_ingredients = shortlistfiltdf['ingredients'].unique()
        if len(common_ingredients) > 0:
            print("\nCommon ingredients used in products like this are: ")
            for ingredient in common_ingredients:
                