def max_window_sum(readings, k):
    if not readings or k <= 0 or k > len(readings):
        raise ValueError()

    if all(r < 0 for r in readings):
        return sum(sorted(readings, reverse=True)[:k])

    first_neg = None
    for i, v in enumerate(readings):
        if v < 0:
            first_neg = i
            break

    start = first_neg if first_neg is not None else 0
    if start + k > len(readings):
        start = len(readings) - k

    window_sum = sum(readings[start:start+k])
    max_sum = window_sum

    for i in range(start + k, len(readings)):
        window_sum += readings[i] - readings[i - k]
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum


if __name__ == "__main__":
    sample_readings = [3, 1, 2, 7, 4, 2]
    sample_k = 3
    print(max_window_sum(sample_readings, sample_k))
