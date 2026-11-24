from collections import defaultdict


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def add_node(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self.size -= 1

    def remove_last(self):
        if self.size == 0:
            return None

        node = self.tail.prev
        self.remove_node(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_size = 0
        self.minFreq = 0

        self.keyMap = {}
        self.freqMap = defaultdict(DoublyLinkedList)

    def update_freq(self, node):
        freq = node.freq

        self.freqMap[freq].remove_node(node)

        if freq == self.minFreq and self.freqMap[freq].size == 0:
            self.minFreq += 1

        node.freq += 1
        self.freqMap[node.freq].add_node(node)

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1

        node = self.keyMap[key]
        self.update_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.keyMap:
            node = self.keyMap[key]
            node.value = value
            self.update_freq(node)
            return

        if self.curr_size == self.capacity:
            lfu_node = self.freqMap[self.minFreq].remove_last()
            del self.keyMap[lfu_node.key]
            self.curr_size -= 1

        new_node = Node(key, value)

        self.keyMap[key] = new_node
        self.freqMap[1].add_node(new_node)

        self.minFreq = 1
        self.curr_size += 1