class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def countDays(capacity: int) -> int:
            d = 0
            cargo = 0
            for w in weights:
                if cargo + w > capacity:
                    d += 1
                    cargo = w
                else:
                    cargo += w
            d += 1
            return d
        
        # binary search
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = (low + high) // 2
            d = countDays(mid)
            if d <= days:
                high = mid
            else:
                low = mid + 1
        return low

# Soln from CodePath Week8 Session2 Lecture