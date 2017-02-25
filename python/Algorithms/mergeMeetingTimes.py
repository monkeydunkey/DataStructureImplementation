def getConsolidatedSchedule(sch):
    sch = sorted(sch, key = lambda x : x[0])
    max_end = sch[0][1]
    min_start = sch[0][0]
    cons = []
    for i in range(1, len(sch)):
        if sch[i][0] <= max_end:
            max_end = max(max_end, sch[i][1])
        else:
            cons.append((min_start, max_end))
            min_start = sch[i][0]
            max_end = sch[i][1]
    cons.append((min_start, max_end))
    return cons
if __name__ == '__main__':
    schedules = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    print getConsolidatedSchedule(schedules)
