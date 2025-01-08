import sys
from collections import Counter

input = sys.stdin.read
data = input().split()
N = int(data[0])
nums = list(map(int, data[1:]))

nums.sort()

cnt_nums = Counter(nums)
most_common = cnt_nums.most_common()
max_freq = most_common[0][1]

freq_n = sorted(k for k, v in most_common if v == max_freq)
freq_n = freq_n[1] if len(freq_n) > 1 else freq_n[0]

print(round(sum(nums) / N)) 
print(nums[N // 2])         
print(freq_n)               
print(nums[-1] - nums[0])    