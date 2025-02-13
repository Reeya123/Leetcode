class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for index in range(n + 1):
            count = 0
            while index:
                
                index = index & (index - 1)
                
                count += 1
            res.append(count)
        return res