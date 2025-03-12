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
    start = max(boards)
    end = sum(boards)
    optimal_load = -1
    while start <= end:
        candidate_load = start + (end - start) // 2
        if can_distribute(boards, candidate_load, num_painters):
            optimal_load = candidate_load
            end = candidate_load - 1
        else:
            start = candidate_load + 1
    return optimal_load
if __name__ == "__main__":
    test_cases = [
        ([10, 20, 30, 40], 2),
        ([10, 10, 10, 10], 2),
        ([10, 20, 30, 40, 50], 3)
    ]
    
    for i, (boards, num_painters) in enumerate(test_cases, 1):
        result = minimize_max_painter_load(boards, num_painters)
        print(f"Test Case {i}: Minimum maximum load for {num_painters} painters is: {result}")