from typing import Optional, Tuple


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


def calc_crop_values(
    img_width: int,
    img_height: int,
    x1: Optional[int] = None,
    y1: Optional[int] = None,
    x2: Optional[int] = None,
    y2: Optional[int] = None,
) -> Tuple[int, int, int, int]:
    if x1 is None:
        x1 = 0
    if y1 is None:
        y1 = 0
    if x2 is None:
        x2 = img_width
    if y2 is None:
        y2 = img_height

    if x1 < 0 or x1 > img_width:
        x1 = x1 % img_width
    if y1 < 0 or y1 > img_height:
        y1 = y1 % img_height
    if x2 < 0 or x2 > img_width:
        x2 = x2 % img_width
    if y2 < 0 or y2 > img_height:
        y2 = y2 % img_height

    return x1, y1, x2, y2
