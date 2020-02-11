from pprint import pprint

with open('recipes.txt', encoding='UTF-8') as f:
    lst = []
    index_lst = []
    for lines in f:
        lst.append(lines.strip())
        a = lines.strip().replace(' ', '')
        b = a.replace('-', '')
        if b.isalpha() == True:
            dishes = lines.strip()
            lst.remove(lines.strip())
        elif lines.strip() == '':
            lst.remove(lines.strip())
        elif lines.strip().isdigit() == True:
            quantity = lines.strip()
            lst.remove(lines.strip())
            index = int(quantity)
            index_lst.append(index)
    ingredients_lst = []
    for i in index_lst:
        ingredients = lst[0:i]
        lst[0:i] = []
        ingredients_lst.append(ingredients)
    print(ingredients_lst)
        
        
            
        
    
            
    