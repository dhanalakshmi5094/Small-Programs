def oddNumbers(l, r):
    # Write your code here
    total_nums = []
    if r>l:
       n = r-l
       for i in range(0,n+1):
           total_nums.append(l+1)
           if total_nums[i] %2 != 0:
              return total_nums[i]
           else:
              continue
    elif r<l:
        n = l-r
        for i in range(0,n+1):
           total_nums.append(r+1)
           if total_nums[i] %2 != 0:
              return total_nums[i]
           else:
              continue
    else:
        print("please enter 2 different nums")

print(oddNumbers(3,5))