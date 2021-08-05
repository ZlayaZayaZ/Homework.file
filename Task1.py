import os

path_cook_book = os.path.join(os.getcwd(), 'cook_book.txt')
with open(path_cook_book, mode='r', encoding='utf-8') as file:
    cook_book = dict()
    for line in file:
        name_of_the_dish = str(line.strip())
        cook_book[name_of_the_dish] = []
        amount_of_ingredients = int(file.readline())
        for i in range(amount_of_ingredients):
            a = dict()
            string = file.readline()
            list_string = string.split(' | ')
            a['ingredient_name'] = list_string[0]
            a['quantity'] = list_string[1]
            a['measure'] = list_string[2].strip()
            cook_book[name_of_the_dish].append(a)
        file.readline()

# print(cook_book)

def get_shop_list_by_dishes(dishes, person):
  list_by_dishes = dict()
  for dish in dishes:
    for ingredient in cook_book[dish]:
      name_ing = ingredient['ingredient_name']
      if name_ing not in list_by_dishes:
        ingredient['quantity'] = int(ingredient['quantity']) * person
        list_by_dishes[ingredient.pop('ingredient_name')] = ingredient
      else:
        list_by_dishes[name_ing]['quantity'] += int(ingredient['quantity']) * person
  return list_by_dishes

print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
