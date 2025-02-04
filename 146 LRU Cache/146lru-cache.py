class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap_cache = {} #key, value from the input 
        self.tracker = deque() #tracks the most/least recently used keys

    def get(self, key: int) -> int:
        '''
        check if key is in cache: 
        yes- return the vlaue 
        no - return -1 
        '''
        if key in self.hashmap_cache:
            #update the deque with lest/most recently. insert this key in deque 
            #remove the key from its curr position and add it to the end (most recently used) - O(n) to traverse, find the key and remove it! Can we do better???
            self.tracker.remove(key)
            self. tracker.append(key)
            return self.hashmap_cache[key]
        return -1 

    def put(self, key: int, value: int) -> None:
        '''
        if key exsisits in cache, update thevalue
        '''
        if key in self.hashmap_cache:
            self.hashmap_cache[key] = value
            #remove the key from its curr position and add it to the end (most recently used)
            self.tracker.remove(key)
            self. tracker.append(key)
        else:
            '''
            check1 : is number of put operation < capcity?
            '''
            if len(self.hashmap_cache) == self.capacity:
                #cache is full. pop least recently used key from front of queue
                lrukey = self.tracker.popleft()
                #now remove from hashmap too
                self.hashmap_cache.pop(lrukey)
            #add new pair 
            self.hashmap_cache[key] = value
            self.tracker.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)