class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        library = {}
        for word in strs:
            key = tuple(sorted(word))
            if key not in library:
                library[key] = [word]
            else:
                library[key].append(word)

        return list(library.values())  