# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    assist_node = ListNode()
    current_node = assist_node
    # pointers
    p1 = list1
    p2 = list2

    while p1 or p2:
        val1 = p1.val if p1 else None
        val2 = p2.val if p2 else None

        if val1 is not None and val2 is not None:
            if val1 <= val2:
                current_node.next = p1
                p1 = p1.next if p1 else None
            else:
                current_node.next = p2
                p2 = p2.next if p2 else None

        elif val1 is not None:
            current_node.next = p1
            p1 = p1.next if p1 else None

        elif val2 is not None:
            current_node.next = p2
            p2 = p2.next if p2 else None

        current_node = current_node.next

    return assist_node.next
