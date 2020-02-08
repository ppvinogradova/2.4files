
with open('recipes.txt', encoding='UTF-8') as f:
    lst = []
    for lines in f:
        lst.append(lines.strip())

#для начала использую функцию для создания списка списков блюд
def split_on(what, delimiter = ''):
    splitted = [[]]
    for item in what:
        if item == delimiter:
            splitted.append([])
        else:
            splitted[-1].append(item)
    return splitted

a = split_on(lst)

#функция превращения в словарь
def dict_create(txt):
    dishes_list = [] 
    ingredients_list = []
    for line in txt:
        dishes_list.append(line[0])
        for ing in line[1:]:
            ingredients_list.append(ing)  #создан список названий блюд и список ингредиентов
    #print(ingredients_list)

    #for dish in dishes_list:
        #cook_book = {dish: []}
        #print(cook_book) #здесь создается "верхний" уровень словаря
    ingred_list = []
    num_lst = []
    for q in ingredients_list:
        if len(q) != 1:
            a = q.split(' | ')
            ingred = {'ingredient_name' : a[0], 'quantity' : a[1], 'measure' : a[2]}
            ingred_list.append(ingred) #делаем словари ингредиентов
        else:
            num_d = int(q)
            num_lst.append(num_d) #для какого-то использования числа ингредиентов
    
    #теперь задача засунуть в словарь словари с ингредиентами в тех количествах, которые указаны в num_d...

    #for n in num_lst:
        #ingred_list.pop(0:n) #pop не хочет возвращать срез списка. Какие еще есть для этого варианты?
#print(a)
dict_create(a)     

            
    
    

    










