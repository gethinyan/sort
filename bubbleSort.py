class Solution:
    def bubbleSort(self, L):
        for i in range(len(L)):
            for j in range(len(L) - i - 1):
                if L[j] > L[j + 1]:
                    L[j], L[j + 1] = L[j + 1], L[j]
        return L


obj = Solution()
print(obj.bubbleSort([9, 3, 2, 4, 8]))
