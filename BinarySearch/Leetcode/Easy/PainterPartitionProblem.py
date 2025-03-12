def can_distribute(boards, max_load, num_painters):
    painter_count = 1
    current_sum = 0
    for board in boards:
        current_sum += board
        if current_sum > max_load:
            painter_count += 1
            current_sum = board
    return painter_count <= num_painters

def minimize_max_painter_load(boards: list, num_painters: int):
    if num_painters > len(boards):
        return -1
    lower_bound = max(boards)
    upper_bound = sum(boards)
    optimal_load = -1
    while lower_bound <= upper_bound:
        candidate_load = lower_bound + (upper_bound - lower_bound) // 2
        if can_distribute(boards, candidate_load, num_painters):
            optimal_load = candidate_load
            upper_bound = candidate_load - 1
        else:
            lower_bound = candidate_load + 1
    return optimal_load