class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {')':'(', '}':'{', ']': '['}
        stack = []
        for ch in s:
            if ch not in mappings:
                stack.append(ch)
            else:
                if len(stack) == 0 or stack[-1] != mappings[ch]:
                    return False
                stack.pop()
        return len(stack) == 0
