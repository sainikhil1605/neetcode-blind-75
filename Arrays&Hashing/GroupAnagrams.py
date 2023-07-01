class Solution:
    def groupAnagrams(self, a: List[str]) -> List[List[str]]:
        d = {}
        ans = []
        for i in a:
            t = "".join(sorted(list(i[:])))
            if t in d.keys():
                k = d[t]
                k.append(i)
                d[t] = k
            else:
                d[t] = [i]
            # print(d)
        for i in d.values():
            ans.append(i)

        return ans
