class File:
    def __init__(self, name):
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        print(f'Файл {self.name} восстановлен из корзины')

    def remove(self):
        print(f'Файл {self.name} был удален')

    def read(self):
        if self.is_deleted:
            print(f'ErrorReadFileDeleted({self.name})')
        elif self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
        else:
            print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        if self.is_deleted:
            print(f'ErrorWriteFileDeleted({self.name})')
        elif self.in_trash:
            print(f'ErrorWriteFileTrashed({self.name})')
        else:
            print(f'Записали значение {content} в файл {self.name}')

class Trash:
    content = []

@staticmethod
def add(file):
    if file.__class__ != File:
        print('В корзину добавлять можно только файл')
    else:
        file.in_trash = True
        Trash.content.append(file)

@staticmethod
def clear():
    print('Очищаем корзину')
    for _ in range(len(Trash.content)):
        Trash.content.pop(0).remove()
    print('Корзина пуста')

@staticmethod
def restore():
    print('Восстанавливаем файлы из корзины')
    for _ in range(len(Trash.content)):
        Trash.content.pop(0).restore_from_trash()
    print('Корзина пуста')