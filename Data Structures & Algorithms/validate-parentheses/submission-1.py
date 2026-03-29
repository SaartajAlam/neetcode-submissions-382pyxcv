class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for ch in s:
            if ch in mappings: # Closing Bracket
                if not stack or stack[-1] != mappings[ch]:
                    return False
                stack.pop()
            else: # Opening Bracket
                stack.append(ch)
        return len(stack) == 0