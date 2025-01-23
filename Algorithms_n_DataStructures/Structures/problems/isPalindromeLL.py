from typing import Optional

from Algorithms_n_DataStructures.Structures.problems.ListNode import ListNode, list_to_linked_list, print_list

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy_node = ListNode()
        current_node = head
        if current_node:
            dummy_node.val = current_node.val
            current_node = current_node.next

        while current_node:
            new_node = ListNode(current_node.val)
            new_node.next = dummy_node
            dummy_node = new_node
            current_node = current_node.next


        current_node1 = dummy_node
        current_node = head
        while current_node and current_node1:
            if current_node.val != current_node1.val:
                return False
            else:
                current_node = current_node.next
                current_node1 = current_node1.next

        return True

print(Solution().isPalindrome(list_to_linked_list([1, 2, 1])))