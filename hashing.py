class hash_table:
    
    def __init__(self,size = 10):
        self.size = size
        size.table = [[] for i in range(size)]
        
    def hash_function(self,key):
        return key % self.size

    def insert(self,key,value):
        index = self.hash_function(key)
        
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
            
        self.table[index].append([key, value])
        
    def search(self,key):
        index = self.hash_function(key)
        
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
            return None
        
    def delete(self,key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return True
            return False
        
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"index{i}:{bucket}")
            
    
ht = hash_table()

ht.insert(24, "kamlesh")
ht.insert(44, "virat")
ht.insert(7, "Mahendra")

ht.display()

