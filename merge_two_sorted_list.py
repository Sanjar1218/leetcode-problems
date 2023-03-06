from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    lst1 = []
    lst2 = []

    while list1.next:
        lst1.append(list1.val)
        list1 = list1.next
    
    while list2.next:
        lst2.append(list2.val)
        list2 = list2.next

    lst = lst1 + lst2
    listnode = ListNode(lst[0])
    for i in lst[1:]:
        listnode.next = ListNode(i)
        listnode = listnode

    return sorted(lst)

if __name__ == '__main__':
    print(mergeTwoLists([1,2,4], [1,3,4]))
    print(mergeTwoLists([], []))
    print(mergeTwoLists([], [0]))