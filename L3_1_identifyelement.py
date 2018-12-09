from collections import *
def countfreq(list):
        return Counter(list)

print("Enter list of variavbles:")
list = [int(x) for x in input().split()]
freq = countfreq(list)
sortedDict = dict(sorted(freq.items(), key=lambda x: x[1]))
print(next(iter(sortedDict)))
