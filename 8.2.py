import random

nums=set()
while True:
    nums.add(random.randint(15,45))
    if len(nums) == 30:
        break
    
print(nums)

count=0
for i in nums:
    if i < 30:
        count+=1
        
nums = {i for i in nums if i <= 35}

print(f"Number of integers less than 30 are {count}")
print(nums)
