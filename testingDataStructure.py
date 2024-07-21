list=[1,2,1,3,4,5]
dict={}

# Appending to dictionary 
def dicT(list):
    for i in range(len(list)):
        if list[i] in dict: dict[list[i]].append(list[i])
        else: dict[list[i]]=[list[i]]
    print(dict)

def anyStream(list):
    seen = set()
    return any(num in seen or seen.add(num) for num in list)
