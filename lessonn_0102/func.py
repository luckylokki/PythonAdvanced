from typing import Any, Dict, List


def filter_by_first_met_value(
        dataset: List[Dict[str, Any]], keys: List[str]) -> List[Dict[str, Any]]:
    """Filter dataset by first met value in keys"""
    trash = []
    result = []
    for dict in dataset:
        for key in dict:
            if key in keys:
                if dict[key] not in trash:
                    trash.append(dict[key])
                    result.append(dict)
                elif dict[key] in trash:
                    break
                break
    return result



origin = [
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
    {"foo": "F", "bar": "BAR", "foobar": "fb"},
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
]

result1 = filter_by_first_met_value(origin, ['foo', 'bar', 'foobar'])
result2 = filter_by_first_met_value(origin, ['foobar'])
result3 = filter_by_first_met_value(origin, ['bar', 'foobar'])

assert result1 == [{'foo': 'FOO', 'bar': 'BAR', 'foobar': 'fb'}, {'foo': 'F', 'bar': 'BAR', 'foobar': 'fb'}]
assert result2 == [{'foo': 'FOO', 'bar': 'BAR', 'foobar': 'fb'}]
assert result3 == [{'foo': 'FOO', 'bar': 'BAR', 'foobar': 'fb'}]