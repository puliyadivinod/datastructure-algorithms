__author__ = 'vinu'


class Node(object):
    def __init__(self, data, next_node=None):
        self.next = next_node
        self.data = data

    def __str__(self):
        self.data


class LinkedLists(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, data, next_node=None):
        if data is None:
            return
        node = Node(data, next_node)
        if self.head is None:
            self.head = node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = node
        return node

    def insert_to_front(self, data):
        if data is None:
            return
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        return node

    def get_all_data(self):
        data = []
        curr_node = self.head
        while curr_node is not None:
            data.append(curr_node.data)
            curr_node = curr_node.next
        return data


if __name__ == '__main__':
    ll = LinkedLists(None)
    ll.insert_to_front(10)
    ll.insert_to_front(True)

    ll.append('abc')

    print ll.get_all_data()
    assert (ll.get_all_data() == [True, 10, 'abc']), "Testing"

    ll.insert_to_front(False)
    ll.insert_to_front(1)
    ll.insert_to_front(2)
    ll.insert_to_front(3)

    ll.append('def')
    ll.append('ghi')
