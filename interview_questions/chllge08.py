class Solution:
    alphabetArr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                   'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]

    def convertToTitle(self, n):
        size = len(self.alphabetArr)

        result = ""
        while n > 0:
            if n <= size:
                result = self.alphabetArr[int(n) - 1] + result
                break

            pos = int(n % size)
            result = self.alphabetArr[pos - 1] + result

            n /= size
            if pos == 0:
                n -= 1

        return result


print(Solution().convertToTitle(702))
# ZZ

print(Solution().convertToTitle(456976))
# YYYZ

print(Solution().convertToTitle(704))
# AAB

print(Solution().convertToTitle(26))
# Output: Z

print(Solution().convertToTitle(51))
# Output: AY

print(Solution().convertToTitle(52))
# Output: AZ

print(Solution().convertToTitle(676))
# Output: YZ

print(Solution().convertToTitle(702))
# Output: ZZ

print(Solution().convertToTitle(704))
# Output: AAB
