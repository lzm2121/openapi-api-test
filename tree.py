"""
创建树
"""
class Node:
    """节点类"""
    def __init__(self, elem):
        self.elem = elem
        self.rchild = None
        self.lchild = None

class Tree:
    """二叉树"""
    def __init__(self):
        self.root = None # 构造函数，定义一个根节点

    """用队列（列表）实现树的遍历，从而添加节点"""
    def add(self, item):
        node = Node(item)
        # 特殊情况：根节点为空,则直接将要添加的节点当作根节点
        if self.root == None:
            self.root = node
        queue = [self.root]
        # 循环条件：列表为空表示节点遍历结束
        while queue:
            # 判断当前节点(列表中的第一个元素)的左右节点是否有子节点
            cur = queue.pop(0)
            if cur.lchild != None:
                # 有子节点，则将当前节点放入列表后面
                queue.append(cur.lchild)
            else:
                # 无子节点，则将要被添加的节点添加为当前节点的左子节点
                cur.lchild = node
                return
            if cur.rchild != None:
                queue.append(cur.rchild)
            else:
                cur.rchild = node
                return

    """层次遍历:利用队列实现"""
    def breadth_travel(self):
        queue = [self.root]


if __name__ == "__main__":
    tree = Tree()
    tree.add(2)
    tree.add(3)