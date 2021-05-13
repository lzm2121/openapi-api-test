class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class Solution:
    def __init__(self, node=None):
        self._head = node

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

import datetime

if __name__ == '__main__':
    # ll = Solution()
    # list = ll.BuildList()
    # ll.ReverseList(list)
    import sys
    #
    nums = [int(i) for i in input().split('/')]
    numerator, denominator = nums[0], nums[1]
    result = ""
    d = {}
    if (numerator < 0) ^ (denominator < 0):
        result += '-'
    numerator, denominator = abs(numerator), abs(denominator)
    div, mod = divmod(numerator, denominator)
    if div == 0:
        result += str(div)
    result += str(div) + '.'
    d[mod] = len(result) # 记录余数以及对应的位置，该位置就是要插入括号的位置
    while mod:
        mod *= 10
        div, mod = divmod(mod, denominator)
        result += str(div)
        if mod in d:
            index = d[mod] # 若余数已经存在，则找到该余数所对应的位置，在该余数之前插入（
            result = result[:index] + '(' + result[index:] + ')'
            break
        d[mod] = len(result)

    sys.stdout.write(result)