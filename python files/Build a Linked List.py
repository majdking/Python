class LinkedList:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def add(self, element):
        node = self.Node(element)
        if self.is_empty():
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.length += 1
    
    def __iter__(self):
        list_iter = []
        currect_node = self.head
        while currect_node is not None:
            list_iter.append(currect_node.element)
            currect_node = self.head.next
            print(currect_node.element)
        return iter(list_iter)
        
        

    def remove(self, element):
        previous_node = None
        current_node = self.head
        while current_node is not None and current_node.element != element:
                previous_node = current_node
                current_node = current_node.next
        if current_node is None:
            return
        elif previous_node is not None:
            self.head = current_node.next
        else:
            self.head = current_node.next
        self.length -= 1



my_list = LinkedList()
print(my_list.is_empty())
my_list.add(1)
my_list.add(2)
my_list.add(3)
print(my_list.is_empty())
print(my_list.length)
my_list.remove(1)
print(my_list.length)


