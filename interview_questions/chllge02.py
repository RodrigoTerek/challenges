class Solution():
    def plusOne(self, digits, i=-1):
        if (digits[i] + 1) == 10:
            digits[i] = 0

            if -i == len(digits):
                digits.insert(0, 1)
                return digits

            return self.plusOne(digits, i - 1)

        digits[i] += 1
        return digits


num = [9, 9, 9]
print(Solution().plusOne(num))
# [1, 0, 0, 0]
