# Recipe Finder
# https://dailypythonprojects.substack.com/p/recipe-finder
import json

ingredients = []
ingr_str = ""
count_ingr = 0
count = 0
count_lst = []
count_comma = 0

ingr = input("Enter a list of ingredients, separated by commas: ")

for let in ingr:
    if let == ",":
        ingredients.append(ingr_str)
        ingr_str = ""
    else:
        ingr_str = ingr_str + let
ingredients.append(ingr_str)

    
print("Here are some recipes you can make:")
print()
print("Recipe: ", end = "")


input_json = open('recipes.json', 'r', encoding='utf-8')

recipes_dict = json.load(input_json)

for dic in range(len(recipes_dict)):
    for ingr_lst in range(len(recipes_dict[dic]["ingredients"])):
        if recipes_dict[dic]["ingredients"][ingr_lst] in ingredients:
            count += 1
    count_lst.append(count)
    count = 0

for count_dic in range(len(count_lst)):
    if count_lst[count_dic] == max(count_lst):
        print(recipes_dict[count_dic]["name"])
        print("Ingredients: ", end = "")
        for ingred in range(len(recipes_dict[count_dic]["ingredients"])):
            if count_comma < len(recipes_dict[count_dic]["ingredients"]) - 1:
                print(recipes_dict[count_dic]["ingredients"][ingred], end = "")
                print(", ", end = "")
                count_comma += 1
            else:
                print(recipes_dict[count_dic]["ingredients"][ingred], end = "")
            
        print("\nInstructions:", recipes_dict[count_dic]["instructions"])
