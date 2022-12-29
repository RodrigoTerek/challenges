import collections


class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        dict = collections.defaultdict(int)

        for rec in rectangles:
            dict[rec[0]/rec[1]] += 1

        result = 0
        for i in dict.values():
            result += (i*(i-1))//2

        return result


print(Solution().interchangeableRectangles(
    [[4, 8], [3, 6], [10, 20], [15, 30]]))
