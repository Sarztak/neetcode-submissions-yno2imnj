"""
The standard solution to this problem is hard to for me to justify physically. 
I can write the code but I don't understand why it works or even why it is physically correct.
Someone in their great insight said "this is the solution" and then those who don't 
question it, just accepted that is the solution. Nobody cared after that.
The idea is to throw physics out of the door and only compare the time it would take for each 
car to reach the target if it won't change the speed after catching up and then compare the arrival times.
Two cars catch if the car behind has smaller arrival time than the car in the front. Sounds plausible
until you start considering cases such as if there are cars in the order C, B, A. And C cannot catch up to B 
because B is faster but then B catches up to A and slows down so that now C can catch up. How does the solution
handle this case. or if C and B both catch up to A at the same time. or C and B catch up first and then they 
catch up to A. 

The solution only give proceduce to get answer but not explain how this handle the physical reality. 
All one does in this problem is to sort by position and then compare the arrival time and update the 
arrival time with that of the larger arrival time. 
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cp = [(x, y) for x, y in zip(position, speed)]
        cp = sorted(cp, key=lambda x: x[0])

        stack = []

        for p, s in cp:
            curr_arrival_time = (target - p) / s
            while stack and stack[-1] <= curr_arrival_time:
                stack.pop()
            stack.append(curr_arrival_time)
        
        return len(stack)
        