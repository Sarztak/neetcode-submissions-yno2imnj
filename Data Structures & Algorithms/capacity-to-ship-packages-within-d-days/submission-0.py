class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)

        def days_to_ship(capacity: int) -> int:
            """returns the days required to ship everything given the capacity of ship"""
            i = 0
            curr_sum = 0
            days = 0
            while 0 <= i < n:
                curr_sum += weights[i]
                if curr_sum == capacity:
                    curr_sum = 0 # capacity full start a new window with zero capacity
                    days += 1
                elif curr_sum > capacity:
                    curr_sum = weights[i] # start a new window
                    days += 1
                i += 1

            return days if curr_sum == 0 else days + 1

        max_weight = max(weights)
        lo = max_weight # I need to have at least the capacity to store the biggest weight or else how will I ship
        hi = sum(weights) # If I have a ship that can load everthing at once then I can ship everything in one day

        while lo <= hi:
            w = (lo + hi) // 2
            print(w)
            if days_to_ship(w) <= days < days_to_ship(max(w - 1, max_weight)):
                print(days_to_ship(8 - 1), days_to_ship(8))
                # reducing w any further should increase the days required to 
                # ship the order but having just w days is good enough
                return w
            elif days_to_ship(w) > days: 
                # if the days required to ship are more than 'days'
                # then for all weights 1 to w I cannot ship within 'days'
                # so I need to increase my capacity
                lo = w + 1
            else:
                # if I can ship within 'days' using w capacity then I can 
                # try to reduce w since I need to minimize the capacity
                hi = w - 1
        # the case when w = 1 will fail because days_to_ship(1 - 1) return 0 but 'days' is non-zero 
        return max_weight # weight = 1 is the case that the loop cannot catch
                
                    



        