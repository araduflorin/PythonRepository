import csv


def csv_reader_categories():
    list_categories = []
    with open('categories.csv', 'r+') as file:
        categories = csv.reader(file)
        for item in categories:
            list_categories.append(item)
    return list_categories


def add_categories():
    while True:
        with open('categories.csv', mode='a', newline='') as file:
            list_add_categories = csv_reader_categories()
            print(list_add_categories)
            var_category = input("Adauga o noua categorie: ").lower()
            list_categories_new = [i[0].lower() for i in list_add_categories]
            if var_category not in list_categories_new:
                writer = csv.writer(file)
                writer.writerow([var_category])
                exit_opt = input('Continuati adaugarea? (d\\n) ')
                if exit_opt == 'd':
                    continue
                elif exit_opt == 'n':
                    break
            else:
                print('Categoria exista deja')
    return


def csv_reader_tasks():
    list_tasks = []
    with open('tasks.csv', 'r+') as file:
        tasks = csv.reader(file)
        for task in tasks:
            list_tasks.append(task)
    return list_tasks


def add_tasks():
    while True:
        with open('tasks.csv', mode='a', newline='') as file:
            list_add_tasks = csv_reader_tasks()
            list_categories = csv_reader_categories()
            print(list(map(print, sorted(list_add_tasks, key=lambda cat: cat[3]))))

            check_tasks = []
            for index, row in enumerate(list_add_tasks):
                check_tasks.append(row[0])
            print('Verifica task:', check_tasks)

            list_check_category = [cat for lst_cat in list_categories for cat in lst_cat]
            print(list_check_category)
            var_task = input("Adauga un task: ").lower()
            var_date = input("Adauga data: ").lower()
            var_person = input("Adauga persoana responsabila: ").lower()
            var_category = input("Adauga categoria: ").lower()
            list_tasks = [var_task, var_date, var_person, var_category]

            if var_task not in check_tasks:
                if var_category in list_check_category:
                    writer = csv.writer(file)
                    writer.writerow(list_tasks)
                    exit_opt = input('Continuati adaugarea? (d\\n)')
                    if exit_opt == 'd':
                        continue
                    elif exit_opt == 'n':
                        break
                else:
                    print('Categoria nu exista!')
                    continue
            else:
                print('Task-ul exista deja!')
                continue
    return


def edit_task():
    while True:
        list_tasks = csv_reader_tasks()
        list_categories = csv_reader_categories()
        check_task = []
        print("Lista task-uri pentru editat: ")
        for index, row in enumerate(list_tasks):
            # for r in row:
                # print(index, r)
            print(index, row)
            check_task.append(row[0])
        print("Task-uri existente:", check_task)

        list_check_category = [cat for lst_cat in list_categories for cat in lst_cat]

        index_task = int(input("Introduceti nr task-ului de modificat: "))
        var_task = input("Editeaza task-ul: ").lower()
        var_date = input("Editeaza data: ").lower()
        var_person = input("Editeaza persoana responsabila: ").lower()
        var_category = input("Editeaza categoria: ").lower()
        list_tasks_update = [var_task, var_date, var_person, var_category]

        list_tasks[index_task] = list_tasks_update

        if var_task not in check_task:
            if var_category in list_check_category:
                with open('tasks.csv', mode='w', newline='') as csv_file:
                    write = csv.writer(csv_file)
                    for task in list_tasks:
                        write.writerow(task)
                    print("Task-ul a fost modificat:")
                    for index, row in enumerate(list_tasks):
                        print(index, row)
                    exit_opt = input('Continuati editarea? (d\\n)')
                    if exit_opt == 'd':
                        continue
                    elif exit_opt == 'n':
                        break
            else:
                print(f'Categoria {var_category} nu exista!')
                continue
        else:
            print(f'Task-ul {var_task} exista deja!')
            continue
    return


def delete_task():
    while True:
        list_tasks = csv_reader_tasks()

        print("Lista task-uri pentru sters: ")
        for index, row in enumerate(list_tasks):
            print(index, row)

        index_task = int(input("Introduceti nr task-ului pe care doriti sa il stergeti: "))
        list_tasks.remove(list_tasks[index_task])

        with open('tasks.csv', mode='w', newline='') as csv_file:
            write = csv.writer(csv_file)
            for task in list_tasks:
                write.writerow(task)
            exit_opt = input('Continuati stergerea? (d\\n)')
            if exit_opt == 'd':
                continue
            elif exit_opt == 'n':
                break
    return


def sort_category_asc():
    sort_tasks = csv_reader_tasks()
    list(map(print, sorted(sort_tasks, key=lambda cat: cat[3])))
    return


def sort_category_desc():
    sort_tasks = csv_reader_tasks()
    list(map(print, sorted(sort_tasks, key=lambda cat: cat[3], reverse=True)))
    return


def sort_task_asc():
    sort_tasks = csv_reader_tasks()
    list(map(print, sorted(sort_tasks, key=lambda cat: cat[0])))
    return


def sort_task_desc():
    sort_tasks = csv_reader_tasks()
    list(map(print, sorted(sort_tasks, key=lambda cat: cat[0], reverse=True)))
    return


def sort_date_asc():
    sort_tasks = csv_reader_tasks()
    list(map(print, sorted(sort_tasks, key=lambda cat: cat[1])))
    return


def sort_date_desc():
    sort_tasks = csv_reader_tasks()
    list(map(print, sorted(sort_tasks, key=lambda cat: cat[1], reverse=True)))
    return


def sort_person_asc():
    sort_tasks = csv_reader_tasks()
    list(map(print, sorted(sort_tasks, key=lambda cat: cat[2])))
    return


def sort_person_desc():
    sort_tasks = csv_reader_tasks()
    list(map(print, sorted(sort_tasks, key=lambda cat: cat[2], reverse=True)))
    return


def filter_task():
    sort_tasks = csv_reader_tasks()
    task = input("Introduceti task-ul cautat: ")
    list_filter_task = filter(lambda r: task in r[0], sort_tasks)
    print(list(list_filter_task))
    return


def filter_date():
    sort_tasks = csv_reader_tasks()
    dates = input("Introduceti data cautata: ")
    list_filter_dates = filter(lambda r: dates in r[1], sort_tasks)
    print(list(list_filter_dates))
    return


def filter_person():
    sort_tasks = csv_reader_tasks()
    person = input("Introduceti persoana responsabila cautata: ")
    list_filter_person = filter(lambda r: person in r[2], sort_tasks)
    print(list(list_filter_person))
    return


def filter_categories():
    sort_tasks = csv_reader_tasks()
    category = input("Introduceti categoria cautata: ")
    list_filter_category = filter(lambda r: category in r[3], sort_tasks)
    print(list(list_filter_category))
    return


def main_function():
    while True:
        # add_categories()
        add_tasks()
        exit_program = input('Daca vrei sa iesi, apasa \'x\', altfel apasa alta tasta: ').lower()
        if exit_program == 'x':
            break
    return


def menu():
    while True:
        list_option = input('Alege una din urmatoarele optiuni: \n Pentru adaugare categorie apasa tasta 0 '
                            '\n Pentru listare apasa tasta 1 \n Pentru sortare apasa tasta 2 '
                            '\n Pentru filtrare date apasa tasta 3 \n Pentru adaugare task nou apasa tasta 4 '
                            '\n Pentru editare task existent apasa tasta 5'
                            '\n Pentru stergere task existent apasa tasta 6 '
                            '\n Pentru iesire din programa apasa \'x\' \n Alege optiunea: ')
        if list_option == '0':
            print('Ati ales sa adaugati o categorie!')
            add_categories()
        elif list_option == '1':
            print('Ati ales listare date sortate dupa categorie!')
            sort_category_asc()
        elif list_option == '2':
            list_sort = input('Pentru sortare alege una din optiunile: \n a) sortare ascendenta task: '
                              '\n b) sortare descendenta task: \n c) sortare ascendenta data: \n d) sortare '
                              'descendenta data:'
                              '\n e) sortare ascendenta persoana responsabila: \n f) sortare descendenta persoana '
                              'responsabila:'
                              '\n g) sortare ascendenta categorie: \n h) sortare descendenta categorie: '
                              '\n Alege o litera pentru sortare: ')
            if list_sort == 'a':
                print('Ati ales sortare ascendenta dupa task!')
                sort_task_asc()
            elif list_sort == 'b':
                print('Ati ales sortare descendenta dupa task!')
                sort_task_desc()
            elif list_sort == 'c':
                print('Ati ales sortare ascendenta dupa data!')
                sort_date_asc()
            elif list_sort == 'd':
                print('Ati ales sortare descendenta dupa data!!')
                sort_date_desc()
            elif list_sort == 'e':
                print('Ati ales sortare ascendenta dupa persoana responsabila!')
                sort_person_asc()
            elif list_sort == 'f':
                print('Ati ales sortare descendenta dupa persoana responsabila!')
                sort_person_desc()
            elif list_sort == 'g':
                print('Ati ales sortare ascendenta dupa categorie!')
                sort_category_asc()
            elif list_sort == 'h':
                print('Ati ales sortare descendenta dupa categorie!')
                sort_category_desc()
        elif list_option == '3':
            print('Ati apasat tasta 3!')
            filter_option = input('Filtrarea se face dupa:\n'
                                  'a) Task\n'
                                  'b) Data\n'
                                  'c) Persoana responsabila\n'
                                  'd) Categorie\n'
                                  'Alege optiunea: ')
            if filter_option == 'a':
                print('Ati ales filtrarea dupa Task!')
                filter_task()
            elif filter_option == 'b':
                print('Ati ales filtrarea dupa Data!')
                filter_date()
            elif filter_option == 'c':
                print('Ati ales filtrarea dupa Persoana responsabila!')
                filter_person()
            elif filter_option == 'd':
                print('Ati ales filtrarea dupa Categorie!')
                filter_categories()
        elif list_option == '4':
            print('Adaugati un task nou!')
            add_tasks()
        elif list_option == '5':
            print('Editati un task!')
            edit_task()
        elif list_option == '6':
            print('Stergeti un task!')
            delete_task()
        elif list_option == 'x':
            break
    return


menu()
