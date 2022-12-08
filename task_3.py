import datetime


class Task:
    def __init__(self, content):
        self.content = content
        self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f'{self.content} (создано {self.time})'

    def __repr__(self):
        return f'{self.content} (создано {self.time})'

    def __eq__(self, other):
        return self.content == other.content

    def __hash__(self):
        return hash(self.content)

    def __bool__(self):
        return self.content != ''


class TodoList:
    def __init__(self):
        self.tasks = []
    def __getitem__(self, item):
        return self.tasks[item]

    def __str__(self):
        return str(self.tasks)

    def __setitem__(self, key, value):
        if key >= len(self.tasks):
            add = key + 1 - len(self.tasks)
            self.tasks.extend([None] * add)
        self.tasks[key] = value
    def __delitem__(self, key):
        del self.tasks[key]


todo_list = TodoList()
todo_list[0] = Task('Сдать домашку')
todo_list[1] = Task('Выпить кофе')
print(todo_list)
print(type(todo_list))
# # [Сдать домашку (создано 2022-12-08 12:34:33), Выпить кофе (создано 2022-12-08 12:34:33)]
print(todo_list[0])
# Сдать домашку (создано 2022-12-08 12:34:33)
del todo_list[0]
print(todo_list)
# [Выпить кофе (создано 2022-12-08 12:34:33)]
