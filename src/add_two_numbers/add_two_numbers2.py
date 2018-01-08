# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    l3 = ListNode(0)
    head = l3
    while l1 is not None or l2 is not None:
        if l1 is not None and l2 is not None:
            l3.val = l1.val + l2.val
            l1 = l1.next
            l2 = l2.next
        elif l1 is not None:
            l3.val = l1.val
            l1 = l1.next
        elif l2 is not None:
            l3.val = l2.val
            l2 = l2.next
        if l3.val > 9:
            l3.val = l3.val - 10
            if l1 is None:
                l1 = ListNode(1)
            else:
                l1.val = l1.val + 1
        if l3.next is None and (l1 is not None or l2 is not None):
            l3.next = ListNode(0)
        l3 = l3.next
    return head


def print_list_node(l):
    while l is not None:
        print(l.val)
        l = l.next


l10 = ListNode(2)
l11 = ListNode(4)
l12 = ListNode(3)
l13 = ListNode(1)
l10.next = l11
l11.next = l12
l12.next = l13

l20 = ListNode(5)
l21 = ListNode(6)
l22 = ListNode(4)
l23 = ListNode(2)
l24 = ListNode(3)
l20.next = l21
l21.next = l22
l22.next = l23
l23.next = l24

head = add_two_numbers(l10, l20)
print_list_node(head)
