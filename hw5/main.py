from hw5.decorators.decorators import logger
import os
from hw4.data.data_list import nested_list

PATH = os.path.abspath('logs.txt')


@logger(PATH)
def flat_generator(some_list):
    for item in some_list:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            yield item


if __name__ == '__main__':
    for i in flat_generator(nested_list):
        print(i)
