"""
Swaps the given input list with modifying the existing list only.
It is same as reversing the list without using any new list.
"""

total_int = raw_input('enter the count of intergers')
ip_nums = []
for x in range(int(total_int)):
    ip_nums.append(int(raw_input('enter number: ')))

start_index = 0
end_index = len(ip_nums) - 1

print(ip_nums)

while start_index < end_index:
    temp = ip_nums[start_index]
    ip_nums[start_index] = ip_nums[end_index]
    ip_nums[end_index] = temp

    start_index = start_index + 1
    end_index = end_index - 1

print(ip_nums)
