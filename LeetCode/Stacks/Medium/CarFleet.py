"""
------------------------------------------------------------------------------------------------------------------------------------------------
22. Generate Parentheses (NeetCode)

There are n cars going to the same destination along a one-lane road. The destination is target miles 
away.
You are given two integer array position and speed, both of length n, where position[i] is the 
position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to 
bumper at the same speed. The faster car will slow down to match the slower car's speed. 
The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. 
Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be 
considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Example 2:

Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, hence there is only one fleet.

Example 3:

Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.

------------------------------------------------------------------------------------------------------------------------------------------------
Solution Walkthrough

We want to calculate the time it takes for the cars to reach the target destination. Distance minus current
distance, divided by speed. Then check is the stack has 2 or more values, and the stack at -1 is less/equal
to stack at -2. if this is the case, we have a collision because stack[-1] will run into the one below it: 
at this point we want to pop the value because it is added to the fleet, which is the car in front.

Return the length of the stack.

Time complexity: O(nlogn). 
Space complexity: O(n). We are using a stack 
------------------------------------------------------------------------------------------------------------------------------------------------
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
