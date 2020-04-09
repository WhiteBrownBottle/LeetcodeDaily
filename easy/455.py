class Solution:
    def findContentChildren(self, g: list, s: list) -> int:
        child = 0
        cookie = 0
        g.sort()
        s.sort()
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child