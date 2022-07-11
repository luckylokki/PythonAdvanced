from typing import List


def find_uniq(dataset: List[int]) -> int:
    result = [num for num in dataset if dataset.count(num) == 1][0]
    return result


lst = [54, 90, 52, 10, 62, 54, 90, 52, 10, 62, 42]
res = find_uniq(lst)
assert res is not False
