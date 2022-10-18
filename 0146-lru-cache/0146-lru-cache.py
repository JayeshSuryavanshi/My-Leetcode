class LRUCache:

    def __init__(self, capacity: int):
        self.deque = collections.deque([])
        self.dictionary = {}
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key not in self.dictionary:
            return -1
        self.deque.remove(key)
        self.deque.append(key)
        return self.dictionary[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary:
            self.deque.remove(key)
        elif len(self.dictionary) == self.capacity:
            remove = self.deque.popleft()
            self.dictionary.pop(remove)
        self.deque.append(key)
        self.dictionary[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)