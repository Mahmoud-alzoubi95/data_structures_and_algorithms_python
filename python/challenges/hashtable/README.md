# Hashtables
Hash Tables
Data Structure used to store data Stores data that has [key,value] pairsMaps key to value and returns an index, Hash table is a large empty array , Takes advantage of array O(1) to get data ,Knowing the index

Hash Function
hash: takes in an arbitrary key and returns an index in the collection.
When adding to a hash table key is passed to hash function
also when getting a key from the hash table

Collisions
Occur when two or more [key,value] are mapped to the same index in the hash table Common to make the index a linked list Thought of like "buckets" that store reference to linked nodes with key/values
called chaining.


## Challenge

**Implement a Hashtable with the following methods:**
hash: takes in an arbitrary key and returns an index in the collection.
add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
get: takes in the key and returns the value from the table.

## Approach & Efficiency

An array was the chosen data structure to use for the HashTable and a linked list was the chosen data structure for to use at each index of the Hash Table to handle collisions.

Adding [key,value] pairs and getting values from the Hash Table is essentially O(1) for time for both posting and getting. Big O is always looking for the worst case scenario. The worst case would be the length of the linked list at any given index.

## API
Three public methods for this Hash Table.
1. HashTable.add(key, value)
2. HashTable.get(key)
3. HashTable.contains(key)
Add: Takes key and value as arguements, hashes the key, returns hash-index, and adds the [key,value] pair to the HashTable at hash-index. Also handles collisions.
get: Takes key as arguement, hashes key; assigns a hash-index, returns value from table at the hash-index.
contains: Takes in a key as arguement and returns a boolean if key is already in HashTable.