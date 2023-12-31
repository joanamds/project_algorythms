def study_schedule(permanence_period, target_time):
    if not target_time or not permanence_period:
        return None

    count = 0

    for period in permanence_period:
        if len(period) != 2 or not all(
            isinstance(value, int) for value in period
        ):
            return None
        if period[0] <= target_time <= period[1]:
            count += 1

    return count
