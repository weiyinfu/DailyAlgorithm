class Node:
    def __init__(self, v):
        self.next = None
        self.value = v


def reverse(no: Node) -> Node:
    i = no
    last = None
    while i:
        temp = i.next
        i.next = last
        last = i
        i = temp
    return last


def main():
    a = [1, 2, 3, 4, 5]
    a = [Node(i) for i in a]
    for i in range(len(a) - 1):
        a[i].next = a[i + 1]
    b = reverse(a[0])

    i = b
    while i:
        print(i.value)
        i = i.next


main()
