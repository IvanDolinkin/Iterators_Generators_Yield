class FlatIterator:

    def __init__(self, list_of_list):
        self.data = list_of_list

    def __iter__(self):
        print('Цикл начинается')
        self.data_copy = self.data.copy()
        return self

    def __next__(self):
        if not self.data_copy:
            print('Цикл завершается')
            raise StopIteration
        while self.data_copy != [] and type(self.data_copy[0]) is list:
            if len(self.data_copy) > 1:
                self.data_copy = self.data_copy[0] + self.data_copy[1:]
            else:
                self.data_copy = self.data_copy[0]

        if not self.data_copy:
            print('Цикл завершается')
            raise StopIteration

        item = self.data_copy.pop(0)

        return item


list_of_lists_2 = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
]

flat_iterator = FlatIterator(list_of_lists_2)
[print(i, end='***') for i in flat_iterator]
[print(i, end='***') for i in flat_iterator]
[print(i, end='***') for i in flat_iterator]

print(flat_iterator.data)
print(flat_iterator.data_copy)


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

# if __name__ == '__main__':
#     test_3()
