__author__ = 'vinu'


class Node:
    def __init__(self, contents=None, next=None):
        self.contents = contents
        self.next = next

    def get_contents(self):
        return self.contents

    def __str__(self):
        return str(self.contents)


def print_list(node):
    while node:
        print(node.get_contents())
        node = node.next
    print


if __name__ == '__main__':
    n1 = Node("Car")
    n2 = Node("Lorry")
    n3 = Node("Bus")

    n1.next = n2
    n2.next = n3

    print_list(n1)
