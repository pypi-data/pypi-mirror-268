import math


def euclidean_distance(ca: tuple, cb: tuple):
    r1, g1, b1, _ = ca
    r2, g2, b2, _ = cb
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)


def _dot_product(vector1, vector2):
    return sum(x * y for x, y in zip(vector1, vector2))


def _norm(vector):
    return math.sqrt(sum(x ** 2 for x in vector))


def cosine_similarity(ca: tuple, cb: tuple):
    dot_prod = _dot_product(ca, cb)
    norm_prod = _norm(ca) * _norm(cb)
    return dot_prod / norm_prod if norm_prod != 0 else 0


def cosine_distance(ca: tuple, cb: tuple):
    return 1 - cosine_similarity(ca, cb)
