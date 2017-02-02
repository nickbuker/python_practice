def travel(total_time, run_time, rest_time, speed):
    dist = 0
    while total_time > 0:
        if total_time > run_time:
            dist += run_time * speed
            total_time -= run_time
        else:
            dist += total_time * speed
            total_time = 0
        if total_time > rest_time:
            total_time -= rest_time
        else:
            total_time = 0
    return dist
