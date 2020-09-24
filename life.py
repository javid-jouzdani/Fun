LIFE_STAGE_MAP = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: tuple(),  # 5 has no neighbors
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6),
}

POSSIBILITY_STAGE_MAP = {
    1: (1, 2, 4),
    2: (2, 3, 5),
    3: (1, 0, 3),
    4: (1, 7),
    5: (9, 7),
    6: (5, 3),
    7: (3, 2, 8),
    8: (9, 3, 4),
    9: (2, 7, 4, 1),
    0: (6, 7, 9),
}

def possibilites(stage):
    return POSSIBILITY_STAGE_MAP[stage]

def next_life_stage(stage):
    return LIFE_STAGE_MAP[stage]

def yield_value(birth, time_to_live, created_value=0):  
    if time_to_live == 0:
        yield created_value
        return
    for stage in next_life_stage(birth):
        yield from yield_value(stage, time_to_live-1, 
                               created_value+max(possibilites(stage)))

def calc_total_value_created(birth, life_length):
    total_value = 0
    for value in yield_value(birth, life_length):
        total_value += value
    return total_value

if __name__ == '__main__':                                      
    print(calc_total_value_created(6, 2))  