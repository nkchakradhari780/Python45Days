import functools
nums = [2,6,3,23,53,69,85]

max_value = functools.reduce(lambda a,b: a if a > b else b ,nums)
print(max_value)