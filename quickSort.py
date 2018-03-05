class Solution:
    def quickSort(self, L, low, high):
        if low >= high:
            return
        index = self.partition(L, low, high)
        self.quickSort(L, low, index - 1)
        self.quickSort(L, index + 1, high)
        return L

    def partition(self, L, low, high):
        target = L[high]
        i = low
        for j in range(low, high):
            if L[j] < target:
                L[i], L[j] = L[j], L[i]
                i += 1
        L[i], L[high] = L[high], L[i]
        return i


obj = Solution()
print(obj.quickSort([9, 3, 2, 4, 8], 0, 4))
