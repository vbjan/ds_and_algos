# Hash Set
*A HashSet is a collection of distinct elements with no particular order. It allows for the storage of unique elements, meaning no two elements in the set are identical.*
- Allows for `adding to set`, `deleting from set` and `membership testing` in $O(1)$
- Useful for
  - Collecting unique items
  - Efficient search operations
  - Excellent at set operations (union, intersection, difference, subset check)
  - Efficiently deleting duplicates in data
  - Membership testing

# Hash Map
*The HashMap is based on the same idea, with some modifications: It stores a set of keys and saves their corresponding values also. This allows for efficient data retrieval by key, offering quick access to the associated values.*


# Array-Based Implementation
- Elements are passed through a hash function and then, depending on the hash value, stored at a resulting index in the underlying array
- To deal with hash collisions each entry in the array stores a linked list, which allows to store multiple elements at one index of the array
- The array is dynamically resized if the `load_factor` exceeds a threshold