# 반복문 : wile문, for문

# while문
# 1 ~ 10까지 반복 출력
i = 1
while i<11:
    print(i)
    i+=1
    if i==5:
        break
else:
    print("End")

nums = [1, 3, 5, 7, 9]
target = 2
found = False

idx=0
while idx<len(nums):
    if nums[idx]==target:
        print(f"{target} found.")
        # found = True
        break
    idx+=1
else:
    print(f"{target} not found.")

# if not found:
#     print(f"{target} not found.")

# 1 ~ 10까지의 합
i = 0
tot = 0
while i<=10:
    tot+=i
    i+=1
else:
    print(f"합: {tot}")

# 1 ~ 10까지의 합
i = 0
tot = 0
while i<=10:
    if i%2==0:
        tot+=i
    i+=1
else:
    print(f"합: {tot}")

# 1 ~ 10까지의 합
i = 1
tot = 0
while i<=10:
    i+=1
    if i%2==1:
        continue
    tot+=i
else:
    print(f"합: {tot}")

