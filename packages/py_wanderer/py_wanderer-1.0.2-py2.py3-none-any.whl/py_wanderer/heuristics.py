from math import radians, sin, cos, sqrt, atan2

def euclidean(a: tuple[int, int], b: tuple[int, int]) -> float:
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def squared_euclidean(a: tuple[int, int], b: tuple[int, int]) -> float:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def manhattan(a: tuple[int, int], b: tuple[int, int]) -> float:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def chebyshev(a: tuple[int, int], b: tuple[int, int]) -> float:
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

def octile(a: tuple[int, int], b: tuple[int, int]) -> float:
    return max(dx := abs(a[0] - b[0]), dy := abs(a[1] - b[1])) + (sqrt(2) - 1) * min(dx, dy)

def hamming(a: tuple[int, int], b: tuple[int, int]) -> int:
    return sum(x != y for x, y in zip(a, b))

def canberra(a: tuple[int, int], b: tuple[int, int]) -> float:
    return sum(abs(x - y) / (abs(x) + abs(y)) if (x or y) else 0 for x, y in zip(a, b))

def cosine_similarity(a: tuple[int, int], b: tuple[int, int]) -> float:
    dot_product = sum(x*y for x, y in zip(a, b))
    magnitude_a = sqrt(sum(x*x for x in a))
    magnitude_b = sqrt(sum(y*y for y in b))
    if magnitude_a == 0 or magnitude_b == 0:  # avoid division by zero
        return 0
    return dot_product / (magnitude_a * magnitude_b)

def hexagonal_distance(a: tuple[int, int], b: tuple[int, int]) -> float:
    ax, ay = a
    bx, by = b
    dx = bx - ax
    dy = by - ay
    return max(abs(dx), abs(dy), abs(dx + dy))

def jaccard_distance(a: tuple[int, int], b: tuple[int, int]) -> float:
    intersection = len(set(a) & set(b))
    union = len(set(a) | set(b))
    return 1 - intersection / union if union != 0 else 1

def haversine(a: tuple[float, float], b: tuple[float, float]) -> float:
    R = 6371  # Earth radius in kilometers
    lat1, lon1 = map(radians, a)
    lat2, lon2 = map(radians, b)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


HEURISTICS = [
        euclidean, 
        manhattan, 
        chebyshev, 
        octile, 
        hamming, 
        canberra, 
        cosine_similarity,
        squared_euclidean,
        hexagonal_distance,
        jaccard_distance,
        haversine
]
