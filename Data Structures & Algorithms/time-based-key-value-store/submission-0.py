from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timemap:
            values = self.timemap[key]
            previous_timestamps = []
            for val, time in values:
                if timestamp == time:
                    return val
                elif time < timestamp:
                    previous_timestamps.append((val, time))
            if previous_timestamps:
                previous_timestamps.sort(key=lambda x : x[1])
                return previous_timestamps[-1][0]
            else:
                return ""
        else:
            return ""
            

