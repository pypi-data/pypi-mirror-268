
from teslastruct.frozen import FrozenDict

class DictWithDictKeys(dict):
    def __keytransform__(self, key):
        if isinstance(key, dict):
            return FrozenDict(key)
        return key

    def __setitem__(self, key, value):
        super().__setitem__(self.__keytransform__(key), value)

    def __getitem__(self, key):
        return super().__getitem__(self.__keytransform__(key))

    def __delitem__(self, key):
        super().__delitem__(self.__keytransform__(key))

    def __contains__(self, key):
        return super().__contains__(self.__keytransform__(key))

    def get(self, key, default=None):
        return super().get(self.__keytransform__(key), default)

    def pop(self, key, default=None):
        return super().pop(self.__keytransform__(key), default)