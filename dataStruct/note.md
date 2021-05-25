1. data struct only have sequence storage and chain storage
2. queue and stack can be realized by sequence(need to solve expansion) or chain
3. graph have adjacency array and chain method to realized
4. the hash table is to map the keys to a large array through the hash function. and for the method of resolving hash conflicts. the zipper method requires linked list characteristics,and for linear probing method requires array characteristics
5. tree, using an array to achieve is a heap, because the heap is a complete binary tree , using an array to store does not require node pointers, and the operation is relatively simple,using a linked list to achieve is a very common kind of tree, because it is not necessarily a complete binary tree

