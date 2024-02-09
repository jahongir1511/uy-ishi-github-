class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    # Helper function to reverse a linked list
    def reverseLinkedList(node):
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev

    # Helper function to find the middle of the linked list
    def findMiddle(node):
        slow = fast = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Helper function to compare two linked lists
    def compareLists(list1, list2):
        while list1 and list2:
            if list1.val != list2.val:
                return False
            list1 = list1.next
            list2 = list2.next
        return True

    if not head or not head.next:
        return True

    # Find the middle of the linked list
    middle = findMiddle(head)

    # Reverse the second half of the linked list
    second_half = reverseLinkedList(middle)

    # Compare the first half and the reversed second half of the linked list
    return compareLists(head, second_half)


# Example usage:
# Construct the linked list
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(1)

head2 = ListNode(1)
head2.next = ListNode(2)

print(isPalindrome(head1))  # Output: True
print(isPalindrome(head2))  # Output: False
