# Hash Table Implementation in Python

This repository contains a simple implementation of a hash table data structure using Python. The hash table uses chaining to handle collisions and supports basic operations such as insert, search, delete, and display.

## Features

- **Customizable Table Size:** You can specify the size of the table during initialization.
- **Hash Function:** Uses modulo operation to map keys to indices.
- **Collision Handling:** Implements chaining (using lists) to store multiple key-value pairs at the same index.
- **Operations Supported:**
  - Insert key-value pairs
  - Search for a value by key
  - Delete a key-value pair
  - Display the contents of the hash table

## Usage Example

```python
class hash_table:
    
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for i in range(size)]
        
    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
        
    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
        
    def delete(self, key):
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
```

## Output

```
index0:[]
index1:[]
index2:[]
index3:[]
index4:[[24, 'kamlesh'], [44, 'virat']]
index5:[]
index6:[]
index7:[[7, 'Mahendra']]
index8:[]
index9:[]
```

## How It Works

- **Insert:** Add a key-value pair to the hash table. If the key already exists, its value is updated.
- **Search:** Retrieve the value associated with a key, or return `None` if the key is not found.
- **Delete:** Remove a key-value pair from the hash table. Returns `True` if deleted, `False` if not found.
- **Display:** Print all buckets and their contents.

## Notes

- This is a basic educational implementation and may not be suitable for production use.
- Keys should be integers, as the hash function uses modulo arithmetic.

## License

This project is open source and available under the MIT License.
