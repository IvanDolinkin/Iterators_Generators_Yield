import types


def flat_generator(list_of_list):
    for elem in list_of_list:
        if isinstance(elem, list):              # до использования генератора внутри генератора я как-то сам дошел
            for el in flat_generator(elem):     # а конкретно такую запись подсмотрел. у меня было просто "flat_generator(elem)"
                yield el                        # почему нужно именно так непонятно
        else:
            yield elem

list_of_lists_2 = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
]

# for x in flat_generator(list_of_lists_2):
#     print(x)
# for x in flat_generator(list_of_lists_2):
#     print(x)
# for x in flat_generator(list_of_lists_2):
#     print(x)

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
