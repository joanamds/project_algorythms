# def study_schedule(permanence_period, target_time):
#     count = 0
#     if not target_time or not permanence_period:
#         return None
#     # permanence_period são tuplas
#     # exemplo: [(2, 2), (1, 2)...]
#     for period in permanence_period:
#         if (len(period) != 2 or
#                 not isinstance(period[0], int) or
#                 not isinstance(period[1], int)):
#             return None
#         # por isso é possível acessar os índices
#         elif period[0] <= target_time <= period[1]:
#             count += 1

#     return count


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


# target_time é o horário que está sendo testado
