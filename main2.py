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
    #pprint(ingredients_d_list)
    for i in index_lst:
        ingredients = ingredients_d_list[0:i]
        ingredients_d_list[0:i] = []
        ingredients_lst.append(ingredients)
    #pprint(ingredients_lst)
    q = len(dishes_lst)
    book = {}
    cook_book = book.fromkeys(dishes_lst)
    #for n in range(0, q):

    pprint(cook_book)
    
            
    