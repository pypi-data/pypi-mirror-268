def calc_new_size(cur_x, cur_y, target_w: int, target_h: int) -> tuple:
    if target_w is not None and target_w < 1:
        target_w = None
    if target_h is not None and target_h < 1:
        target_h = None
    if target_w is None and target_h is None:
        raise ValueError("At least one of w or h must be given")
    if target_w is None:
        ratio = target_h / cur_y
        new_x, new_y = int(cur_x * ratio), target_h
    elif target_h is None:
        ratio = target_w / cur_x
        new_x, new_y = target_w, int(cur_y * ratio)
    else:
        new_x, new_y = target_w, target_h

    return new_x, new_y
