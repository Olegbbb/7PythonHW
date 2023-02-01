db_list = []
db_listCheck = []

def read_db(path: str):
    global db_list
    global db_listCheck
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            id_dict = dict()
            line = line.strip().split(';')
            id_dict['lastname'] = line[0]
            id_dict['firstname'] = line[1]
            id_dict['phone'] = line[2]
            id_dict['comment'] = line[3]
            db_list.append(id_dict)
    db_listCheck.extend(db_list)




def save_contact(path: str):
    global db_list
    with open(path, 'w', encoding='UTF-8') as file:
        for i in range(len(db_list)):
            [file.write(v + ';') for v in db_list[i].values()]
            file.write('\n')
    print('Контакты сохранены')

