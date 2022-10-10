class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def get_node(self, index):
        if index < 0:
            return
        current = self.head
        for i in range(index):
            current = current.next
            if current is None:
                return None
        return current
 
def has_cycle(l_list):
    first = l_list.head
    last = l_list.head
    while (last != None and last.next != None):
        first = first.next
        last = last.next.next
        if first == last:
            return True
    return False
 
 
a_llist = LinkedList()
 
data_list = input('Input:').split()
for data in data_list:
    a_llist.append(int(data))
 
length = len(data_list)
if length != 0:
    pos = input('Pos:').strip()
    if pos == '':
        pos = None
    else:
        pos = a_llist.get_node(int(pos))
        a_llist.last_node.next = pos
 
output=has_cycle(a_llist)
print(output)