def Solution(input:list[int])-> bool:
    duplicat_validation=set(input)
    if len(duplicat_validation)==len(input): return False
    else: return True
    
def Solution1(input:list[int])->bool:
    duplicate_set=set()
    for i in input:
        if i in duplicate_set: return True
        else: duplicate_set.add(i)
    return False

list=[1,2,3,4,2]
print(Solution1(list))