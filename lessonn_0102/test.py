dataset = [54, 90, 52, 10, 62, 54, 90, 52, 10, 62, 42]


def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


def find_elem():
    sorted_list = sort_list(dataset)
    for i in range(0, len(sorted_list) - 1):
        if sorted_list[i - 1] != sorted_list[i] != sorted_list[i + 1]:
            result = int(sorted_list[i])
    return result


#####version with set
def find(lst):
    pair = set()
    for x in lst:
        pair ^= {x}
    result = int(list(pair)[0])
    return result
