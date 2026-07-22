class Solution:
    def isValid(self, s: str) -> bool:
        isValid = False
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        # Configuration test