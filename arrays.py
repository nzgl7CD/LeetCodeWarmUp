def solution(n, nums:list[int])->list[int]:
    for i in range(n):
        for j in range(n-i-1):
            if nums[j]>nums[j+1]: nums.insert(j,nums.pop(j+1))
    return nums

def product(nums:list[int])->list[int]:
    maxProduct=0
    n=len(nums)
    while n>=0:
        tempProduct=1
        for i in range(n):
            tempProduct*=nums[i]
        maxProduct=max(maxProduct,tempProduct)
        n-=1
        
def maxProfit(prices:list[int])->int:
    min_price=float('inf')
    max_profit=0
    for i in prices:
        if min_price>i: min_price=i
        max_profit=max(max_profit,i-min_price)
    return max_profit
    
print(maxProfit([1,3,0.5,5,7]))

def getSum(a:int,b:int)->int:
    while b!=0:
        sum_without_carry=a^b
        carry=(a&b)<<1
        a=sum_without_carry
        b=carry
    return a

def missingNumber(nums: list[int]) -> int:
    n=len(nums)
    sum_of_array=n*(n+1)//2
    return sum_of_array-sum(nums)

def dicting():
    sict={'My','name','is','XYZ'}
    string='MynameisXYZ'
    found = any(word in string for word in sict)
    for word in sict:
        if word in string: 
            string=string.replace(word, "")
            print(string)
            yield word
            
def fromInttoBin(n:int)->int:
    binary=bin(n)[2:]
    count=0
    for i in str(binary):
        if i=='1':count+=1
    return count

def climbStairs(n:int)->int:
    if n==0 or n==1: return 1
    dp=[1 if i<=1 else 0 for i in range(n+1)]
    dp1=list(map(lambda i: 1 if i<=1 else 0, range(n+1)))
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[-1]

def robber(nums:list[int]):
    rob1, rob2=0,0
    for i in nums:
        temp_findings=max(rob1+i,rob2)
        rob1=rob2
        rob2=temp_findings
    return rob2

def sortInts(nums:list[int])->list[int]:
    n=len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j]>nums[j+1]: nums.insert(j+1,nums.pop(j))
    return nums


# set_temp={1,2,3}
# set_temp.remove(1)
# set_temp.add(6)

# stacker=[1,2,3,1,2,4]
# stacker.remove(1)
# print(stacker)

# new_stack=list(map(lambda i: stacker[i] if stacker[i]>1 else None, range(len(stacker))))
# new_stack=list(filter(lambda i: i>1, stacker))

# print(new_stack)
# # print(list(set_temp)[0])


def check_anagram(s:str, t:str)->bool:
    return sorted(s)==sorted(t)

def equationString(s:str)->bool:
    if not s: return False
    validator="()"
    counter=0
    for i in s:
        if i in validator:
            counter+=(1 if i =="(" else -1)
        if counter<0: return False
    return counter==0

# print(equationString('()(())'))


# x='ses'
# x=list(x)
# x[0]='t'
# x=''.join(x)    
# print(x) 


def sumOfCarry(a:int,b:int)->int:
    while b!=0:
        sum_without_carry=a^b
        carry=(a&b)<<1
        a=sum_without_carry
        b=carry
        return a

def sumWCarry(a:int,b:int):
    while b!=0:
        sum_wo_carry=a^b
        carry=(a&b)<<1
        a=sum_wo_carry
        b=carry
    return a

def sortRaising(lst:list[int]):
    n=len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                lst.insert(j, lst.pop(j+1))
    return lst

def shortestWay(matrix):
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












        
        
