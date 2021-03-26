"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        employee_numbers = {}
        for i in range(len(employees)):
            employee_numbers[employees[i].id] = i
            
        queue = collections.deque([id])
        output = 0
        while len(queue)>0:
            current = queue.popleft()
            employee = employees[employee_numbers[current]]
            output += employee.importance
            for sub in employee.subordinates:
                queue.append(sub)
        return output
        # O(V)
        # space O(V)
        # print(employees[1].id)
        # print(employees[0].subordinates)
        # print(employees[1].importance)
        # print(employees[id-1].subordinates)
            
