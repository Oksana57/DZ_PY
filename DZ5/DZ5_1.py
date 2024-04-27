def path_file():
    """Принимает на вход строку - абсолютный путь до файла и возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""
    text = input("Введите путь к файлу: ").split('/')
    path_file = '/'.join(text[0:-1])
    all_file = (' '.join(text[-1::])).split('.')
    name_file = all_file[0]
    extension = all_file[1]

    return   path_file, name_file, extension


print(path_file())

