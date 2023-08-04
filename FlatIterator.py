class FlatIterator:

    def __init__(self, list_of_list):
        self.data = list_of_list

    def __iter__(self):
        print('Цикл начинается')
        self.smallest_counter = 0
        self.elem_counter = 0
        self.data_elem = self.data[self.smallest_counter]
        return self

    def __next__(self):

        if self.smallest_counter >= len(self.data_elem):
            self.elem_counter += 1
            if self.elem_counter >= len(self.data):
                print('Цикл завершается')
                raise StopIteration
            else:
                self.data_elem = self.data[self.elem_counter]
                self.smallest_counter = 0

        smallest_elem = self.data_elem[self.smallest_counter]
        self.smallest_counter += 1
        return smallest_elem


list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
