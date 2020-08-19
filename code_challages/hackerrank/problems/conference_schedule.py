"""
3. Conference Schedule
A schedule has just been released for an upcoming tech conference. The schedule provides the start and end times of
each of the presentations. Once a presentation has begun, no one can enter or leave the room. It takes no time to go
from one presentation to another. Determine the maximum number of presentations that can be attended by one
person.
Example
n = 3
scheduleStart = [1, 1, 2]
scheduleEnd =(3, 2, 4]
Using O-based indexing, an attendee could attend any presentation alone, or both presentations 1 and 2. Presentation
O ends too late to be able to attend presentation 2 afterwards. The maximum number of presentations one person can
attend is 2.
Function Description
Complete the function maxPresentations in the editor below.
maxPresentations has the following parameter(s):
scheduleStart[n]: the start times of presentation /
scheduleEnd[n]: the end times of presentation i
Returns:
int: the maximum number of presentations that can be attended by one person
Constraints
• 1573105
• 1 <scheduleStart[i), scheduleEnd[i] = 109
•
| Input Format For Custom Testing
Sample Case 0
Sample Input
STDIN
Function
scheduleStart[] size n
scheduleStart = [1, 1, 2, 3]
1
In man mmt
scheduleEnd[size n = 4
scheduleEnd = [2, 3, 3, 4)
Sample Output
Explanation
An attendee can go to presentations 0, 2, and 3 without conflict. If presentation 1 is chosen, from time 1 to 3, only
two presentations can be attended. The maximum number of presentations a single person can attend is 3.
Sample Case 1
192.14
"""


def maxPresentations(scheduleStart, scheduleEnd):
    # Write your code here

    for i, j in zip(scheduleStart, scheduleEnd):
        meeting = (i, j)
        print(meeting)


maxPresentations([1, 1, 2, 3], [2, 3, 3, 4])
