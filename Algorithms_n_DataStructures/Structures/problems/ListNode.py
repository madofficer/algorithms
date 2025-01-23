class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(a: list):
    if not a:
        return None

    head = ListNode(a[0])
    curr_node = head
    for i in a[1:]:
        curr_node.next = ListNode(i)
        curr_node = curr_node.next

    return head


def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")