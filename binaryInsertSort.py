class Solution:
    def binaryInsertSort(self, L):
        for i in range(1, len(L)):
            left = 0
            right = i - 1
            tmp = L[i]
            while left <= right:
                mid = (left + right) // 2
                if L[mid] > tmp:
                    right = mid - 1
                else:
                    left = mid + 1
            for j in range(i, left, -1):
                L[j] = L[j - 1]
            L[left] = tmp
        return L


obj = Solution()
print(obj.binaryInsertSort([3, 2, 4, 2.5, 3.5, 9, 8]))
