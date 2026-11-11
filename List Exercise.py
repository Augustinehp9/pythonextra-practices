print()
print("Exercise 1")
print()

nums = [4, 8, 4]
nums.append(16)
nums.insert(2,9)
nums.remove(8)
nums.pop(0)
print(nums)

print()
print("Exercise 2")
print()

nums = [10, 20 ,30, 40 ,50,60]
print(nums[0:2])
print(nums[:2] + nums[3:])
print("30 is excluded from slicing:",nums[-4])

print()
print("Exercise 3")
print()

nums = [3, 6, 9, 12]
for i in range(1,len(nums)):
    nums[i] = nums[i - 1] + 2
print(nums)

print()
print("Exercise 4")
print()

nums = [2, 4, 6, 8]

for i in range(len(nums)-2,-1,-1):
    nums[i] = nums[i] + nums[i+1]
print(nums)

print()
print("Exercise 5")
print()

nums = [7, 3, 9]
for i in range(len(nums)):
    print(nums[i],end = " ")
    
print()
print("Exercise 6")
print()

nums = [5, 10, 15]
for i in range(len(nums)):
    if nums[i] > 8:
        print(nums[i],end = " ")
        

print()
print("Exercise 7")
print()

num = 5
result = []

for i in range(1,num +1 ):
    nNum = i  * 3
    result.append(nNum)
    
print("The nums multiple with 3 is",result)

print()
print("Exercise 8")
print()

nums = [-4, 0, 7, -1, 9 ,0]
pList =[]
nList = []
count = 0

for i in range(len(nums)):
    if nums[i] == 0:
        count += 1
        
    elif nums[i] < 0:
        nList.append(nums[i])
        
    elif nums[i] > 0:
        pList.append(nums[i])
        
print("Count of num greater than 0 is:",count)
print("Positive integer is:", pList)
print("Negative integer is:", nList)
    
print()
print("Exercise 9")
print()

nums = [5, 2, 5, 3, 5, 4]
target = 5
newlist = []

for i in range(len(nums)):
    if target != nums[i]:
        newlist.append(nums[i])
        
print("The new list is :",newlist)

print()
print("Exercise 10")
print()

nums = [10,20,30,40,50]
nLen = len(nums)
reverse = []

for i in range(nLen -1, -1, -1):
     
     reverse.append(nums[i])
     
print("The reversed list is :",reverse)

print()
print("Exercise 11")
print()

nums = [3, 8, 2, 5]
nLen = len(nums)
total = 0

for i in range(nLen):
    
    if i % 2 == 0:
        total += nums[i]
    
    else:
        total -=nums[i]
        
print("The answer after all substraction:",total)

print()
print("Exercise 12")
print()

nums = [2, 2, 3, 5, 5, 5, 7]
indices = []
nLen = len(nums)

for i in range(nLen -1-1):
    if nums[i] == nums[ i + 1]:
        indices.append(i)
        
print("A list of indices are:",indices)
        
print()
print("Exercise 13")
print()

listNum = []
nSize = 5

for i in range(nSize):
    listNum.append(0)

print("The size filled with zeros",listNum)

print()
print("Exercise 14")
print()

# nName = input("Would you like to add a new name:")
# nlist = []
# 
# while nName == "yes":
#     
#         name = input("Input a name:")        
#         nlist.append(name)
#         
#         nName = input("Would you like to add more:")
#         
#         
#         
# print("Name of the list is :",nlist)

print()
print("Exercise 15")
print()

def removelist(nums):
    nLen = len(nums)
    middle = nLen // 2
    newlist = 0
    
    if nLen % 2 == 0:
        newlist = nums[ : middle-1] + nums[middle +1 :]
    
    else:
        newlist = nums[ : middle] + nums[middle +1 :]
    
    return newlist

nNum = [1, 2, 3, 4, 5, 6,7 ]
print("Removing the central element:",removelist(nNum))

print()
print("Exercise 16")
print()

def resetList(a_listWord, a_nSize, a_strValue):
    a_listWord.clear()
    
    for i in range(a_nSize):
        a_listWord.append(a_strValue)
        
    return a_listWord

a_listWord = ["A", "B"]
print("The list of ** is",resetList(a_listWord,4, "*"))

print()
print("Exercise 17")
print()



































































































































