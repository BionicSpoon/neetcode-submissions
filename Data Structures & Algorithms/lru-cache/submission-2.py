class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev       

    def __repr__(self) -> str:
        return f'Node({self.key}, {self.val})' 
        

class LRUCache:

    def __init__(self, capacity: int):
        # internal storage is a doubly linked list
        # this list will keep the most recently accessed element at the tail
        # and the least recently accessed at the head
        # we will have a Dict[key: Node] for O(1) lookup of Node addresses
        # Thus, whenever we get(), we will remove the Node from that pos, and move it to the end
        # of the doubly linked list
        # Whenever we get, we will append the node to the list, and pop the head if the capactity
        # has been exceeded.
        # We need to be sure to also update the table whenever the linked list is changed
        # That's it ?
        self.table = {}
        self.capacity = capacity
        self.size = 0

        # doubly linked list members
        self.head = Node()
        self.tail = Node()

        # connect internal linked list
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        '''Return the value associated with the key if it is in the table, else None.'''
        print(f'get({key}) called and table is {self.table}')
        if key not in self.table:
            return -1
        self.move_to_back(self.table[key])
        print(self.table, 'right before get returns')
        return self.table[key].val

    def put(self, key: int, value: int) -> None:
        print(f'put({key}, {value}) called')
        if key in self.table:
            self.table[key].val = value
            self.move_to_back(self.table[key])
            return None

        if self.size == self.capacity:
            self.remove(self.head.next)        

        new_node = Node(key, value)
        self.append(new_node)
        self.table[key] = new_node

    def append(self, node) -> None:
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.table[node.key] = node
        self.size += 1

    def remove(self, node) -> None:
        print(f'self.remove({node}) called')
        if not node.prev or not node.next:
            return "Hello"
        node.prev.next = node.next
        node.next.prev = node.prev
        if node.key in self.table:
            del self.table[node.key]
        self.size -= 1
        print(self.table)

    def move_to_back(self, node) -> None:
        self.remove(node)
        self.append(node)

    

        
