class Solution:
    def insertSort(self, L):
        for i in range(1, len(L)):
            j = 0
            while L[j] < L[i] and j < i:
                j += 1
            if j != i:
                tmp = L[i]
                for k in range(i, j, -1):
                    L[k] = L[k - 1]
                L[j] = tmp
        return L


obj = Solution()
print(obj.insertSort([9, 3, 2, 4, 8]))
