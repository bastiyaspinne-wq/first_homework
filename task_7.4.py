def common_elements():
    list_3 = set(range(0, 100, 3))
    list_5 = set(range(0, 100, 5))
    common = list_3.intersection(list_5)
    return common