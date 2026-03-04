nums = []
for i in range(5):
    n = float(input(f"Enter number {i+1}: "))
    nums.append(n)

average = sum(nums) / 5
print("Average is:", average)