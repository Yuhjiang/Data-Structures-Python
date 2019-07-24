"""
链表相关的算法
"""


class Node(object):
    def __init__(self, element):
        self.element = element
        self.next = None

    def __str__(self):
        return str(self.element)

    def __lt__(self, other):
        return self.element < other.element


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        temp = self.head
        s = []
        while temp:
            s.append(str(temp))
            temp = temp.next
        s.append('None')
        return ' -> '.join(s)

    def length(self):
        temp = self.head
        num = 0
        while temp:
            num += 1
            temp = temp.next

        return num

    def initial(self, elements):
        self.head = Node(elements.pop(0))
        head = self.head
        for e in elements:
            new_node = Node(e)
            head.next = new_node
            head = head.next

    """
    链表成对调换
    1 -> 2 -> 3 -> None
    2 -> 1 -> 3 -> None
    """
    def exchange(self):
        self.head = self.exchange_helper(self.head)

    @staticmethod
    def exchange_helper(head):
        if head is None or head.next is None:
            return head
        temp = head.next
        head.next = LinkedList.exchange_helper(temp.next)
        temp.next = head
        return temp

    """
    分叉链表求交点
    1 -> 2 -> 3 -> 4 -> 5 -> 1 -> 2 -> None
                   4 -> 5 -> 1 -> 2 -> None
    较长的链表先移动，直到和短链表一样
    """
    @staticmethod
    def cross_list(list1, list2):
        len1, len2 = list1.length(), list2.length()

        head1 = list1.head
        head2 = list2.head

        if len1 > len2:
            for _ in range(len1 - len2):
                head1 = head1.next
        else:
            for _ in range(len2 - len1):
                head2 = head2.next

        while head1 and head2:
            if head1 == head2:
                    return head1
            head1 = head1.next
            head2 = head2.next
        else:
            return None

    """
    pa，pb分别从自己的头结点开始遍历，遍历结束就从对方头结点开始遍历，
    两者最终都会走过相同的节点最后相交
    """
    @staticmethod
    def cross_point_2(list1, list2):
        p1, p2 = list1.head, list2.head

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
            if p1 is None:
                p1 = list2.head
            if p2 is None:
                p2 = list1.head
        return p1

    """
    单链表翻转，递归方法
    """
    def reverse(self):
        self.head = self.reverse_helper(self.head)

    @staticmethod
    def reverse_helper(head):
        if head is None or head.next is None:
            return head
        temp = LinkedList.reverse_helper(head.next)
        head.next.next = head
        head.next = None

        return temp

    """
    单链表翻转，非递归方法
    1 -> 2 -> 3 -> None
    2 -> 3 -> None <- 1
    3 -> None <- 1 <- 2
    None <- 1 <- 2 <- 3
    """
    def reverse_loop(self):
        curr = self.head
        if curr is None:
            return None
        prev, temp = None, None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        self.head = prev

    """
    单链表判断是否有环
    快慢指针遍历链表，一个速度为1，另一个速度为2
    """
    def has_cycle(self):
        if self.head is None:
            return False
        slow, fast = self.head, self.head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

    """
    单链表找环入口
    当快慢指针相遇时，慢指针正好走到一半的位置，这时从头在走一个慢指针
    两个慢指针相遇的地方即是交点
    """
    def cross_point(self):
        if self.head is None:
            return None
        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # 相遇后，从头再来一个慢指针
                slow2 = self.head
                while slow2 != slow:
                    slow2 = slow2.next
                    slow = slow.next
                return slow

        return None

    """
    单链表找中间节点
    快慢指针，快指针走到链表结尾，慢指针正好在中间
    """
    def find_middle(self):
        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    """
    单链表合并
    两个链表已经排好序
    """
    @staticmethod
    def merge_list(list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        new_list = LinkedList(Node(-1))
        head = new_list.head
        head1, head2 = list1.head, list2.head

        while head1 and head2:
            if head1 < head2:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            head = head.next
        if head1:
            head.next = head1
        if head2:
            head.next = head2

        new_list.head = new_list.head.next
        return new_list



def reset(data):
    l = LinkedList()
    l.initial(data)

    return l


if __name__ == '__main__':
    l = reset([1, 2, 3, 4])
    print(l)

    # 1.链表成对调换
    print('1.链表成对调换:  ', l)

    # 2.交叉链表求交点
    l1 = LinkedList()
    l1.initial([1, 2, 3, 4, 5, 1, 2])
    l2 = LinkedList()
    l2.initial([3, 5])
    l2.head.next.next = l1.head.next.next.next
    print('2.交叉链表求交点:  ', LinkedList.cross_list(l1, l2))

    # 3.单链表翻转，递归方法
    l = reset([1, 2, 3, 4])
    l.reverse()
    print(l)

    # 4.单链表翻转，非递归方法
    l = reset([1, 2, 3, 4])
    l.reverse_loop()
    print(l)

    # 5.单链表判断是否有环
    l = reset([1, 2, 3, 4])
    l.head.next.next.next.next = l.head.next

    print(l.has_cycle())

    # 6.单链表找环入口
    l = reset([1, 2, 3, 4])
    l.head.next.next.next.next = l.head.next

    print(l.cross_point())

    # 7. 单链表找交点
    l1 = LinkedList()
    l1.initial([1, 2, 3, 4, 5, 1, 2])
    l2 = LinkedList()
    l2.initial([3, 5])
    l2.head.next.next = l1.head.next.next.next
    print(LinkedList.cross_point_2(l1, l2))

    # 单链表找中点
    l = reset([1, 2, 3, 4, 5])
    print(l.find_middle())

    # 单链表合并
    l1 = LinkedList()
    l1.initial([1, 3, 5, 7])
    l2 = LinkedList()
    l2.initial([2, 4])
    l3 = LinkedList.merge_list(l1, l2)
    print(l3)
