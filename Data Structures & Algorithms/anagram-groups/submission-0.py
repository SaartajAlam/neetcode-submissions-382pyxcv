class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappings = {}
        for string in strs:
            canon = "".join(sorted(string))
            if canon in mappings:
                mappings[canon].append(string)
            else:
                mappings[canon] = [string]
        return [value for value in mappings.values()]