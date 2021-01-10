cook_book = {}
cook = {}
cook_list = []

with open('recipes.txt', 'r', encoding='utf-8') as f:
    recipes = f.readlines()

for cook_r in recipes:
    cook_r = cook_r.rstrip().split()
    if '|' not in cook_r and [a for a in cook_r if a.isdigit() is False]:
        cook_list = []
        cook_book[str(' '.join(cook_r))] = cook_list

    elif '|' in cook_r:
        cook_r = [a for a in cook_r if a != '|']
        cook = {'ingredient_name': ' '.join(cook_r[:-2]), 'quantity': cook_r[-2], 'measure': cook_r[-1]}
        cook_list.append(cook)

for key, value in cook_book.items():
    print(key, value)

