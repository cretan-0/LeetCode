#v1 - Time Limit - using lists

from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        res = []
        for elem in meetings:
            for i in elem:
                start = elem[0]
                end = elem[1]
                z = [j for j in range(start, end+1)]
                maxim = max(z)
                maxim = max(maxim, days)
                res.extend(z)
                break

        a = [i for i in range(1, days+1) if i not in res]
        return len(a)

  #v2 - Memory Limit - using set()

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        reserved_days = set()
        for start, end in meetings:
            reserved_days.update(range(start, end+1))
        return days - len(reserved_days)

# the accepted one

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if days <= 0:
            return 0
        
        # Sortează intervalele după început
        meetings.sort(key=lambda x: x[0])
        merged = []
        
        # Unifică intervalele care se suprapun
        for start, end in meetings:
            # Dacă lista merged e goală sau intervalul curent nu se suprapune cu ultimul interval din merged
            if not merged or start > merged[-1][1] + 1:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        
        # Calculează numărul total de zile rezervate, ținând cont de limita [1, days]
        reserved = 0
        for s, e in merged:
            # Limităm intervalul la [1, days]
            start_interval = max(s, 1)
            end_interval = min(e, days)
            if start_interval <= end_interval:
                reserved += (end_interval - start_interval + 1)
        
        # Zilele libere sunt zilele totale minus zilele rezervate
        return days - reserved
