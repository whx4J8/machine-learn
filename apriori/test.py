# coding=utf-8
from itertools import combinations, chain

#
# def subsets(arr):
#     return chain(*[combinations(arr, i + 1) for i, a in enumerate(arr)])


if __name__ == '__main__':
    # test = combinations([1, 2, 3, 4], 2)
    # for el in test:
    #     print el

    arr = [1,2,3,4]
    # for i, c in enumerate(arr):
    #     for el in combinations(arr, i + 1):
    #         print el
    #
    # print "================================="
    # for value in chain(*[combinations(arr,i+1) for i,a in enumerate(arr)]):
    #     print value
    #
    # print type(chain(*[combinations(arr,i+1) for i,a in enumerate(arr)]))

    chain(*[combinations(arr, i + 1) for i, a in enumerate(arr)])
    for value in combinations([1,2,3],1):
        print value
