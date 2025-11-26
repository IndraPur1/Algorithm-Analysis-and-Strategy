def activity_selection(activities):
    activities.sort(key=lambda x: x[1])

    selected = []
    selected.append(activities[0])
    last_end_time = activities[0][1]

    for i in range(1, len(activities)):
        start, end = activities[i]
        if start >= last_end_time:
            selected.append(activities[i])
            last_end_time = end

    return selected

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
selected_activities = activity_selection(activities)
print(selected_activities)