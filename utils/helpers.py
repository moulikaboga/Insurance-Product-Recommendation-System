def in_range(value, range_str):
    low, high = map(int, range_str.split("-"))
    return low <= value <= high
