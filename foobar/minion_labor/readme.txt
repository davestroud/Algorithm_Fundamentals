Minion Labor Shifts
===================

Commander Lambda's minions are upset! They're given the worst jobs 
on the whole space station, and some of them are starting to complain 
that even those worst jobs are being allocated unfairly. If you can 
fix this problem, it'll prove your chops to Commander Lambda so you 
can get promoted!

Minions' tasks are assigned by putting their ID numbers into a list, 
one time for each day they'll work that task. As shifts are planned 
well in advance, the lists for each task will contain up to 99 integers. 
When a minion is scheduled for the same task too many times, they'll
complain about it until they're taken off the task completely. 
Some tasks are worse than others, so the number of scheduled assignments
before a minion will refuse to do a task varies depending on the task.  
You figure you can speed things up by automating the removal of the 
minions who have been assigned a task too many times before they 
even get a chance to start complaining.

Write a function called solution(data, n) that takes in a list of less 
than 100 integers and a number n, and returns that same list but with 
all of the numbers that occur more than n times removed entirely. 
The returned list should retain the same ordering as the original 
list - you don't want to mix up those carefully-planned shift rotations!
For instance, if data was [5, 10, 15, 10, 7] and n was 1, 
solution(data, n) would return the list [5, 15, 7] because 10 
occurs twice, and thus was removed from the list entirely.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([1, 2, 3], 0)
Output:
    

Input:
solution.solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
Output:
    1,4

-- Java cases --
Input:
Solution.solution({1, 2, 3}, 0)
Output:
    

Input:
Solution.solution({1, 2, 2, 3, 3, 3, 4, 5, 5}, 1)
Output:
    1,4

Use verify [file] to test your solution and see how it does. 
When you are finished editing your code, use submit [file] to 
submit your answer. If your solution passes the test cases, 
it will be removed from your home folder.