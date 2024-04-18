"""
MIT License

Copyright (c) 2023 Peter Wendl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.    
"""

"""
This is a fork to Peter Wendl's work at "https://github.com/mextex/dicta/tree/main", which is licensed under the MIT License

The following modifications are made

- removed serializer and deserializer support since this class will not expect such input
- removed stringfy by introducing orjson.dumps
- removed and optimized some recurisive overhead
"""
from contextlib import contextmanager
import json
import os
import typing
from ._utils import force_hash
_placeholderObj = object()

class ExtOptions:
    raiseOnError = 0x01
    returnClosest = 0x02

def getDeep(
    d : dict, 
    *keys, 
    default = None,
    options : int = 0
):
    if len(keys) == 0:
        return d
    if len(keys) == 1:
        return d.get(keys[0], default)
    
    for key in keys[:-1]:
        if (
                key not in d and isinstance(d, dict
            )
            or (
                isinstance(d, list) and key >= len(d)
            )
        ):
            if options & ExtOptions.raiseOnError:
                raise KeyError(key)
            elif options & ExtOptions.returnClosest:
                return default
            return default
        d = d[key]
    
    
    if options & ExtOptions.raiseOnError:
        raise KeyError(keys[-1])
    elif options & ExtOptions.returnClosest:
        return default
    
    return d.get(keys[-1], default)

def iterTypeMapping(
    keys : typing.List[str] = None,
    mapping  : typing.Union[
        type, typing.List[typing.Tuple[typing.Type, int]], typing.Dict[str, typing.Type]
    ] = dict
):
    index = 0
    counter = 0
    while True:
        if index > len(keys) - 1:
            break
        
        if isinstance(mapping, type):
            yield mapping, keys[index]
        elif isinstance(mapping, list) and counter < len(mapping):
            # (dict, 3) (list, 2) yield 3 times dict and 2 times list
            for i in range(mapping[counter][1]):
                yield mapping[counter][0], keys[index]
            counter += 1
        elif isinstance(mapping, dict):
            yield mapping[keys[index]], keys[index]
            
        index += 1

def setDeep(
    d : dict, 
    *keysAndValue,
    expandMapping : typing.Union[
        type, typing.List[typing.Tuple[typing.Type, int]], typing.Dict[str, typing.Type]
    ] = dict
):
    if len(keysAndValue) == 0:
        raise KeyError("no keys passed in")
    
    if len(keysAndValue) == 1:
        raise KeyError("only 1 key passed in, missing value")
    
    if len(keysAndValue) == 2:
        d[keysAndValue[0]] = keysAndValue[1]
        return
    
    target = d
    for stype, key in iterTypeMapping(keysAndValue[:-2], expandMapping):
        if key not in target:
            target[key] = stype()
        target = target[key]
    
    target[keysAndValue[-2]] = keysAndValue[-1]

def setDeepSimple(d, *keysAndValue):
    if len(keysAndValue) < 2:
        raise ValueError("At least one key and one value are required")

    # Navigate through the keys, stopping before the last key to set the value
    target = d
    for i, key in enumerate(keysAndValue[:-2]):  # Iterate until the penultimate item
        next_key = keysAndValue[i+1]  # Look ahead to the next key to determine the required type

        if isinstance(key, int):  # Current key is an integer, so we expect a list at this level
            # Ensure the target is a list and is long enough
            while isinstance(target, dict) and key in target and not isinstance(target[key], list):
                target[key] = [target[key]]  # Convert to list if necessary
            if not isinstance(target, list):
                raise TypeError(f"Expected list at key '{key}' but found a dict.")
            while len(target) <= key:
                target.append({})
            target = target[key]
        else:  # Current key is not an integer, we expect a dict at this level
            if key not in target or not isinstance(target[key], (dict, list)):
                # Initialize the correct type based on the next key
                target[key] = [] if isinstance(next_key, int) else {}
            target = target[key]

    # Set the value for the last key
    final_key = keysAndValue[-2]
    if isinstance(final_key, int):  # Final key is an integer, prepare a list if necessary
        # Ensure the target is a list and is long enough
        if not isinstance(target, list):
            target = [target]  # Convert existing value to list
        while len(target) <= final_key:
            target.append(None)
        target[final_key] = keysAndValue[-1]
    else:  # Final key is not an integer, simply set the value in a dict
        target[final_key] = keysAndValue[-1]
    
def setDefault(
    d : dict,
    *keys,
    default,
    expandMapping : typing.Union[
        type, typing.List[typing.Tuple[typing.Type, int]], typing.Dict[str, typing.Type]
    ] = dict,
    useSimple : bool = False
):
    try:
        getDeep(d, *keys, options=ExtOptions.raiseOnError)
    except KeyError:
        if useSimple:
            setDeepSimple(d, *keys, default)
        else:
            setDeep(d, *keys, expandMapping=expandMapping, default=default)

# -------------------------------------------------------------------------------------------------------- Shared Capabilities
# The callback method for nested objects. 
# Calls the callback method of its parent -> the callback bubbles up the tree
class ParentCaller():
    def __init__(self, parent, call_to_parent):
        self.parent = parent
        self.call_to_parent = call_to_parent

    def setDeep(
        self,
        *keysAndValue,
        expandMapping : typing.Union[
            type, typing.List[typing.Tuple[typing.Type, int]], typing.Dict[str, typing.Type]
        ] = None
    ):
        with self.saveLock():
            if expandMapping is None:
                return setDeepSimple(self, *keysAndValue)

            setDeep(self, *keysAndValue, expandMapping=expandMapping)

    def getDeep(
        self,
        *keys,
        default = None,
        options : int = 0
    ):
        return getDeep(self, *keys, default=default, options=options)

    def __call_from_child__(self, modified_object, modify_info, modify_trace):
        modify_trace.insert(0, self)
        self.parent.__call_from_child__(modified_object=modified_object, modify_info=modify_info, modify_trace=[self])

# Method to convert childs to NestedDict, NestedList or NestedTuple Class, 
# giving them the ability to convert nested objects and to call its parrent on data change
class ChildConverter():
    def __convert_child__(self, child):
        if isinstance(child, dict):
            # iter throu childs and convert them if they are a dict, a list, a tuble or a set
            for key, value in child.items():
                if isinstance(value, dict) or isinstance(value, list) or isinstance(value, tuple)  or isinstance(value, set):
                    child[key] = self.__convert_child__(value)
            # subclass the dict
            nestedDict = NestedDict(parent=self, call_to_parent=self.__call_from_child__)
            nestedDict.update(child)
            return nestedDict
        elif isinstance(child, list):
            # iter throu childs and convert them if they are a dict, a list, a tuble or a set
            for i in range(len(child)):
                if isinstance(child[i], dict) or isinstance(child[i], list) or isinstance(child[i], tuple)  or isinstance(child[i], set):
                    child[i] = self.__convert_child__(child[i])
            # subclass the list
            nestedList = NestedList(parent=self, call_to_parent=self.__call_from_child__)
            nestedList.extend(child)
            return nestedList
        elif isinstance(child, tuple):
            # iter throu childs and convert them if they are a dict, a list, a tuble or a set
            for i in range(len(child)):
                if isinstance(child[i], dict) or isinstance(child[i], list) or isinstance(child[i], tuple)  or isinstance(child[i], set):
                    child[i] = self.__convert_child__(child[i])
            # subclass the tuple
            nestedTuple = NestedTuple(parent=self, call_to_parent=self.__call_from_child__, iterable=child)
            return nestedTuple
        elif isinstance(child, set):
            # no need to iter throu the child items of the set, as they are not changable
            # subclass the set
            nestedSet = NestedSet(parent=self, call_to_parent=self.__call_from_child__, iterable=child)
            return nestedSet
        else:
            return child

# Custom update function for dicts
class DictUpdater():
    def update(self, *args, **kwargs):
        '''Update dict'''
        if args:
            if len(args) > 1:
                raise TypeError("update() expects at most 1 arguments, "
                                "got %d" % len(args))
            other = dict(args[0])
            for key in other:
                self[key] = other[key]
        for key in kwargs:
            self[key] = kwargs[key]


# -------------------------------------------------------------------------------------------------------- Nested Set Class
class NestedSet(set, ParentCaller):
    def __init__(self, parent, call_to_parent, iterable):
        ParentCaller.__init__(self, parent, call_to_parent)
        r = super(NestedSet, self).__init__(iterable)
        modify_info = {
            "type": type(self),
            "mode": "new",
            "iterable": iterable
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        return r
    
    def __repr__(self):
        return str(set(self))
    
    def add(self, item):
        super(NestedSet, self).add(item)
        modify_info = {
            "type": type(self),
            "mode": "add",
            "item": item
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        
    def update(self, iterable):
        super(NestedSet, self).update(iterable)
        modify_info = {
            "type": type(self),
            "mode": "update",
            "item": iterable
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        
    def pop(self):
        r = super(NestedSet, self).pop()
        modify_info = {
            "type": type(self),
            "mode": "pop",
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        return r
        
    def remove(self, item):
        super(NestedSet, self).remove(item)
        modify_info = {
            "type": type(self),
            "mode": "remove",
            "value": item
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        
    def discard(self, item):
        super(NestedSet, self).discard(item)
        modify_info = {
            "type": type(self),
            "mode": "remove",
            "value": item
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        
    def clear(self):
        super(NestedSet, self).clear()
        modify_info = {
            "type": type(self),
            "mode": "clear"
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])


# -------------------------------------------------------------------------------------------------------- Nested Tuple Class
class NestedTuple(tuple, ChildConverter, ParentCaller):
    def __init__(self, parent, call_to_parent, iterable):
        ParentCaller.__init__(self, parent, call_to_parent)
        
    def __new__ (self, parent, call_to_parent, iterable):
        ParentCaller.__init__(self, parent, call_to_parent)
        r = super(NestedTuple, self).__new__(self, iterable)
        modify_info = {
            "type": type(self),
            "mode": "new",
            "iterable": iterable
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        return r


# -------------------------------------------------------------------------------------------------------- Nested Dict Class
class NestedDict(dict, ChildConverter, ParentCaller, DictUpdater):
    def __init__(self, parent, call_to_parent):
        ParentCaller.__init__(self, parent, call_to_parent)

    def __getitem__(self, *key):
        if isinstance(key, tuple) and len(key) > 1: 
            return getDeep(self, *key,  options=ExtOptions.raiseOnError)
        else:
            if isinstance(key, tuple):
                key = key[0]

            return super().__getitem__(key)

    def __setitem__(self, index, value):
        cval = self.__convert_child__(value)
        if isinstance(index, tuple):
            return setDeepSimple(self, *index, cval)
        else:
            super(NestedDict, self).__setitem__(index, cval)
        modify_info = {
            "type": type(self),
            "mode": "setitem",
            "key": index,
            "value": value
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])


    def __delitem__(self, key):
        super(NestedDict, self).__delitem__(key)
        modify_info = {
            "type": type(self),
            "mode": "delitem",
            "key": key
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])

    def clear(self):
        super(NestedDict, self).clear()
        modify_info = {
            "type": type(self),
            "mode": "clear"
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])

    def pop(self, key):
        r = super(NestedDict, self).pop(key)
        modify_info = {
            "type": type(self),
            "mode": "pop",
            "key": key
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        return r

    def popitem(self, key):
        r = super(NestedDict, self).popitem(key)
        modify_info = {
            "type": type(self),
            "mode": "popitem",
            "key": key
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        return r
    
    def setdefault(self, key, default=None):
        r = super(NestedDict, self).setdefault(key, default=default)
        modify_info = {
            "type": type(self),
            "mode": "setdefault",
            "key": key,
            "default": default
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        return r

    def update(self, *args, **kwargs):
        DictUpdater.update(self, *args, **kwargs)


# -------------------------------------------------------------------------------------------------------- Nested List Class
class NestedList(list, ChildConverter, ParentCaller):
    def __init__(self, parent, call_to_parent):
        ParentCaller.__init__(self, parent, call_to_parent)

    def get(self, *key, default=None):
        return getDeep(self, *key, default=default)

    def __getitem__(self, *key):
        if isinstance(key, tuple) and len(key) > 1:
            return getDeep(self, *key,  options=ExtOptions.raiseOnError)
        else:
            if isinstance(key, tuple):
                key = key[0]
            return list.__getitem__(self, key)

    def __add__(self, item):
        super(NestedList, self).__add__(item)
        modify_info = {
            "type": type(self),
            "mode": "add",
            "item": item
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])

    def __delitem__(self, index):
        super(NestedList, self).__delitem__(index)
        modify_info = {
            "type": type(self),
            "mode": "delitem",
            "index": index
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])

    def __delslice__(self, i, j):
        super(NestedList, self).__delslice__(i, j)
        modify_info = {
            "type": type(self),
            "mode": "delslice",
            "start": i,
            "end": j
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])

    def __setitem__(self, index, value):
        cval = self.__convert_child__(value)
        if isinstance(index, tuple):
            return setDeepSimple(self, *index, cval)
        else:
            super(NestedList, self).__setitem__(index, cval)

        modify_info = {
            "type": type(self),
            "mode": "setitem",
            "index": index,
            "value": value
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        
    def __setslice__(self, i, j, y):
        super(NestedList, self).__setslice__(i, j, y)
        modify_info = {
            "type": type(self),
            "mode": "setsclice",
            "start": i,
            "end": j,
            "item": y
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        
    def append(self, obj):
        '''L.append(object) -- append object to end'''
        super(NestedList, self).append(self.__convert_child__(obj))
        modify_info = {
            "type": type(self),
            "mode": "append",
            "item": obj
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        
    def extend(self, iterable):
        '''L.extend(iterable) -- extend list by appending elements from the iterable'''
        for item in iterable:
            self.append(self.__convert_child__(item))
        modify_info = {
            "type": type(self),
            "mode": "extend",
            "iterable": iterable
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        
    def insert(self, index, item):
        '''L.insert(index, object) -- insert object before index'''
        super(NestedList, self).insert(index, self.__convert_child__(item))
        modify_info = {
            "type": type(self),
            "mode": "insert",
            "index": index,
            "item": item
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        
    def pop(self, index=-1):
        '''L.pop([index]) -> item -- remove and return item at index (default last).
        Raises IndexError if list is empty or index is out of range.'''
        r = super(NestedList, self).pop(index)
        modify_info = {
            "type": type(self),
            "mode": "pop",
            "index": index
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        return r
        
    def remove(self, value):
        '''L.remove(value) -- remove first occurrence of value.
        Raises ValueError if the value is not present.'''
        super(NestedList, self).remove(value)
        modify_info = {
            "type": type(self),
            "mode": "remove",
            "value": value
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        
    def clear(self):
        super(NestedList, self).clear()
        modify_info = {
            "type": type(self),
            "mode": "clear"
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        
    def reverse(self):
        '''L.reverse() -- reverse *IN PLACE*'''
        super(NestedList, self).reverse()
        modify_info = {
            "type": type(self),
            "mode": "reverse",
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])
        
    def sort(self, key=None, reverse=False):
        '''L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
        cmp(x, y) -> -1, 0, 1'''
        super(NestedList, self).sort(key=key, reverse=reverse)
        modify_info = {
            "type": type(self),
            "mode": "sort",
            "key": key,
            "reverse": reverse
        }
        self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self])


# -------------------------------------------------------------------------------------------------------- SioBase Class
class SioBase(ChildConverter):
    def __init__(self, *args, **kwargs):
        self.path = None
        self.prevStamp = None
        self.callback = None
        self.callback_args = None
        self.callback_kwargs = None
        super().__init__(*args, **kwargs)
        self.loadMethod : typing.Callable = None
        self.saveMethod : typing.Callable= None
        self.clearMethod : typing.Callable = None
        self.syncToggleLock = False

    @contextmanager
    def saveLock(self, saveAfter : bool  = True):
        if self.syncToggleLock:
            yield
        else:
            self.syncToggleLock = True
            yield
            self.syncToggleLock = False
            if saveAfter:
                if hasattr(self, 'path') and self.path:
                    self.saveMethod(self, self.path)

   
    def bind(self, callback, response=None, *args, **kwargs):
        '''Set the callback function'''
        self.callback = callback
        self.response = response
        self.callback_args = args
        self.callback_kwargs = kwargs

    def syncFile(self, path, reset=False):
        '''Set the sync file path. Set reset=True if you want to reset the data in the file on startup. Default is False'''
        self.path = path
        if reset or not os.path.exists(path):
            self.clearMethod(path)
        data = self.loadMethod(path)

        # update
        return data
    
    def importFile(self, path, ignoreError=False):
        '''Insert/Import data from a file.'''
        if os.path.exists(path):
            data = self.loadMethod(path)
            return data
            # update
        else:
            if ignoreError:
                return
            raise FileNotFoundError("importFile: File '{}' does not exist.".format(path))
    
    def removeFile(self, path, ignoreError=False):
        '''Delete a file. Use with care'''
        if os.path.exists(path):
            os.remove(path)
        else:
            if ignoreError:
                return
            raise FileNotFoundError("removeFile: File '{}' does not exist.".format(path))
        
    #ANCHOR misc
    def setDeep(
        self,
        *keysAndValue,
        expandMapping : typing.Union[
            type, typing.List[typing.Tuple[typing.Type, int]], typing.Dict[str, typing.Type]
        ] = None
    ):
        with self.saveLock():
            if expandMapping is None:
                return setDeepSimple(self, *keysAndValue)

            setDeep(self, *keysAndValue, expandMapping=expandMapping)

    def getDeep(
        self,
        *keys,
        default = None,
        options : int = 0
    ):
        return getDeep(self, *keys, default=default, options=options)
    
    def __call_from_child__(self, modified_object, modify_info, modify_trace):
        self.currentStamp = hash(force_hash(self))
        if self.currentStamp != self.prevStamp:
            with self.saveLock():
                if hasattr(self, 'callback') and self.callback:
                    modify_trace.insert(0, self)
                    if self.response:
                        self.callback(modified_object=modified_object, modify_info=modify_info, modify_trace=[self], *self.callback_args, **self.callback_kwargs)    
                    else:
                        self.callback(*self.callback_args, **self.callback_kwargs)
            self.prevStamp = self.currentStamp

class SioBaseDict(dict, SioBase, DictUpdater):
    '''
    A dict subclass that observes a nested dict and listens for changes in its data 
    structure. If a data change is registered, reacts with a callback 
    or a data-export to a JSON file.

    Automatically write data to a JSON file, when the nested data structure changes (optional)
    Throw a callback method, when the nested data structure changes (optional)

    Behaves like a regular dict and supports all dict and list methods like pop(), append(), slice()...
    Supports nesting of all possible datatypes like dict, list, tuple, set and other objects like custom classes.
    Writing data to a file will encode a non-serializable object to a binary-string.
    Reading data from a file will decode a binary-string back to a non-serializable object.
    You can import additional data from json files.
    You can export data to json files.
    '''
        
    def __init__(self, *args, **kwargs):
        SioBase.__init__(self)
        dict.__init__(self)
        self.update(*args, **kwargs)

    def __getitem__(self, __key):
        if isinstance(__key, tuple):
            return getDeep(self, *__key,  options=ExtOptions.raiseOnError)
        else:
            return super(SioBaseDict, self).__getitem__(__key)

    def __setitem__(self, key, val):
        cval = self.__convert_child__(val)
        if isinstance(key, tuple) and len(key) > 1:
            return setDeepSimple(self, *key, cval)
        else:
            if isinstance(key, tuple):
                key = key[0]
            super(SioBaseDict, self).__setitem__(key, cval)

        if hasattr(self, 'callback') and self.callback:
            if self.response:
                modify_info = {
                    "type": type(self),
                    "mode": "setitem",
                    "key": key,
                    "value": val
                }
                self.callback(modified_object=self, modify_info=modify_info, modify_trace=[self], *self.callback_args, **self.callback_kwargs)
            else:
                self.callback(*self.callback_args, **self.callback_kwargs)
        with self.saveLock():
            pass

    def __delitem__(self, key):
        super(SioBaseDict, self).__delitem__(key)
        if self.response:
            modify_info = {
                "type": type(self),
                "mode": "delitem",
                "key": key
            }
            self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self], *self.callback_args, **self.callback_kwargs)
        else:
            self.callback(*self.callback_args, **self.callback_kwargs)

    def clear(self):
        super(SioBaseDict, self).clear()
        if self.response:
            modify_info = {
                "type": type(self),
                "mode": "clear"
            }
            self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self], *self.callback_args, **self.callback_kwargs)
        else:
            self.callback(*self.callback_args, **self.callback_kwargs)

    def pop(self, key):
        r = super(SioBaseDict, self).pop(key)
        if self.response:
            modify_info = {
                "type": type(self),
                "mode": "pop",
                "key": key
            }
            self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self], *self.callback_args, **self.callback_kwargs)
        else:
            self.callback(*self.callback_args, **self.callback_kwargs)
        return r

    def popitem(self, key):
        r = super(SioBaseDict, self).popitem(key)
        if self.response:
            modify_info = {
                "type": type(self),
                "mode": "popitem",
                "key": key
            }
            self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self], *self.callback_args, **self.callback_kwargs)
        else:
            self.callback(*self.callback_args, **self.callback_kwargs)
        return r
    
    def setdefault(self, key, default=None):
        r = super(SioBaseDict, self).setdefault(key, default=default)
        if self.response:
            modify_info = {
                "type": type(self),
                "mode": "setdefault",
                "key": key,
                "default": default
            }
            self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self], *self.callback_args, **self.callback_kwargs)
        else:
            self.callback(*self.callback_args, **self.callback_kwargs)
        return r

    def update(self, *args, **kwargs):
        '''Update the data tree with *args and **kwargs'''
        DictUpdater.update(self, *args, **kwargs)

    def bind(self, callback, response=None, *args, **kwargs):
        '''Set the callback function'''
        self.callback = callback
        self.response = response
        self.callback_args = args
        self.callback_kwargs = kwargs

    def syncFile(self, path, reset=False):
        '''Set the sync file path. Set reset=True if you want to reset the data in the file on startup. Default is False'''
        data = super(SioBaseDict, self).syncFile(path, reset)
        self.update(**data)

    def importFile(self, path, ignoreError=False):
        '''Insert/Import data from a file.'''
        data = super(SioBaseDict, self).importFile(path, ignoreError)
        if data:
            self.update(**data)
    
    def importData(self, *args, **kwargs):
        '''
        Insert/Import data.
        
        importData(dict)
        importData(key=value,key2=value…)
        
        '''
        self.update(*args, **kwargs)
    

    def removeFile(self, path, ignoreError=False):
        '''Delete a file. Use with care'''
        if os.path.exists(path):
            os.remove(path)
        else:
            if ignoreError:
                return
            raise FileNotFoundError("removeFile: File '{}' does not exist.".format(path))
        
class SioBaseList(list, SioBase, ChildConverter):
    def __init__(self, *args):
        SioBase.__init__(self)  # Assuming SioBase does not require arguments
        list.__init__(self)
        if args:
            if len(args) == 1 and isinstance(args[0], typing.Iterable):
                self.extend(args[0])
            else:
                self.extend(args)

    def __setitem__(self, key, value):
        converted_value = self.__convert_child__(value)
        super(SioBaseList, self).__setitem__(key, converted_value)
        self.__detailed_callback(mode="setitem", key=key, value=value)
        with self.saveLock():
            pass

    def append(self, value):
        with self.saveLock():
            converted_value = self.__convert_child__(value)
            super(SioBaseList, self).append(converted_value)
            self.__detailed_callback(mode="append", value=value)

    def extend(self, iterable):
        with self.saveLock():
            for item in iterable:
                self.append(item)  # Leverage the overridden append for conversion and callbacks

    def insert(self, index, value):
        with self.saveLock():
            converted_value = self.__convert_child__(value)
            super(SioBaseList, self).insert(index, converted_value)
            self.__detailed_callback(mode="insert", index=index, value=value)

    def __detailed_callback(self, mode, key=None, value=None, index=None, values=None):
        if hasattr(self, 'callback') and self.callback:
            if hasattr(self, 'response') and self.response:
                modify_info = {
                    "type": type(self),
                    "mode": mode,
                    "key": key,
                    "value": value,
                    "index": index,
                    "values": values
                }
                self.call_to_parent(modified_object=self, modify_info=modify_info, modify_trace=[self], *self.callback_args, **self.callback_kwargs)
            else:
                self.callback(*self.callback_args, **self.callback_kwargs)

# WRAPPER
class SioWrapper(SioBaseDict):
    def __init__(
        self, 
        path : str, 
        *args, 
        reset : bool = False,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.loadMethod = self._load
        self.saveMethod = self._save
        self.clearMethod = self._clear
        self.syncFile(path, reset)
        
    @staticmethod
    def _load(path : str):
        try:
            import orjson
            with open(path, 'rb') as f:
                return orjson.loads(f.read())
        except ImportError:
            with open(path, 'r') as f:
                return json.load(f)
    
    @staticmethod
    def _save(d, path : str):
        try:
            import orjson 
            with open(path, 'wb') as f:
                f.write(orjson.dumps(d))
        except ImportError:
            with open(path, 'w') as f:
                json.dump(d, f, indent=4)
    
    @staticmethod
    def _clear(path : str):
        with open(path, 'w') as f:
            f.write("{}")

class SioList(SioBaseList):
    def __init__(self, path : str, *args, reset : bool = False):
        super().__init__(*args)
        self.loadMethod = SioWrapper._load
        self.saveMethod = SioWrapper._save
        self.clearMethod = self._clear
        self.syncFile(path, reset)

    @staticmethod
    def _clear(path : str):
        with open(path, 'w') as f:
            f.write("[]")