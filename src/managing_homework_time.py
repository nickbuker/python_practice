def time_per_day(tasks):
    times = [t[0] * t[1] * 0.75 / 60. for t in tasks]
    return round(sum(times) / 5., 2)
