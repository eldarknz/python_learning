# https://stepik.org/lesson/24462/step/7?unit=6768

num_classes = int(input())
classes     = {}

i = 0
while i < num_classes:
    child_with_parents = str(input()).split(":")
    child              = child_with_parents[0].strip()
    parents            = child_with_parents[1].strip().split(" ") if len(child_with_parents) > 1 else []
    for p in parents:
        if p != child:
            if not p in classes:
                classes[p] = [child]
            else:
                classes[p].append(child)
    i += 1

def checkParents(parent, child):
    if parent in classes:
        if child in classes[parent]:
            return "Yes"
        else:
            res = "No"
            for c in classes[parent]:
                res = checkParents(c, child)
                if res == "Yes":
                    break
            return res

    else:
        return "No"
    
num_queries = int(input())

j = 0
while j < num_queries:
    parent_with_class = str(input()).split(" ")
    parent            = parent_with_class[0].strip()
    child             = parent_with_class[1].strip()

    res = checkParents(parent, child) if parent != child else "Yes"
    print(res)

    j += 1
