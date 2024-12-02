def minSetSize(self, arr):
        freq_map={}
        for num in arr:
            if num in freq_map:
                freq_map[num]+=1
            else:
                freq_map[num]=1    
        frequency=sorted(freq_map.values(),reverse=True)
        removed=0
        set_size=0
        target=len(arr)/2
        for freq in frequency:
            removed+=freq
            set_size+=1
            if removed >=target:
                break
        return set_size 