# 2933. High-Access Employees
```
class Solution:
  def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
    # Group access times by employee
    emp_access = {}
    for emp, time in access_times:
      if emp not in emp_access:
        emp_access[emp] = []
      emp_access[emp].append(int(time))

    high_access_employees = []

    # Check each employee's access pattern 
    for emp, times in emp_access.items():
      # Sort the access times 
      times.sort()

      # Check for 3 accesses within a 60-minute window (100 in numeric format)
      for i in range(len(times) - 2):
        # If the time difference between the current access and the one 
        # two positions ahead is <= 99 ( which is 60 minutes in this format), 
        # then we have  3 accesses within the window
        if times[i+2] - times[i] <= 99:
          high_access_employees.append(emp)
          break

      return high_access_empplyees
```
