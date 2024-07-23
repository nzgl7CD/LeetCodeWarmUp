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

def indexArray():
    list=[1,2,3,4,5]
    list[2]=4 #change existing element in index 2 with 4
    list.insert(0,10) #puts 10 in index 0
    list.append(2) #puts new element in the back of the stack
    print(list)
indexArray()