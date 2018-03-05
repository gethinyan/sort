class Solution:
    def mergeSort(self, L):
        if len(L) <= 1:
            return L
        index = len(L) // 2
        left = self.mergeSort(L[:index])
        right = self.mergeSort(L[index:])
        return self.merge(left, right)

    def merge(self, left, right):
        indexL, indexR = 0, 0
        result = []
        while indexL < len(left) and indexR < len(right):
            if left[indexL] < right[indexR]:
                result.append(left[indexL])
                indexL += 1
            else:
                result.append(right[indexR])
                indexR += 1
        result += left[indexL:]
        result += right[indexR:]
        return result


obj = Solution()
print(obj.mergeSort([3, 2, 4, 2.5, 3.5, 9, 8]))
