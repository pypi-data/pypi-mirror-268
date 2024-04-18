from .frozen import FrozenDict

def force_hash(x):
    if isinstance(x, dict):
        return FrozenDict(x)
    if isinstance(x, list):
        return tuple([force_hash(y) for y in x])
    return x