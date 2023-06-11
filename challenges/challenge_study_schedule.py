def study_schedule(permanence_period, target_time):

    try:
        result = sum(
            1
            for login, logout in permanence_period
            if login <= target_time <= logout
        )
    except TypeError:
        return None
    return result
