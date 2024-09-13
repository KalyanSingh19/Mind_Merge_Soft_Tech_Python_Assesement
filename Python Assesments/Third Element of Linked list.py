class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def find_third_from_last(self):
        if self.head is None or self.head.next is None or self.head.next.next is None:
            return None

        slow = self.head
        fast = self.head

        
        for _ in range(3):
            fast = fast.next

        
        while fast:
            slow = slow.next
            fast = fast.next

        return slow.data


my_list = SinglyLinkedList()


my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)


third_from_last = my_list.find_third_from_last()
if third_from_last:
    print("Third element from the last:", third_from_last)
else:
    print("Linked list is too short")