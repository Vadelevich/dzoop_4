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
    def __init__(self, start=0, step=1, stop=2):
        self.tasks = []
        self.start = start
        self.stop = stop
        self.step = step

    def __str__(self):
        return str(self.tasks)

    def __setitem__(self, key, value):
        if key >= len(self.tasks):
            add = key + 1 - len(self.tasks)
            self.tasks.extend([None] * add)
        self.tasks[key] = value

    def __delitem__(self, key):
        del self.tasks[key]

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.tasks[self.value]
        else:
            raise StopIteration


todo_list = TodoList()
todo_list[0] = Task('Сдать домашку')
todo_list[1] = Task('Выпить кофе')

for item in todo_list: print(item)
# Сдать домашку (создано 2022-12-08 12:34:33)
# Выпить кофе (создано 2022-12-08 12:34:33)
