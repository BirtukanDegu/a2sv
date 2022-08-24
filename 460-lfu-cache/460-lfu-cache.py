class LFUCache(object):
    import collections

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.freqCache = collections.defaultdict(list)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        val = self.cache.get(key, -1)
        if val == -1: 
            return val
        
        value,freq = val
        self.freqCache[freq].remove(key)
        if not self.freqCache[freq]: del self.freqCache[freq]
        self.freqCache[freq+1].append(key)

        self.cache[key] = [value, freq+1]  
        
        return value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity <=0:
            return
        val = self.cache.get(key, -1)
        initfreq=1
        
        if  val == -1:
            
            if len(self.cache) == self.capacity:
                #print self.freqCache.items()
                minFreq, delList = min(self.freqCache.items(), key=lambda x:x[0])
                #print delList
                delkey = delList[0]
                del self.cache[delkey]
                self.freqCache[minFreq].remove(delkey)
                
                #insert in cache
                self.cache.update({key:[value,initfreq]})
                self.freqCache[initfreq].append(key)
            else:
                self.cache.update({key:[value,initfreq]})
                self.freqCache[initfreq].append(key)
        else:
            oldval,freq = val
            
            self.freqCache[freq].remove(key)
            if not self.freqCache[freq]: del self.freqCache[freq]
            self.freqCache[freq+1].append(key)
            
            self.cache[key] = [value,freq+1]
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)