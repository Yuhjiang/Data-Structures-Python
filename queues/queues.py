"""
堆栈
基于链表实现
"""


class Node(object):
    def __init__(self, element):
        self.element = element
        self.next = None


class Queue(object):
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        deleted_node = self.front

        if self.is_empty():
            return False
        elif self.size == 1:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        self.size -= 1

        return deleted_node.element
