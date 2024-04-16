import dataclasses
from copy import deepcopy

from construct import Container

SQUARE = [[-1, -1, 3],
          [-1, 0, 1],
          [1, 0, 1],
          [-1, 1, 3]]

CROSS5 = [[0, -2, 1],
          [0, -1, 1],
          [-2, 0, 5],
          [0, 1, 1],
          [0, 2, 1]]

BIRD = [[0, 0, 1],
        [-1, 1, 1],
        [1, 1, 1],
        [-2, 2, 1],
        [2, 2, 1],
        [-3, 3, 1],
        [3, 3, 1]]

CROSS3 = [[0, -1, 1],
          [-1, 0, 3],
          [0, 1, 1]]

VLINE5 = [[0, -2, 1],
          [0, -1, 1],
          [0, 0, 1],
          [0, 1, 1],
          [0, 2, 1]]

NUMBER = {
    0: [[-2, -3, 5],
        [-2, 3, 5],
        [-2, -2, 1],
        [-2, -1, 1],
        [-2, 0, 1],
        [-2, 1, 1],
        [-2, 2, 1],
        [2, -2, 1],
        [2, -1, 1],
        [2, 0, 1],
        [2, 1, 1],
        [2, 2, 1]],

    1: [[-2, -3, 3],
        [-2, 3, 5],
        [0, -2, 1],
        [0, -1, 1],
        [0, 0, 1],
        [0, 1, 1],
        [0, 2, 1]],

    2: [[-2, -3, 5],
        [2, -2, 1],
        [2, -1, 1],
        [-2, 0, 5],
        [-2, 1, 1],
        [-2, 2, 1],
        [-2, 3, 5]],

    3: [[-2, -3, 5],
        [2, -2, 1],
        [2, -1, 1],
        [0, 0, 2],
        [2, 1, 1],
        [2, 2, 1],
        [-2, 3, 5]],

    4: [[-2, -3, 1],
        [-2, -2, 1],
        [-2, -1, 1],
        [2, -3, 1],
        [2, -2, 1],
        [2, -1, 1],
        [-2, 0, 5],
        [2, 1, 1],
        [2, 2, 1]],

    5: [[-2, -3, 5],
        [-2, -2, 1],
        [-2, -1, 1],
        [-2, 0, 5],
        [2, 1, 1],
        [2, 2, 1],
        [-2, 3, 5]],

    6: [[-2, -3, 5],
        [-2, -2, 1],
        [-2, -1, 1],
        [-2, -0, 5],
        [-2, 1, 1],
        [-2, 2, 1],
        [2, 1, 1],
        [2, 2, 1],
        [-2, 3, 5]],

    7: [[-2, -3, 5],
        # [-2, -2, 1],
        [2, -2, 1],
        [2, -1, 1],
        [1, 0, 1],
        [0, 1, 1],
        [0, 2, 1],
        [0, 3, 1]],

    8: [[-2, -3, 5],
        [-2, -2, 1],
        [-2, -1, 1],
        [2, -2, 1],
        [2, -1, 1],
        [-1, 0, 3],
        [-2, 1, 1],
        [-2, 2, 1],
        [2, 1, 1],
        [2, 2, 1],
        [-2, 3, 5]],

    9: [[-2, -3, 5],
        [-2, -2, 1],
        [-2, -1, 1],
        [-2, 0, 5],
        [2, -2, 1],
        [2, -1, 1],
        [2, 1, 1],
        [2, 2, 1],
        [-2, 3, 5]],
}

NUM = list(NUMBER.values())


@dataclasses.dataclass
class Item:
    x: int
    y: int
    q: int


class Element:

    def __init__(self, mil, t):
        self.mil = mil
        self.t = [Item(*item) for item in t]

    def __repr__(self):
        return f'<({self.mil}, {len(self.t)})>'

    def append(self, other):
        if isinstance(other, Item):
            self.t.append(other)
        else:
            raise TypeError

    def __add__(self, other):
        if isinstance(other, (int, float)):
            for i in self.t:
                i.x += other
            return self
        elif isinstance(other, Element):
            for i in other.t:
                self.t.append(i)
            return self
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            for i in self.t:
                i.x -= other
            return self
        raise TypeError


El = Element

SMALL_RET = ((1, 230, 320), (1, 231, 320), (1, 232, 320), (1, 233, 320), (1, 234, 320), (1, 235, 320), (1, 236, 320),
             (1, 237, 320), (1, 238, 320), (1, 239, 320), (21, 240, 310), (1, 241, 320), (1, 242, 320), (1, 243, 320),
             (1, 244, 320), (1, 245, 320), (1, 246, 320), (1, 247, 320), (1, 248, 320), (1, 249, 320), (1, 250, 320))


def create_row_supersonic(distance):
    if distance == 100:
        return [El(x, VLINE5) for x in range(-5, 0)] + [El(0, BIRD)] + [El(x, VLINE5) for x in range(1, 6)]
    elif distance % 100 == 0:
        row = [El(-1, SQUARE), El(0, CROSS5), El(1, SQUARE)]
        nums = [int(i) for i in str(distance // 100)]
        nums.reverse()
        num = El(-3, [])
        move = 0
        for i in nums:
            num += El(-3, NUM[i]) - move
            move += 7
        row.insert(0, num)
        return deepcopy(row)
    elif distance % 100 == 50:
        return [El(0, CROSS3)]


def create_row_subsonic(distance):
    if distance == 50:
        return [El(x, VLINE5) for x in range(-5, 0)] + [El(0, BIRD)] + [El(x, VLINE5) for x in range(1, 6)]
    elif distance % 100 == 0:
        row = [El(-1, SQUARE), El(0, CROSS5), El(1, SQUARE)]
        nums = [int(i) for i in str(distance // 1)]
        nums.reverse()
        num = El(-5, [])
        move = 0
        for i in nums:
            num += El(-2, NUM[i]) - move
            move += 7
        row.insert(0, num)
        return deepcopy(row)
    elif distance % 100 == 50:
        return [El(0, CROSS3)]


def create_hold_reticle(distances, click, zoom=1, addy=9, subsonic=False):
    y = 0
    mil = 10000 / click * zoom

    img_data = []

    create = create_row_subsonic if subsonic or distances[0] == 50 else create_row_supersonic

    for d in distances:
        macro = []
        row = create(d)
        if row:
            macro.append(Item(700, round(d / 10), 0))
            macro.append(Item(700, 0, 0))
            macro.append(Item(700, y, 0))

            for el in row:

                for it in el.t:
                    it.x += round(mil * el.mil) + 320
                    it.y += y + 240
                    macro.append(it)

            y += addy
            # addy += 1

        img_data = macro + img_data
    img_data.append(Item(700, 1000, 0))

    conts = [Container(x=it.x, y=it.y, q=it.q) for it in img_data]
    return conts
