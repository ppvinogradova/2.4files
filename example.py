with open('recipes.txt', encoding='UTF-8') as f:
    dishes = {}
    while True:
        name_dish = f.readline().strip()
        if name_dish == '':
            break  # конец файла
        count_ingrs = int(f.readline().strip())
        ingrs = []
        for index_ingr in range(count_ingrs):
            ingr = f.readline().split(' | ')
            ingrs.append({'ingredient_name': ingr[0], 'quantity': int(ingr[1]), 'measure':ingr[2].strip()})
        dishes[name_dish] = ingrs
        f.readline()
    print(dishes)