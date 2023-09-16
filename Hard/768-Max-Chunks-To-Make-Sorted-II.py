class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Initialize minimum array.
        smallest = [0] * len(arr)
        smallest[-1] = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            smallest[i] = min(arr[i], smallest[i+1])
            
        num_chunks = 1
        biggest = arr[0]
        for i in range(len(arr) - 1):   # dont need to split in last element
            biggest = max(arr[i], biggest)
            if biggest <= smallest[i+1]:
                num_chunks += 1

        return num_chunks
    
# Solution from CodePath Week8 Session1 Lecture 