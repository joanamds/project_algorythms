def study_schedule(permanence_period, target_time):
    count = 0
    if not target_time or not permanence_period:
        return None
    # permanence_period são tuplas
    # exemplo: [(2, 2), (1, 2)...]
    for period in permanence_period:
        if len(period) != 2:
            return None
        # por isso é possível acessar os índices
        if period[0] <= target_time <= period[1]:
            count += 1

    return count

# target_time é o horário que está sendo testado
