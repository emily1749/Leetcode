# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # if lists == None: return None
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heap.append((lists[i].val, i))
                lists[i] = lists[i].next
            
        heapq.heapify(heap)
        dummy = ListNode()
        curr_list = dummy
        while len(heap)>0:
            curr = heapq.heappop(heap)
            curr_val, curr_idx = curr[0], curr[1]
            curr_list.next = ListNode(curr_val)
            curr_list = curr_list.next
            
            if lists[curr_idx]:
                heapq.heappush(heap, (lists[curr_idx].val, curr_idx))
                lists[curr_idx] = lists[curr_idx].next
        curr_list.next = None
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #push first items into a heap
        # if len(lists)==0:
        #     return None
        # if len(lists)==1:
        #     return lists[0]
        
#         heap = []
#         for i in range(len(lists)):
#             if lists[i]:
#                 heap.append((lists[i].val, i))
#         heapq.heapify(heap)
#         result_list = ListNode()
#         head = result_list
#         print(heap)
        
#         while len(heap)>0:
#             current = heapq.heappop(heap)
#             current_val = current[0]
#             current_list_idx = current[1]
#             result_list.next = ListNode()
#             result_list = result_list.next
#             result_list.val = current_val
#             lists[current_list_idx] = lists[current_list_idx].next
#             if lists[current_list_idx] != None:
#                 heapq.heappush(heap, (lists[current_list_idx].val, current_list_idx))
                
#         result_list.next = None
#         return head.next
            