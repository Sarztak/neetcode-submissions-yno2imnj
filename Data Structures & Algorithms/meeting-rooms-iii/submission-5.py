from _heapq import heapreplace
from heapq import heapify, heappop, heappush
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda x: (x[0], x[1]))
        l = len(meetings)
        # constraints ensure that there is at least one meeting and one room
        state = []
        heapify(state) 
        heappush(state, (meetings[0][1], 0)) # sort by end time first and then break ties by room number

        empty_room_heap = [i for i in range(1, n)] # leave out the first room as it is filledc
        heapify(empty_room_heap)

        meetings_counter = [0] * n
        meetings_counter[0] = 1 # one room scheduled for first meeting
        i = 1
        
        
        while i < l:
            
            # there may be cases where two or more room can have meeting ending at the same time
            # in that case we need to remove all the rooms and make them empty
            # which also means that I need to seprately keep track of all the available rooms
            # and that cannot be done by just nothing down the room number in the heap

            while state and state[0][0] <= meetings[i][0]: # the first room that is available with the smallest room number
                _, room_number = heappop(state) # remove the last meeting
                # put in empty_room_heap because a room became empty
                heappush(empty_room_heap, room_number)
                
            
            if empty_room_heap: # check if there are room available to fill
                next_empty_room = heappop(empty_room_heap)
                heappush(state, (meetings[i][1], next_empty_room))
                meetings_counter[next_empty_room] += 1
                i += 1
               
            else:
                # if no room is available then schedule the next meeting in the room that has earliest availability
                # remove all the room that end at the earliest time
                earliest_end_time = state[0][0]

                while state and state[0][0] == earliest_end_time:
                    _, room_number = heappop(state)
                    heappush(empty_room_heap, room_number)
                  
                # now there is again a gotcha I can schedule all the backlogged meeting that were going to start before
                # the earliest_end_time and not just one until all the room are filled again
                while empty_room_heap and i < l and meetings[i][0] <= earliest_end_time:
                    # now add the meeting to first available empty room 
                    next_empty_room = heappop(empty_room_heap)
                    new_end_time = earliest_end_time + (meetings[i][1] - meetings[i][0])
                    heappush(state, (new_end_time, next_empty_room))
                    meetings_counter[next_empty_room] += 1
                    i += 1
                    
                    
        
        # find the room with most number of meeting and then break_tiles by room number
        meetings_counter = [(-count, index) for index, count in enumerate(meetings_counter)]
        meetings_counter = sorted(meetings_counter, key=lambda x: (x[0], x[1]))
        return meetings_counter[0][1] # room_number with max count is in the beginning
            
