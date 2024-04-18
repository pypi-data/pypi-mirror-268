
class FrozenDict(dict):
    def __init__(self, *args, **kwargs):
        self._orig = dict(*args, **kwargs)

        super().__init__(*args, **kwargs)

        for k, w in self.items():
            if isinstance(w, FrozenDict):
                continue
            if isinstance(w, dict):
                dict.__setitem__(self, k, FrozenDict({k : FrozenDict(v) if isinstance(v, dict) else v for k, v in w.items()}))
            elif isinstance(w, list):
                dict.__setitem__(self, k, tuple([FrozenDict(x) if isinstance(x, dict) else x for x in w]))

    def __readonly__(self, *args, **kwargs):
        raise RuntimeError("Cannot modify ReadOnlyDict")

    __setitem__ = __readonly__
    __delitem__ = __readonly__
    pop = __readonly__
    popitem = __readonly__
    clear = __readonly__
    update = __readonly__

    def __hash__(self):
        if not hasattr(self, '_hash'):
            self._hash = hash(tuple(self.items()))
        return self._hash

    def copy(self, mutable: bool = False) -> dict:
        if mutable:
            return self._orig.copy()
        return FrozenDict(self)
    