"""
Convert a list of dictionaries into a dictionary of equal length lists.

[{'a': 1, 'b': 3}, {'a': 2, 'b': 2}, {'a': 3, 'b': 1}]
  => {'a': [1, 2, 3], 'b': [3, 2, 1]}
"""


def list_to_dict(data):
    results = {}
    for row in data:
        for k, v in row.items():
            if k not in results:
                results[k] = []
            results[k].append(v)
    return results
