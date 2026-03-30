def common_elements():
    list_3 = set(range(0, 100, 3))
    list_5 = set(range(0, 100, 5))
    result = list_3.intersection(list_5)
    return result
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('OK')
