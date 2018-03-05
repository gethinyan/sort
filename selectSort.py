class Solution:
    def selectSort(self, L):
        for i in range(len(L)):
            index = i
            for j in range(i + 1, len(L)):
                if L[index] > L[j]:
                    index = j
            L[i], L[index] = L[index], L[i]
        return L


obj = Solution()
print(obj.selectionSort([9, 3, 2, 4, 8]))
