from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        is_not_end = True
        result = []
        prob = {}
        index = 0
        while is_not_end:
            is_not_end = False
            for one_list in lists:
                if len(one_list) > index:
                    prob[one_list[index]] = 1 if one_list[index] not in prob else prob[one_list[index]] + 1
                    is_not_end = True
            index += 1

        for num, count in prob.items():
            result += [num]*count

        return result

sol = Solution()

sol.mergeKLists([[1,4,5],[1,3,4],[2,6]])