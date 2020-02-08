#ЧИСТОВИК (без переменных в глобальном контексте)
    
def split_on(what, delimiter = ''):
    splitted = [[]]
    for item in what:
        if item == delimiter:
            splitted.append([])
        else:
            splitted[-1].append(item)
    return splitted
    
def dict_create(txt):
    split_on(txt)
    dishes_list = []
    for line in txt:
        dishes_list.append(line[0])
    #for dish in dishes_list:    
    return 'jujgkjh'
    


with open('recipes.txt', encoding='UTF-8') as f:
    lst = []
    for lines in f:
        lst.append(lines.strip())
    print(dict_create(f))







