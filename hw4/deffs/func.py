from hw4.data.data_list import nested_list


class FlatIterator:
    def __init__(self, some_list):
        self.some_list = some_list

    def __iter__(self):
        self.cursor = -1
        self.counter = 0
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.some_list):
            raise StopIteration
        if isinstance(self.some_list[self.cursor], list):
            if self.counter >= len(self.some_list[self.cursor]):
                self.counter = 0
                self.cursor += 1
                if self.cursor == len(self.some_list):
                    raise StopIteration
                element = self.some_list[self.cursor][self.counter]
                self.cursor -= 1
                self.counter += 1
                return element

            else:
                element = self.some_list[self.cursor][self.counter]
                self.counter += 1
                self.cursor -= 1
                return element


def flat_generator(some_list):
    for item in some_list:
        for point in item:
            yield point


