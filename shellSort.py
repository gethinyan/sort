class Solution:
    def shellSort(self, L):
        step = len(L) // 2
        while step > 0:
            for i in range(step, len(L)):
                while i >= step and L[i - step] > L[i]:
                    L[i], L[i - step] = L[i - step], L[i]
                    i -= step
            step = step // 2
        return L


obj = Solution()
print(obj.shellSort([3, 2, 4, 2.5, 3.5, 9, 8]))
