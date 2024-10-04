data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(param):
    sum_ = 0
    for el in param:
        if type(el) is int:
            sum_ += el
        if type(el) is str:
            sum_ += len(el)
        if type(el) is bool:
            if el:
                sum_ += 1
        if isinstance(el, list):
            sum_ += calculate_structure_sum(el)
        if isinstance(el, dict):
            sum_ += calculate_structure_sum([list(el.values()),list(el.keys())])
        if isinstance(el, tuple):
            sum_ += calculate_structure_sum(list(el))
        if isinstance(el, set):
            sum_ += calculate_structure_sum(list(el))
    return sum_

result = calculate_structure_sum(data_structure)
print(result)
