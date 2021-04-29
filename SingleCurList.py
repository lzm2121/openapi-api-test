"""
单向循环链表
"""
class Node(object):
    def __init__(self, node=None):
        self.elem = node
        self.next = None

class SingleCurList(object):
    def __init__(self, node=None):
        self._head = node
        if node:
            node.next = node

    """是否为空"""
    def is_empty(self):
        return self._head == None

    """链表长度"""
    def length(self):
        # 先判断链表是否为空
        if self.is_empty():
            return 0
        cur = self._head
        count = 1
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    """遍历链表"""
    def travel(self):
        if self.is_empty():
            return 0
        cur = self._head
        while cur.next != self._head:
            print(cur.elem, end=' ')
            cur = cur.next
        # 退出循环，cur指向尾节点，但是没有打印尾节点元素
        print(cur.elem)

    """首部添加元素"""
    def add(self, item):
        node = Node(item)
        cur = self._head
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            # 遍历，找到尾节点指向新节点
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            self._head = node
            cur.next = node

    """尾部插入"""
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

    """指定位置插入元素"""
    def insert(self, pos, item):
        cur = self._head
        count = 0
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            while count < (pos-1):
                cur = cur.next
                count += 1
            # 循环退出后，cur指向pos-1处
            node = Node(item)
            node.next = cur.next
            cur.next = node

    """查找结点"""
    def search(self, item):
        cur = self._head
        pos = 0
        if self.is_empty():
            return False
        while cur.next != self._head:
            if cur.elem == item:
                print(pos, end=' ')
            pos += 1
            cur = cur.next
        if cur.elem == item:
            print(pos, end=' ')
        print(end='\n')

    """删除节点"""
    def remove(self, item):
        count = 0
        cur = self._head
        pre = None
        pos = self.search(item)
        while cur.next != self._head:
            if count in pos:
                pre.next = cur.next
            count += 1
            pre.next = cur
            cur = cur.next

if __name__ == '__main__':
    ll = SingleCurList()
    print(ll.is_empty())
    print(ll.length())
    ll.add(1)
    ll.append(2)
    ll.travel()
    ll.add(3)
    ll.travel()
    ll.insert(2, 5)
    ll.insert(3, 3)
    ll.travel()
    ll.search(3)
    ll.remove(3)
    ll.travel()
