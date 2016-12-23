def pick_peaks(arr):
    pos, peaks, plat_pos, plat_peak = [], [], [], []
    old1, old2 = -100, -100
    for i, n in enumerate(arr):
        if n < old1 and old1 > old2 and i > 1:
            pos.append(i - 1)
            peaks.append(old1)
        if n == old1 and old1 > old2 and i > 1:
            plat_pos.append(i - 1)
            plat_peak.append(old1)
        if n < old1 and old1 == old2 and i > 1:
            try:
                pos.append(plat_pos.pop())
                peaks.append(plat_peak.pop())
            except IndexError:
                continue
        old2 = old1
        old1 = n
    return {"pos":pos, "peaks":peaks}
