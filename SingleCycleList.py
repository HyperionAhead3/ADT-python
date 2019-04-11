class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None


class SingleCircleList(object):
    """单向循环链表"""
    def __init__(self,node = None):
        '''用户不传入头节点时默认为None'''
        self.__head = node
        #双下划线为类私有属性，对外不暴露，子类不继承
        #如果传入不是空则循环
        if node:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        # cur游标，初始时指向头节点
        cur = self.__head
        count = 1
        # 尾节点指向None，当未到达尾部时
        while cur.next != self.__head:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return 
        cur = self.__head
        while cur.next != self.__head:
            print(cur.item,end = " ")
            cur = cur.next
        #退出循环后尾节点没有打印
        print(cur.item)

    def add(self, item):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 将新节点的链接域next指向头节点，即__head指向的位置
            node.next = self.__head
            # 将链表的头__head指向新节点
            self.__head = node
            cur.next = self.__head

    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将__head指向新节点
        if self.is_empty():
            self.__head = node
            node.next = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

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
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self.__head
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self,item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self.__head
        pre = None

        while cur.next != self.__head:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if cur == self.__head:
                    rear = self.__head    #设置游标rear最终指向尾结点
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next    #头结点删除
                    rear.next = self.__head
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                return
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next
        #退出循环后，要删除的是尾节点
        if cur.item == item:
            if cur == self.__head:
            #链表只有一个结点
                self.__head = None
            else:
                pre.next = self.__head

    def search(self,item):
        """链表查找节点是否存在，并返回True或者False"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur != self.__head:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        #
        if cur.item == item:
            return True
        return False

'''
测试
'''
if __name__ == "__main__":
    ll = SingleCircleList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    print("length:",ll.length())

    print(ll.search(3))
    print(ll.search(5))
    ll.remove(1)
    print("length:",ll.length())
    ll.travel()