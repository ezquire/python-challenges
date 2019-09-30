def organize(meetings):
    start_times = list(map(lambda m: m[0], meetings))
    end_times = sorted(map(lambda m: m[1], meetings))

    print(start_times, end_times)


meetings = [(12, 16), (13, 14), (13, 13.5), (14, 15), (15, 16)]

organize(meetings)

def minRooms(times):
    if len(times) == 0: 
        return 0
    rooms = {1: [times[0]]}
    for roomNumber, meetings in rooms.items():
    for i in range(1, len(times)):
        for roomNumber, meetings in rooms.items():
            canAdd = True
            for j in range(len(meetings)):
                meeting1 = times[i]
                meeting2 = meetings[j]
                if meeting1[0] == meeting2[0]:
                    canAdd 
                
    return len(rooms) 
            
            
            
            
            
            
times = [(13, 13.5), (14, 15), (13, 14), (15, 16)]

print(minRooms(times))
