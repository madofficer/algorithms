from typing import Optional

from Algorithms_n_DataStructures.Structures.problems.ListNode import ListNode, list_to_linked_list, print_list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        dummy_node = ListNode()
        if current_node:
            dummy_node.val = current_node.val
            current_node = current_node.next
        else:
            return dummy_node.next


        while current_node:
            new_node = ListNode(current_node.val)
            new_node.next = dummy_node
            dummy_node = new_node
            current_node = current_node.next

        return dummy_node

print_list(Solution().reverseList(list_to_linked_list([])))
