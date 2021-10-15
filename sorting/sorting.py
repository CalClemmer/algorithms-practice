import random

# import numpy as np

# check sorted
def is_sorted(l):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def random_list(n):
    l = list(range(1, n + 1))
    random.shuffle(l)
    return l


# The most fundamental sorting algorithm
# BOGO SORT
# If you're optimistic enough it's the perfect solution in all cases
# If you're a boring realist, don't use for n > ~10
def bogo_sort(l):
    while True:
        random.shuffle(l)
        if is_sorted(l):
            return l


# The simplest sorting algorithim
# BUBBLE SORT
# If you're lazy it's a decent solution in cases where n is less than about 2,000
def bubble_sort(l):
    while not is_sorted(l):
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
    return l


# The default
# TIM SORT
# So good python comes with it. Lol.
def tim_sort(l):
    return sorted(l)


# A fun sorting algorithm
# QUICK SORT
def quick_sort(l):
    less = []
    equal = []
    greater = []

    if len(l) > 1:
        pivot = l[0]
        for x in l:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return l


def merge_sort(arr):
    pass
    # split_arr = np.array_split(arr, len(arr))
    # print(split_arr)


# merge_sort([4, 3])


# print(quick_sort(random_list(50000)), "QUICK SORT")

# print("BOGO", bogo_sort(random_list(9)), "BOGO")

# print("BUBBLE", bubble_sort(random_list(10000)), "BUBBLE")

# print("QUICK", quick_sort_cheeky(random_list(180000)), "TIM")
