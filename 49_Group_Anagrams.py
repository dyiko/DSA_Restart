def groupAnagrams(self, strs):
        anagram_Map={}
        for words in strs:
            sorted_Word=''.join(sorted(words))
            if sorted_Word in anagram_Map:
                anagram_Map[sorted_Word].append(words)
            else:
                anagram_Map[sorted_Word]=[words]
        return list(anagram_Map.values()) 