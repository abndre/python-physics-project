def calc_speed_mean(x2: float,
                    x1: float,
                    t2: float,
                    t1: float):
    """
    v = delta s / delta t
    v = x2 - x1 / t2 - t1
    """
    speed_mean = (x2 - x1) / (t2 - t1)
    # print('speed mean:', speed_mean)
    return speed_mean
