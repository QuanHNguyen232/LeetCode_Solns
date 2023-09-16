class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = deque()
        
        for log in logs:
            if log == "./": continue
            elif log == "../":
                if stack: stack.pop()
            else:
                stack.append(log)
        
        return len(stack)
        