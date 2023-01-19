# Input: 
# version1 = "1.0.33"
# version2 = "1.0.27"
# Output: 1 
# #version1 > version2

# Input:
# version1 = "0.1"
# version2 = "1.1"
# Output: -1
# #version1 < version2

# Input: 
# version1 = "1.01"
# version2 = "1.001"
# Output: 0
# #ignore leading zeroes, 01 and 001 represent the same number. 

# Input:
# version1 = "1.0"
# version2 = "1.0.0"
# Output: 0
# #version1 does not have a 3rd level revision number, which
# defaults to "0"

class Solution:
    def compareVersion(self, version1, version2):
        

        return 0

version1 = "1.0.1"
version2 = "1"
print(Solution().compareVersion(version1, version2))
# 1
