class Solution:
    def isValid(self, s: str) -> bool:
        c = 0
        for i in s:
            if i in ["(", "{", "]"]:
                c += 1
            else:
                c -= 1
        if c == 0:
            return True
        else:
            return False
