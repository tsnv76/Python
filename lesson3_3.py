my_list = ['Иван', 'Мария', 'Петр', 'Илья', 'Михаил', 'Прасковья', 'Николай', 'Надежда']

def thesaurus(inp_list):
    out_dict = {}
    for item in my_list:
        name_list = filter(lambda fl: fl.startswith(item[0]), my_list)
        key = item[0]
        out_dict[key] = list(name_list)
    return out_dict

print(my_list)
print(thesaurus(my_list))

