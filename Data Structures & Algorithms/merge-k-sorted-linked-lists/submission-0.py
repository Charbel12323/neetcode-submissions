# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        while len(lists) > 1:
            merged_list = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]

                if i + 1 < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None
                
                merged = self.mergeTwoLists(list1, list2)
                merged_list.append(merged)
            
            lists = merged_list
        return lists[0]
    
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next
        
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        return dummy.next
            
