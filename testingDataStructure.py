
# Appending to dictionary 
def dicT(list):
    for i in range(len(list)):
        if list[i] in dict: dict[list[i]].append(list[i])
        dict[list[i]]=[list[i]]
    print(dict)

def anyStream(list):
    seen = set()
    return any(num in seen or seen.add(num) for num in list)
# print(anyStream([1,2,3,4]))

def indexArray():
    list_1=[1,2,3,4,5]
    list_1[2]=4 #change existing element in index 2 with 4
    list_1.insert(0,10) #puts 10 in index 0
    list_1.append(2) #puts new element in the back of the stack
    list_1.insert(0,list_1.pop(list_1.index(max(list_1))))
    return list_1
# print(indexArray())

def splitStrings(string1:str):
    stringList=[i for i in string1]
    stringList.append("")
    for i in range(len(stringList)-1):
        
        stringList.insert(i+1,stringList[i])
    
    return stringList

def shortestPath(matrix):
    m,n=len(matrix),len(matrix[0])
    dp=[[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = matrix[0][0]
    for i in range(1,n):
        dp[0][i]=dp[0][i-1]+matrix[0][i]
    for j in range(1,m):
        dp[j][0]=dp[j-1][0]+matrix[j][0]
    
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=min(dp[i-1][j],dp[i][j-1]+matrix[i][j])
    
    return dp[m-1][n-1]

def commonNumber(arrayA, arrayB):
    setB, setA=set(arrayB),set(arrayA)
    result=[x for x in setA if x in setB]
    return list(filter(lambda x: x in setB, setA))

# print(commonNumber([1,2,3],[1,2,3]))

def group_anagrams(strings):
    anagrams={}
    for string in strings:
        temp=''.join(sorted(string))
        if temp not in anagrams: 
            anagrams[temp]=[]
        anagrams[temp].append(string)
    return anagrams.values()

# print(group_anagrams(['text', 'tet', 'xtet', 'tte', 'ttex']))


def shortPathMatrix(matrix):
    m,n=len(matrix), len(matrix[0])
    dp=[[0 for _ in range(n)] for _ in range(m)]
    dp[0][0]=matrix[0][0]
    for i in range(1,n):
        dp[0][i]=dp[0][i-1]+matrix[0][i]
    for j in range(1,m):
        dp[j][0]=dp[j-1][0]+matrix[j][0]
    
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=min(dp[i-1][j],dp[i][j-1]+matrix[i][j])
    return dp[m-1][n-1]
    

# ma=[[1,2,1], [1,4,2], [1,2,5]]
# shortPathMatrix(matrix=ma)


def armstrong(num, pow):
    sum=0
    for i in str(num):
        sum+=int(i)**pow
    return sum

# print(armstrong(222,2))

# def fibonacci(n):
#     if not n:
#         return ''
#     elif n<3:
#         return '0 1'
#     fib='0 1'
#     for i in range(2,n):
        
    
#     return fib

# print(fibonacci(6))

# words = ["Hello", "world", "from", "Python"]
# sentence = " ".join(words)
# print(sentence) 

def back_number_equal_no(n):
    return str(n**2)[-(len(str(n)))::]==str(n)

# print(back_number_equal_no(376))
