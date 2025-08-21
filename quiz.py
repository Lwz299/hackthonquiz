def find_missing_ranges(frames: list[int]) -> dict:
    n = len(frames)
    for i in range(n):
        for j in range(i + 1, n):
            if frames[i] > frames[j]:
                frames[i], frames[j] = frames[j], frames[i]

    frame_set = set(frames)
    missing_frames = []
    for x in range(1, frames[-1] + 1):
        if x not in frame_set:
            missing_frames.append(x)

    if not missing_frames:
        return {"gaps": [], "longest_gap": None, "missing_count": 0}

    gaps = []
    start = end = missing_frames[0]

    for i in range(1, len(missing_frames)):
        if missing_frames[i] == end + 1:
            end = missing_frames[i]
        else:
            gaps.append([start, end])
            start = end = missing_frames[i]

    gaps.append([start, end])
    longest_gap = gaps[0]
    for g in gaps:
        if g[1] - g[0] > longest_gap[1] - longest_gap[0]:
            longest_gap = g

    missing_count = len(missing_frames)
    return {"gaps": gaps, "longest_gap": longest_gap, "missing_count": missing_count}


