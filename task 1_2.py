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


todo_list = set()

todo_list.add(Task('Сделать домашку'))
todo_list.add(Task('Выпить кофе'))
todo_list.add(Task('Выйти на пробежку'))
todo_list.add(Task('Сделать домашку'))

for item in todo_list:
    print(item)

# Сделать домашку (создано 2022-12-08 12:09:14)
# Выпить кофе (создано 2022-12-08 12:09:14)
# Выйти на пробежку (создано 2022-12-08 12:09:14)

todo_list = []
todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))
todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))

non_empty_tasks = [item for item in todo_list if item]
print(non_empty_tasks)
# [Сделать домашку (создано 2022-12-08 12:21:16), Сделать домашку (создано 2022-12-08 12:21:16)]

print(len([item for item in todo_list if not item]))
# 2
