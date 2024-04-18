from contextlib import contextmanager
import json
import os
from teslastruct._utils import force_hash

class DetectionDescriptor:

    def __init__(self, func):
        self.__func = func

    def __get__(self, obj, cls):
        if obj is None:
            return self
        
        def runner(*args, **kwargs):
            res = self.__func(obj, *args, **kwargs)
            hash(obj)
            return res

        return runner

class LiteOnChangeBase:
    initialWriteData = None

    @contextmanager
    def _saveLock(self):
        try:
            self.__saveLock += 1
            yield
        finally:
            self.__saveLock -= 1
            if self.__saveLock == 0:
                hash(self)

    def __init__(self, path):
        self.__hash = None
        self.__saveLock = 0

        path = os.path.abspath(path)

        self.__path = path

        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(path)

        if not os.path.exists(path):
            with open(path, 'w'):
                self.writeFile(path, self.initialWriteData)

    @staticmethod
    def writeFile(path, data):
        with open(path, 'w') as f:
            if isinstance(data, str):
                f.write(data)
            elif isinstance(data, (dict, list)):
                json.dump(data, f, indent=4)

    @staticmethod
    def readFile(path):
        with open(path, 'r') as f:
            if path.endswith('.json'):
                return json.load(f)

        raise RuntimeError(f'Cannot read {path}')

    @property
    def savePath(self):
        return self.__path
    
    def __hash__(self):
        newhash = hash(force_hash(self))

        if self.__hash != newhash and self.__saveLock == 0:
            self.writeFile(self.savePath, self)

        self.__hash = newhash
        return self.__hash

class LiteOnChangeList(LiteOnChangeBase, list):
    initialWriteData = '[]'
    def __init__(self, path : str, *args, **kwargs):
        LiteOnChangeBase.__init__(self, path)
        list.__init__(self)
        with self._saveLock():
            self.extend(self.readFile(path))
            self.extend(list(*args, **kwargs))
    
    append = DetectionDescriptor(list.append)
    extend = DetectionDescriptor(list.extend)
    insert = DetectionDescriptor(list.insert)
    remove = DetectionDescriptor(list.remove)
    pop = DetectionDescriptor(list.pop)
    clear = DetectionDescriptor(list.clear)
    sort = DetectionDescriptor(list.sort)
    __setitem__ = DetectionDescriptor(list.__setitem__)
    __delitem__ = DetectionDescriptor(list.__delitem__)
    __iadd__ = DetectionDescriptor(list.__iadd__)
    __imul__ = DetectionDescriptor(list.__imul__)
    __rmul__ = DetectionDescriptor(list.__rmul__)
    __reversed__ = DetectionDescriptor(list.__reversed__)
    #__contains__ = DetectionDescriptor(list.__contains__)
    #__iter__ = DetectionDescriptor(list.__iter__)
    __len__ = DetectionDescriptor(list.__len__)
    __repr__ = DetectionDescriptor(list.__repr__)
    __str__ = DetectionDescriptor(list.__str__)
    __add__ = DetectionDescriptor(list.__add__)
    __mul__ = DetectionDescriptor(list.__mul__)
    __rmul__ = DetectionDescriptor(list.__rmul__)
    
    
class LiteOnChangeDict(LiteOnChangeBase, dict):
    initialWriteData = '{}'
    def __init__(self, path : str, *args, **kwargs):
        LiteOnChangeBase.__init__(self, path)
        dict.__init__(self)
        with self._saveLock():
            self.update(self.readFile(path))
            self.update(dict(*args, **kwargs))
        hash(self)
    
    __setitem__ = DetectionDescriptor(dict.__setitem__)
    __delitem__ = DetectionDescriptor(dict.__delitem__)
    pop = DetectionDescriptor(dict.pop)
    popitem = DetectionDescriptor(dict.popitem)
    clear = DetectionDescriptor(dict.clear)
    update = DetectionDescriptor(dict.update)
    setdefault = DetectionDescriptor(dict.setdefault)

