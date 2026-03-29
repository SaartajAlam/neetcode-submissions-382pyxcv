class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = {}
        for s in strs:
            canon = "".join(sorted(s))
            if canon not in hMap:
                hMap[canon] = [s]
            else:
                hMap[canon].append(s)
        return [val for val in hMap.values()]