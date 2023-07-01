class Solution:
    def productExceptSelf(self, a: List[int]) -> List[int]:
        s = [1] * len(a)
        p = [1] * len(a)
        ans = []
        for i in range(1, len(a)):
            s[i] = a[i - 1] * s[i - 1]
        for i in range(len(a) - 2, -1, -1):
            p[i] = a[i + 1] * p[i + 1]
        print(p)
        for i in range(0, len(a)):
            ans.append(s[i] * p[i])
        return ans
