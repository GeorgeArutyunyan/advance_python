from hw4.data.data_list import nested_list
from hw4.deffs.func import FlatIterator, flat_generator

if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)
    for point in FlatIterator(nested_list):
        print(point)
