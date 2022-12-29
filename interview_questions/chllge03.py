# Input: ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"], k = 2
# Output: ["pro", "daily"]

class Solution(object):
    def topKFrequent(self, words, k):
        quantDict = {}

        for w in words:
            if w in quantDict:
                quantDict[w] += 1
            else:
                quantDict[w] = 1

        result = list(quantDict.items())
        result.sort(key=lambda x: x[1], reverse=True)

        return list(map(lambda item: item[0], result[:k]))


words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
