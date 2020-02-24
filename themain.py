from pprint import pprint

with open('recipes.txt', encoding='UTF-8') as f:
    lst = []
    index_lst = []
    dishes_lst = []
    for lines in f:
        lst.append(lines.strip())
        a = lines.strip().replace(' ', '')
        b = a.replace('-', '')
        if b.isalpha() == True:
            dishes = lines.strip()
            dishes_lst.append(dishes)
            lst.remove(lines.strip())
        elif lines.strip() == '':
            lst.remove(lines.strip())
        elif lines.strip().isdigit() == True:
            quantity = lines.strip()
            lst.remove(lines.strip())
            index = int(quantity)
            index_lst.append(index)
    ingredients_lst = []
    ingredients_d_list = []
    for ing in lst:
        l = ing.split(' | ')
        ingredients_dicts = {'ingredient_name':l[0], 'quantity':l[1], 'measure':l[2]}
        ingredients_d_list.append(ingredients_dicts)
    for i in index_lst:
        ingredients = ingredients_d_list[0:i]
        ingredients_d_list[0:i] = []
        ingredients_lst.append(ingredients)
    cook_book = dict(zip(dishes_lst, ingredients_lst))
    #pprint(cook_book)
    dishes_list = input('Введите названия блюд через запятую ').split(', ')
    persons = int(input('Введите количество человек '))
    def get_shop_list_by_dishes(dishes, person_count):
        ingrs = []
        names = []
        for dish in dishes:
            n = dishes.count(dish)
            if dish in cook_book.keys():
                ingr = cook_book.get(dish)
                for i in ingr:
                    ingrs.append(i)
                    try:
                        name = i.pop('ingredient_name')
                    except KeyError:
                        break
                    else:
                        names.append(name)         
        n_names = n*names
        #print(n_names)      
        a_list = []
        for name in n_names:
            n = n_names.count(name)
            a = n * persons
            a_list.append(a)
        mul_ingrs = []
        for z in zip(a_list, ingrs):
            mul = z[0] * int(z[1].get('quantity'))
            z[1]['quantity'] = mul
            mul_ingrs.append(z[1])
        shop_list = dict(zip(names, mul_ingrs))
        pprint(shop_list)
    get_shop_list_by_dishes(dishes_list, persons)
    