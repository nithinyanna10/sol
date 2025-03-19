class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_c = float('inf')
        for i in range(len(blocks)-k+1):
            sub = blocks[i:k+i]
            recolors = sub.count('W')
            min_c = min(min_c, recolors)
        return min_c