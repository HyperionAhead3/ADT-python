class SingleNode(object):
    """双向链表的结点"""
    def __init__(self,item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None
        # prev是前驱结点标识
        self.prev = None

class DoubleLinkList(object):
    """双向链表"""
    '''可以继承SingleLinkList类,__init__ is_empty length travel search方法可继承'''
    def __init__(self,node = None):
        '''用户不传入头节点时默认为None'''
        self.__head = node
        #双下划线为类私有属性，对外不暴露，子类不继承

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        # cur游标，初始时指向头节点
        cur = self.__head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur != None:
            print(cur.item,end = " ")
            cur = cur.next
        print('')

    def add(self, item):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        if self.is_empty():
            self.__head = node
        else:
            # 将新节点的链接域next指向头节点，即__head指向的位置
            node.next = self.__head
            # 将链表的头__head指向新节点
            self.__head = node
            node.next.prev = node

    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将__head指向新节点
        if self.is_empty():
            self.__head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length()-1):
            self.append(item)
        # 找到指定位置
        else:
            node = SingleNode(item)
            count = 0
            cur = self.__head
            while count < pos:
                count += 1
                cur = cur.next
            # 先将新节点node的next指向插入位置的节点
            node.next = cur
            #新结点node的prev指向插入位置的前一个
            node.prev = cur.prev
            # 将插入位置的前一个节点的next指向新节点
            cur.prev.next = node
            # 插入位置结点的prev指向node
            cur.prev = node

    def remove(self,item):
        """删除节点"""
        cur = self.__head
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if cur == self.__head:
                    # 将头指针指向头节点的后一个节点
                    self.__head = cur.next
                    if cur.next:    #判断链表是否只有一个结点
                        cur.next.prev = None
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    cur.prev.next = cur.next
                    if cur.next:    #判断是否是最后一个结点
                        cur.next.prev = cur.prev
                break
            else:
                # 继续按链表后移节点
                cur = cur.next

    def search(self,item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

'''
测试
'''
if __name__ == "__main__":
    ll = DoubleLinkList()
    ll.add(4)
    ll.append(3)
    ll.add(1)
    ll.add(2)
    ll.insert(2, 4)
    print("length:",ll.length())

    print(ll.search(3))
    print(ll.search(5))
    ll.remove(1)
    print("length:",ll.length())
ll.travel()