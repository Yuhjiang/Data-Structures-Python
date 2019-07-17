class Node(object):
    def __init__(self, element, next=None, previous=None):
        self.element = element
        self.next = next
        self.previous = previous


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def is_emtpy(self):
        return self.head is None

    def length(self):
        list_length = 0
        temp = self.head
        while temp:
            temp = temp.next
            list_length += 1

        return list_length

    # 1.开始处插入数据
    def insert_at_head(self, element):
        new_node = Node(element)
        if self.head is None:
            self.tail = new_node
        else:
            self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node

    # 2.开始处删除数据
    def delete_at_head(self):
        temp = self.head
        self.head = temp.next
        if self.head is None:
            self.tail = None
        else:
            self.head.previous = None

        return temp

    # 3.尾巴处插入数据
    def insert_at_tail(self, element):
        new_node = Node(element)
        if self.tail is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node

    # 4.尾巴处删除数据
    def delete_at_tail(self):
        temp = self.tail
        self.tail = temp.previous
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        return temp

    # 5.任意位置插入数据
    def insert_at_index(self, element, index):
        if index == 1:
            self.insert_at_head(element)
        elif index == self.length() + 1:
            self.insert_at_tail(element)
        else:
            new_node = Node(element)
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next.previous = new_node
            temp.next = new_node
            new_node.previous = temp

    # 6.任意位置删除数据
    def delete_at_index(self, index):
        if index == 1:
            return self.delete_at_head()
        elif index == self.length():
            return self.delete_at_tail()
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            temp.previous.next = temp.next
            temp.next.previous = temp.previous

            return temp

    def __str__(self):
        s_forward = []
        temp = self.head
        while temp is not None:
            s_forward.append(temp.element)
            temp = temp.next

        s_backward = []
        temp = self.tail
        while temp is not None:
            s_backward.append(temp.element)
            temp = temp.previous

        return ' -> '.join(s_forward) + '\n' + ' -> '.join(s_backward)
