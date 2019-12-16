# https://stepik.org/lesson/24463/step/7?unit=6771

data  = [
    '1 : 2 3 4 5 6',
    '7 : 8 3 5',
    '8 : 3 9',
    '2 : 7 3 5 10 9',
    '3 : 5 9',
    '4 : 10',
    '5 : 9',
    '10',
    '6 : 4 10',
    '9 : 6'
]
queries = ['5', '9', '1', '7', '8']

groups   = {}

#len_data = int(input())
len_data = len(data)

i = 0
while i < len_data:
    #value   = str(input()).split(":")
    value   = data[i].strip().split(":")
    child   = value[0].strip()
    parents = value[1].strip().split(" ") if len(value) > 1 else []
    if child in groups:
        for p in parents:
            if not p in groups[child]:
                groups[child].extend(p)
    else:
        groups[child] = parents
    i += 1

#len_queries = int(input())
len_queries = len(queries)

j = 0
while j < len_queries:
    #value = str(input())
    value = queries[j]
    res = checkExceptions(value)
