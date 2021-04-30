class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class Solution:
    def __init__(self, node=None):
        self._head = Node(node)

    def BuildList(self):
        cur = self._head
        elem = input("输入节点：")
        while elem != '#':
            node = Node(int(elem))
            cur.next = node
            cur = cur.next
            elem = input("输入节点:")
        return self._head


    def ReverseList(self, phead):
        if not phead:
            # phead为空
            return None
        cur = phead
        pre = None
        while phead:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

if __name__ == '__main__':
    ll = Solution()
    list = ll.BuildList()
    ll.ReverseList(list)


