class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} 

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    

    def insert_to_head(self, node:Node) -> None:
        # Inserting the already existing node to the head 
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head 
        node.next = next_node
        next_node.prev = node
    def delete(self, node:Node) -> None:
        # Deletion will only happen of the last node of the linkedlist
        node_next = node.next
        node_prev = node.prev 
        node_prev.next = node_next
        node_next.prev = node_prev
    def get(self, key: int) -> int:
        if(key not in self.cache):
            return -1
        # If the node is present in the head delete it and again insert it from the head 
        node_delete = self.cache[key] #Gives me the node
        self.delete(node_delete)
        self.insert_to_head(node_delete)
        return node_delete.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move node to the head
            node = self.cache[key]
            node.val = value
            self.delete(node)
            self.insert_to_head(node)
        # If the node is not in cache 
        else:
            # Create a brand new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insert_to_head(new_node)
            
            # Check capacity; evict Least Recently Used (node before tail) if exceeded
            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                self.delete(lru_node)
                del self.cache[lru_node.key]

        