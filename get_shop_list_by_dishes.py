cook_book = {}
cook = {}
cook_list = []
sort_dict = {}
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


def get_shop_list_by_dishes(dishes, person):
    all_sort = {}
    for value in dishes:
        if value in cook_book.keys():
            for title in cook_book[value]:
                name = title.pop('ingredient_name')
                if name in all_sort.keys():
                    title['quantity'] = int(title['quantity']) * person + int(all_sort[name]['quantity'])
                    all_sort[name] = title
                    sort_dict[name] = title
                else:
                    title['quantity'] = int(title['quantity']) * person
                    all_sort[name] = title
                    sort_dict[name] = title
        else:
            print(value, ' Такого блюда нет в книге')

    return print(all_sort)


def print_shop_list(some_dict):
    for key, value in some_dict.items():
        print(f'{key} : {value}')


get_shop_list_by_dishes(['Омлет', 'Утка по-пекински', 'Запеченный картофель'], 2)
print_shop_list(sort_dict)