import csv
import re
import random

def assign_safety_rating(ingredient_list):
    # Manually assign safety rating for common ingredients
    safety_ratings = {'water': 1, 'aqua': 1, 'eau': 1}

    # Sort the ingredient list in alphabetic order
    sorted_ingredients = sorted(ingredient_list)

    # Assign safety rating randomly for each ingredient
    safety_index = {}
    for index, ingredient in enumerate(sorted_ingredients):
        if ingredient.lower() in safety_ratings:
            safety_index[ingredient] = 1
        else:
            safety_index[ingredient] = (index % 3) + 1

    return safety_index

def read_csv(file_path):
    ingredients = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:
                ingredient = row[-2].strip()
                ingredients.extend(re.split(r', | ', ingredient))
    return ingredients

def main():
    # Provide the path to your CSV file
    csv_file_path = 'half.csv'

    # Read ingredients from the CSV file
    ingredients = read_csv(csv_file_path)

    # Assign safety ratings to ingredients
    safety_ratings = assign_safety_rating(ingredients)

    # Display the sorted ingredients and their safety ratings
    for ingredient in sorted(safety_ratings.keys()):
        print(f"{ingredient}: Safety Rating {safety_ratings[ingredient]}")

if __name__ == "__main__":
    main()
