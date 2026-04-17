from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for w in strs:
            new_repr = [0] * 26
            for ch in w:
                new_repr[ord(ch) - ord("a")] += 1
            result[tuple(new_repr)].append(w)

        return list(result.values())
