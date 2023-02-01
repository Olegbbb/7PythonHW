import controller
def main_menu() -> int:
    print('Главное меню.')
    menu_list = ['Показать все контакты',
                 'Открыть файл',
                 'Сохранить файл',
                 'Создать контакт',
                 'Найти контакт',
                 'Изменить контакт',
                 'Удалить контакт',
                 'Выход'
                 ]
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')
    user_input = int(input('Введи команду >: '))
    # TODO: сделать валидацию
    return user_input


def show_all(db: list):
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()


def db_success(db: list):
    if db:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False


def exit_program(master: list,slave: list):
    if master == slave:
        print('Завершение программы.')
        exit()
    else:
        a = input('В список внесены изменения. 1 - вернуться в меню, любая клавиша - не сохранять: ')
        if a == '1':
            main_menu()
        else:
            print('Завершение программы.')
            exit()



def create_contact():
    print('Создание нового контакта.')
    new_contact = dict()

    new_contact['lastname'] = input('\tВведите фамилию >: ')
    new_contact['firstname'] = input('\tВведите имя >: ')
    new_contact['phone'] = input('\tВведите телефон >: ')
    new_contact['comment'] = input('\tВведите комментарий >: ')
    return new_contact

def find_contact(db: list) -> dict:
    if db:
        search = input("Введите имя, фамилию, номер или комментарий: ")
        for i in range(len(db)):
            for v in db[i].values():
                    if search in v:
                        for v in db[i].values():
                            print(f'{v}', end=' ')                 
                        print()
                        return i
    else: print('Телефонная книга пуста или не открыта')
    



def change_contact(db: list, i:int ):    
    print(f"Вы хотите изменить этот контакт?")
    a = input("Введите '0' для отмены или любую клавишу для подтверждения: " )
    if a != '0':
        db[i]['lastname'] = input('\tВведите фамилию >: ')
        db[i]['firstname'] = input('\tВведите имя >: ')
        db[i]['phone'] = input('\tВведите телефон >: ')
        db[i]['comment'] = input('\tВведите комментарий >: ')
        print('Контакт изменен')
    else:
        main_menu()

def delete_contact(db: list) -> list:
    search = input("Введите имя, фамилию, номер или комментарий: ")
    for i in range(len(db)):
        for v in db[i].values():
                if search in v:
                    print(db[i])
                    print('Контакт удален')
                    return db[i]







