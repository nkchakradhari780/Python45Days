# higher order function
# functools.reduce(function_name, iterable)
# it reurns a single reduced value 

import functools
nums = [1,25,6,4,2,34,2]

result = functools.reduce(lambda a,b: a+b,nums)
print(result)

