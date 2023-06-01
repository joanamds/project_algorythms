def study_schedule(permanence_period, target_time):
    count = 0
    if not permanence_period:
        return None
    elif not target_time:
        return None
    else:
        # permanence_period são tuplas
        # exemplo: [(2, 2), (1, 2)...]
        for period in permanence_period:
            # por isso é possível acessar os índices
            if period[0] <= target_time <= period[1]:
                count += 1

    return count

# target_time é o horário que está sendo testado
